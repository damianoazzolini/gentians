import math
import sys
import itertools
import random
import copy
import time

import utils

import argparse

import os.path

import strategies

from clingo_interface import ClingoInterface
from clingo_interface import Coverage

from program_sampler import ProgramSampler
from variable_placer import VariablePlacer

import example_programs

program_description = "GENTIANS: GENeTic algoritm for inductive learning of ANswer Set programs."

version = "1.0.1" 

class Program:
    def __init__(self,
        # clauses : 'list[Clause]',
        clauses : 'list[str]',
        covered_positive : int,
        covered_negative : int
        ) -> None:
        self.clauses : 'list[str]' = clauses
        self.covered_positive : float = covered_positive
        self.covered_negative : float = covered_negative
        self.complexity_n_atoms : int = self.get_complexity_n_atoms()
        self.complexity_n_variables : int = self.get_complexity_n_variables()
        
    def get_complexity_n_atoms(self) -> int:
        '''
        Returns the complexity of the program as the number
        of atoms in all the clauses.
        '''
        complexity : int = 0
        for c in self.clauses:
            nl = c.replace(' ', '').split(':-')
            h = nl[0]
            b = nl[1]
            # to handle facts and constraints add or not 1
            complexity += h.count('),') + (1 if len(h) > 0 else 0) + b.count('),') + (1 if len(b) > 0 else 0)

        return complexity
    
    def get_complexity_n_variables(self) -> int:
        '''
        Computes the complexity as the number of variables in clauses.
        '''
        stop = False
        i = 0
        while not stop:
            r = f"V{i}"
            cl = ' '.join(self.clauses)
            if not (r in cl):
                stop = True
            i += 1
        return i - 1

    def get_program_str(self) -> str:
        if len(self.clauses) > 0:
            return '\nPROGRAM\n' + '\n'.join(self.clauses) + '\nATOMS: ' + str(self.complexity_n_atoms) + '\nVARIABLES: ' + str(self.complexity_n_variables) + '\n'
        else:
            return '\nEMPTY PROGRAM\n'
        # for c in self.clauses:
        #     # s += c.get_clause() + '\n' 
        #     s += c + '\n' 
        # return s

    # def get_program_list(self) -> 'list[str]':
    #     s : 'list[str]' = []
    #     for c in self.clauses:
    #         # s.append(c.get_clause()) 
    #         s.append(c) 
    #     return s

    def __str__(self) -> str:
        return self.get_program_str() + f"Covered positive: {self.covered_positive} - negative: {self.covered_negative}\n"
    
    def __repr__(self) -> str:
        return self.__str__()


class Solver:
    def __init__(self, 
        background : 'list[str]',
        positive_examples : 'list[list[str]]',
        negative_examples : 'list[list[str]]',
        language_bias_head : 'list[str]',
        language_bias_body : 'list[str]',
        arguments : argparse.Namespace
        ) -> None:
        self.background : 'list[str]' = background
        self.positive_examples : 'list[list[str]]' = positive_examples
        self.negative_examples : 'list[list[str]]' = negative_examples
        self.language_bias_head : 'list[str]' = language_bias_head
        self.language_bias_body : 'list[str]' = language_bias_body
        self.verbose : int = arguments.verbose
        self.max_depth : int = arguments.depth
        self.max_variables : int = arguments.variables
        self.disjunctive_head_length : int = arguments.disjunctive_head
        self.unbalanced_aggregates : bool = arguments.unbalanced_agg
        self.sample_loops : int = arguments.iterations
        self.n_clauses_genetic : int = arguments.clauses
        self.pop_size_genetic : int = arguments.pop_size
        self.mutation_probability : float = arguments.mutation_probability
        self.iterations_genetic : int = arguments.iterations_genetic
        self.arguments = arguments
        self.max_as = arguments.max_as
        
        self.aggregates : 'list[str]' = arguments.aggregates
        self.comparison : 'list[str]' = arguments.comparison
        self.arithm : 'list[str]' = arguments.arithm
        self.cr : bool = arguments.cr # for choice rules
        self.invention : bool = arguments.invention # predicate invention
    

    def solve(self) -> None:
        '''
        Main loop
        '''

        best_found : bool = False
        best_stub_for_next_round : 'list[str]' = []

        sampler = ProgramSampler(
            self.language_bias_head,
            self.language_bias_body,
            max_depth = self.max_depth,
            max_variables = self.max_variables,
            prob_increase_level= self.arguments.prob_increase,
            # max_clauses = max_clauses,
            verbose = self.verbose,
            enable_find_max_vars_stub=False,
            find_all_possible_pos_for_vars_one_shot=True,
            disjunctive_head_length=self.disjunctive_head_length,
            unbalanced_aggregates=self.unbalanced_aggregates,
            allowed_aggregates=self.aggregates,
            arithmetic_operators=self.arithm,
            comparison_operators=self.comparison
        )

        placer = VariablePlacer(
            max_variables=self.max_variables,
            verbose=self.verbose,
            unbalanced_aggregates=self.unbalanced_aggregates
        )
        
        start_total_time = time.time()
        
        for it in range(self.sample_loops):
            # Step 0: sample a list of clauses
            print(f"Sampling loop: {it}")
            start_time = time.time()
            print("Sampling clauses")
            cls = sampler.sample_clause_stub(self.arguments.sample)
            sample_time = time.time() - start_time
            
            # add the best from the previous rounds
            cls.extend(best_stub_for_next_round)
            # clean up the best stub
            best_stub_for_next_round = []
            # Step 1: remove duplicates
            sampled_clauses = sorted(list(set(cls)))
            print(f"Sampled {len(sampled_clauses)} different clauses in {sample_time} seconds")
            # sys.exit()
            if self.verbose >= 1:
                print("Sampled clauses:")
                sampled_clauses.sort(key=lambda x : len(x))
                for index, current_cl in enumerate(sampled_clauses):
                    print(f"{index}) {current_cl}")

            # Step 2: place the variables
            # This is THE bottleneck: generation of all the 
            # possible locations, which are #n_vars^#n_pos in the 
            # worst case
            start_time = time.time()
            
            placed_list : 'list[list[str]]' = placer.place_variables_list_of_clauses(sampled_clauses)
            placing_time = time.time() - start_time
            print(f"Placed variables in {placing_time} seconds")

            placed_list_improved : 'list[strategies.PlacedClause]' = []
            for p in placed_list:
                pl = strategies.PlacedClause(p)
                placed_list_improved.append(pl)

            print(f"Total clauses stub: {len(placed_list)}")
            print(f"Total number of possible clauses: {sum(len(pl) for pl in placed_list)}")

            if len(placed_list) == 0:
                print("No clauses found")
                sys.exit()

            if self.verbose >= 2:
                for el in placed_list:
                    print(f"{len(el)}: {el}")

            # Step 3: genetic algorithm
            start_time = time.time()
            current_strategy = strategies.Strategy(
                placed_list_improved,
                self.background,
                positive_examples,
                negative_examples
            )

            prg, score, best_found, best_index_stub_for_the_next_round = current_strategy.genetic_solver(
                self.n_clauses_genetic,
                self.pop_size_genetic,
                self.mutation_probability,
                self.iterations_genetic)
            genetic_time = time.time() - start_time
            
            for i in best_index_stub_for_the_next_round:
                best_stub_for_next_round.append(sampled_clauses[i]) 
            # print(best_stub_for_next_round)
            print(f"Evolutionary cycle {it} - Time {genetic_time}")
            if best_found:
                print("--- Found best program ---")
            else:
                print(f"Current best with score: {score}")
            for r in prg:
                print(r)
            print("--------------------------")
            # print(f"Program: {prg}")
            if best_found:
                break
        
        print(f"Total time: {time.time() - start_total_time}")


if __name__ == "__main__":
    command_parser = argparse.ArgumentParser(description=program_description)
    command_parser.add_argument("-dir", "--directory", help="Directory storing the \
        bk.pl, exs.pl, and bias.pl files (Popper format).", type=str, default=".")
    command_parser.add_argument("-v", "--verbose", help="Verbose mode", type=int, \
        choices=range(0,3), default=0)
    
    command_parser.add_argument("-vars", "--variables", help="Max variables to consider \
        in a rule", type=int, default=3)
    command_parser.add_argument("-d", "--depth", help="Max literals in rules", \
        type=int, default=3)
    command_parser.add_argument("-pil", "--prob-increase", help="Probability to add one \
        more literal in the current clause (used in sampling)", \
        type=float, default=0.5)
    command_parser.add_argument("-dh", "--disjunctive-head", help="Max atoms in head", \
        type=int, default=1)
    command_parser.add_argument("-s", "--sample", help="Number of clauses to sample",\
        type=int, default=1000)
    command_parser.add_argument("-ua", "--unbalanced-agg", help="Unabalnced aggregates",\
        default=False, action="store_true")
    command_parser.add_argument("--max_as", help="Max number of answer sets to generate",\
        type=int, default=5000)
    
    command_parser.add_argument("-c", "--clauses", help="Max clauses to consider in a \
        program", type=int, default=6)
    command_parser.add_argument("-it", "--iterations", help="Max number of sample and \
        genetic iterations", type=int, default=100)
    command_parser.add_argument("-p", "--pop-size", help="Size of the population",\
        type=int, default=50)
    command_parser.add_argument("-itg", "--iterations-genetic", help="Number of \
        iterations for the genetic algorithm", type=int, default=2000)
    command_parser.add_argument("-mp", "--mutation-probability", help="Mutation \
        probability", type=float, default=0.2)
    command_parser.add_argument("-e", "--example", help="Load a predefined example",
        choices=[
            "coin", 
            "even_odd",
            "animals_bird",
            "coloring",
            "adjacent_to_red",
            "grandparent",
            "4queens",
            "5queens", 
            "clique", 
            "sudoku",
            # "dummy", 
            "subset_sum",
            "subset_sum_double",
            "subset_sum_double_and_sum",
            "subset_sum_double_and_prod",
            "subset_sum_triple",
            "hamming_0", 
            "hamming_1", 
            # "harder_hamming_0",
            # "harder_hamming_1",
            "magic_square_no_diag", 
            "latin_square", 
            "set_partition_sum",
            "set_partition_sum_and_cardinality", 
            "set_partition_sum_cardinality_and_square",
            "set_partition_sum_new", 
            "set_partition_sum_and_cardinality_new",
            "user_defined"
        ],
        default=None)

    command_parser.add_argument("--comparison", help="Set the usage of comparison \
        predicates: less than (<) with lt, less equal (<=) with leq, \
        greater than (>) with gt, greater equal (>=) with geq \
        equal (==) with eq and different (!=) with neq.\
        Example: --comparison lt gt eq diff", nargs='+', \
        required=False, choices=["lt","leq","gt","geq","eq","neq"])
    command_parser.add_argument("--arithm", help="Enables the usage of arithmetic \
        predicates: add (+), sub(-), mul(*), div(/), and abs (||). Example: \
        --arithm add sub mul div abs", nargs='+', required=False, choices=["add","sub",
        "mul","div","abs"])
    command_parser.add_argument("--cr", help="Enables the generation of \
        choice rules.", default=False, action="store_true")
    command_parser.add_argument("--invention", help="Enables predicate invention with \
        n predicates. Example --invention=1", type=int, default=0)
    command_parser.add_argument('--aggregates', help="Enable aggregates. Example:\
        --aggregates sum(a/1) count (a/1). Specify the atom to aggregate.", 
        nargs='+', required=False)
    
    command_parser.add_argument("--profile", help="Enables profiling.", 
        default=False, action="store_true")
    
    command_parser.add_argument("--version", help="Prints the software version and exits.", 
        default=False, action="store_true")
    
    args = command_parser.parse_args()
    
    if args.profile:
        import cProfile, pstats, io
        from pstats import SortKey
        pr = cProfile.Profile()
        pr.enable()
        
    if args.version:
        print(f"GENTIANS version: {version}.")
        sys.exit()

    
    # print(args.arithm)
    # print(args.comparison)
    # sys.exit()
    background = []
    positive_examples = []
    negative_examples = []
    language_bias_head = []
    language_bias_body = []
    
    if args.example is None:
        if (os.path.isfile(args.directory + "bk.pl") and
            os.path.isfile(args.directory + "exs.pl") and
            os.path.isfile(args.directory + "bias.pl")):
            background, positive_examples, negative_examples,\
                language_bias_head, language_bias_body = utils.read_popper_format(
                    args.directory)
            # print(background, positive_examples, negative_examples, language_bias_head, language_bias_body)
        else:
            utils.print_error_and_exit("Specify a directory or an example")
    else:
        if args.example == "coin":
            background, positive_examples, negative_examples,\
            language_bias_head, language_bias_body = example_programs.coin_example()
            # print(background, positive_examples, negative_examples, language_bias_head, language_bias_body)
        elif args.example == "even_odd":
            background, positive_examples, negative_examples,\
            language_bias_head, language_bias_body = example_programs.even_odd_example()
        elif args.example == "animals_bird":
            background, positive_examples, negative_examples,\
            language_bias_head, language_bias_body = example_programs.animals_bird_example()
        # elif args.example == "penguin":
        #     background, positive_examples, negative_examples,\
        #     language_bias_head, language_bias_body = example_programs.penguin_example()
        elif args.example == "coloring":
            background, positive_examples, negative_examples,\
            language_bias_head, language_bias_body = example_programs.coloring_example()
        elif args.example == "adjacent_to_red":
            background, positive_examples, negative_examples,\
            language_bias_head, language_bias_body = example_programs.adjacent_to_red_example()
        elif args.example == "grandparent":
            background, positive_examples, negative_examples,\
            language_bias_head, language_bias_body = example_programs.grandparent_example()
        elif args.example == "sudoku":
            background, positive_examples, negative_examples,\
            language_bias_head, language_bias_body = example_programs.sudoku()
        # elif args.example == "dummy":
        #     background, positive_examples, negative_examples,\
        #     language_bias_head, language_bias_body = example_programs.dummy()
        elif args.example == "subset_sum":
            background, positive_examples, negative_examples,\
            language_bias_head, language_bias_body = example_programs.subset_sum()
        elif args.example == "subset_sum_double":
            background, positive_examples, negative_examples,\
            language_bias_head, language_bias_body = example_programs.subset_sum_double()
        elif args.example == "subset_sum_double_and_sum":
            background, positive_examples, negative_examples,\
            language_bias_head, language_bias_body = example_programs.subset_sum_double_and_sum()
        elif args.example == "subset_sum_double_and_prod":
            background, positive_examples, negative_examples,\
            language_bias_head, language_bias_body = example_programs.subset_sum_double_and_prod()
        elif args.example == "subset_sum_triple":
            background, positive_examples, negative_examples,\
            language_bias_head, language_bias_body = example_programs.subset_sum_triple()
        elif args.example == "4queens":
            background, positive_examples, negative_examples,\
            language_bias_head, language_bias_body = example_programs.n_4queens()
        elif args.example == "5queens":
            background, positive_examples, negative_examples,\
            language_bias_head, language_bias_body = example_programs.n_5queens()
        elif args.example == "clique":
            background, positive_examples, negative_examples,\
            language_bias_head, language_bias_body = example_programs.clique()
        elif args.example == "hamming_0":
            background, positive_examples, negative_examples,\
            language_bias_head, language_bias_body = example_programs.hamming(0, False)
        elif args.example == "hamming_1":
            background, positive_examples, negative_examples,\
            language_bias_head, language_bias_body = example_programs.hamming(1, False)
        # elif args.example == "harder_hamming_0":
        #     background, positive_examples, negative_examples,\
        #     language_bias_head, language_bias_body = example_programs.hamming(0, True)
        # elif args.example == "harder_hamming_1":
        #     background, positive_examples, negative_examples,\
        #     language_bias_head, language_bias_body = example_programs.hamming(1, True)
        # elif args.example == "partition":
        #     background, positive_examples, negative_examples,\
        #     language_bias_head, language_bias_body = example_programs.partition()
        elif args.example == "magic_square_no_diag":
            background, positive_examples, negative_examples,\
            language_bias_head, language_bias_body = example_programs.magic_square_no_diag()
        elif args.example == "latin_square":
            background, positive_examples, negative_examples,\
            language_bias_head, language_bias_body = example_programs.latin_square()
        elif args.example == "set_partition_sum":
            background, positive_examples, negative_examples,\
            language_bias_head, language_bias_body = example_programs.set_partition_sum()
        elif args.example == "set_partition_sum_and_cardinality":
            background, positive_examples, negative_examples,\
            language_bias_head, language_bias_body = example_programs.set_partition_sum_and_cardinality()
        elif args.example == "set_partition_sum_new":
            background, positive_examples, negative_examples,\
            language_bias_head, language_bias_body = example_programs.set_partition_new(False)
        elif args.example == "set_partition_sum_and_cardinality_new":
            background, positive_examples, negative_examples,\
            language_bias_head, language_bias_body = example_programs.set_partition_new(True)
        elif args.example == "set_partition_sum_cardinality_and_square":
            background, positive_examples, negative_examples,\
            language_bias_head, language_bias_body = example_programs.set_partition_sum_cardinality_and_square()
        elif args.example == "user_defined":
            background, positive_examples, negative_examples,\
            language_bias_head, language_bias_body = example_programs.user_defined()
        else:
            utils.print_error_and_exit("Example not found")

    
    s = Solver(
        background, 
        positive_examples, 
        negative_examples, 
        language_bias_head, 
        language_bias_body,
        args
    )

    s.solve()
    
    if args.profile:
        pr.disable()
        s = io.StringIO()
        sortby = SortKey.CUMULATIVE # sort by total time
        # sortby = SortKey.CALLS # sort by number of calls
        ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
        ps.print_stats()
        print(s.getvalue())
