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

import example_programs

program_description = "GENTIANS: GENeTic algoritm for inductive learning of ANswer Set programs."

# class Literal:
#     def __init__(self, string_representation : str) -> None:
#         def parse_literal(string_representation : str) -> 'tuple[str,int,bool]':
#             # supposing no nested literals, no a(b(x)) but a(x)
#             negated = False
#             if string_representation.startswith('not '):
#                 negated = True
#             if negated:
#                 name = string_representation[4:].split('(')[0]
#             else:
#                 name = string_representation.split('(')[0]
#             if '(' in string_representation and not(',' in string_representation):
#                 arity = 1
#             else:
#                 arity = string_representation.count(',') + 1
            
#             return name, arity, negated
        
#         self.name, self.arity, self.negated = parse_literal(string_representation)
        
#     def __str__(self) -> str:
#         return f"Name: {self.name}, arity: {self.arity}, negated: {self.negated}"
    
#     def __repr__(self) -> str:
#         return self.__str__()


# def compute_n_vars(clause : str):
#     i = 0
#     found = True
#     while found:
#         if f'V{i}' not in clause:
#             found = False
#         i +=1
    
#     return i - 1
    
# class PlacedClause:
#     def __init__(self,
#         placed_clauses : 'list[str]'
#         ) -> None:
#         self.placed_clauses = placed_clauses
#         self.n_vars_clauses : 'list[int]' = []
#         self.n_atoms = 0
        
#         for cl in self.placed_clauses:
#             self.n_vars_clauses.append(compute_n_vars(cl))

#         cl = placed_clauses[0]
#         cl = cl.split(':-')
#         head = cl[0]
#         body = cl[1]
        
#         if len(head) != 0:
#             self.n_atoms = len(head.split(';')) + 1
#         self.n_atoms = len(body.split('),')) + 1
        

    # def get_clause(self) -> str:
    #     cl : str = ''
    #     for h in self.head:
    #         cl += h + ';'
    #     cl = cl[:-1] + ' :- '
        
    #     for b in self.body:
    #         cl += b + ', '
    #     cl = cl[:-2] + '.'
    #     return cl
    
    # def __str__(self) -> str:
    #     s = ""
    #     for cl in self.placed_clauses:
    #         s += cl + '\n'
    #     s += f"n_vars: {self.n_vars_clauses}\nn_atoms: {self.n_atoms}\n"
    #     return s
    
    # def __repr__(self) -> str:
    #     return self.__str__()
    

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
        self.sample_loops : int = arguments.iterations
        self.n_clauses_genetic : int = arguments.clauses
        self.pop_size_genetic : int = arguments.pop_size
        self.mutation_probability : float = arguments.mutation_probability
        self.iterations_genetic : int = arguments.iterations_genetic
        
        self.aggregates : 'list[str]' = arguments.aggregates
        self.comparison : 'list[str]' = arguments.comparison
        self.arithm : 'list[str]' = arguments.arithm
        self.cr : bool = arguments.cr # for choice rules
        self.invention : bool = arguments.invention # predicate invention
    

    def solve(self) -> None:
        '''
        Main loop
        '''
        # maximum number of clauses in a program
        # max_variables = 3
        # max_depth = 4
 
        # sampling loops and test
        # sample_loops : int = 10
        
        best_found : bool = False

        sampler = ProgramSampler(
            self.language_bias_head,
            self.language_bias_body,
            max_depth = self.max_depth,
            max_variables = self.max_variables,
            # max_clauses = max_clauses,
            verbose = self.verbose,
            enable_find_max_vars_stub=False,
            find_all_possible_pos_for_vars_one_shot=True,
            allowed_aggregates=self.aggregates,
            arithmetic_operators=self.arithm,
            comparison_operators=self.comparison
        )
        
        start_total_time = time.time()
        for it in range(self.sample_loops):
            # Step 0: sample a list of clauses
            print(f"Sampling loop: {it}")
            start_time = time.time()
            print("Sampling clauses")
            cls = sampler.sample_clause_stub(1000)
            sample_time = time.time() - start_time
        
            # Step 1: remove duplicates: TODO?: sample clauses not duplicated
            sampled_clauses = sorted(list(set(cls)))
            print(f"Sampled {len(sampled_clauses)} different clauses in {sample_time} seconds")
            print(sampled_clauses)
            # sys.exit()
            if self.verbose >= 1:
                print(f"Total number of clauses sampled: {len(sampled_clauses)}")
                if self.verbose >= 2:
                    print("Sampled clauses:")
                    for current_cl in sampled_clauses:
                        print(current_cl)

            # Step 2: place the variables
            # TODO: this is a bottleneck: generation of all the 
            # possible locations, which are #n_vars^#n_pos in the 
            # worst case
            # TODO: store these values for the iterations
            start_time = time.time()
            placed_list : 'list[list[str]]' = sampler.place_variables_list_of_clauses(sampled_clauses)
            placing_time = time.time() - start_time
            print(f"Placed variables in {placing_time} seconds")
            # # QUI
            placed_list_improved : 'list[strategies.PlacedClause]' = []
            for p in placed_list:
                # print(p)
                pl = strategies.PlacedClause(p)
                placed_list_improved.append(pl)
                # print(pl)
                # print("TODO: -- usare individual in strategies? -- placed clauses contiene anche il numero di variabili e di atomi, per considerare meglio il valore di una clausola")
            # sys.exit()
            print(f"Total clauses: {len(placed_list)}")
            # print(len(sampled_clauses))
            
            # Step 3: genetic algorithm
            start_time = time.time()
            current_strategy = strategies.Strategy(placed_list_improved, self.background, positive_examples, negative_examples)
            # n_clauses_genetic = 6
            # pop_size_genetic = 50
            # iterations_genetic = 10000
            # mutation_probability = 0.2
            prg, score, best_found = current_strategy.genetic_solver(
                self.n_clauses_genetic, 
                self.pop_size_genetic, 
                self.mutation_probability,
                self.iterations_genetic)
            genetic_time = time.time() - start_time
            
            print(f"Iteration {it} - Time {genetic_time}")
            print(f"Program: {prg}")
            if best_found:
                print("Best found")
                break
            else:
                print(f"Score: {score}")
        
        print(f"Total time: {time.time() - start_total_time}")


if __name__ == "__main__":
    command_parser = argparse.ArgumentParser(description=program_description)
    command_parser.add_argument("-dir", "--directory", help="Directory storing the \
        bk.pl, exs.pl, and bias.pl files (Popper format).", type=str, default=".")
    command_parser.add_argument("-v", "--verbose", help="Verbose mode", type=int, \
        choices=range(0,3), default=0)
    command_parser.add_argument("-c", "--clauses", help="Max clauses to consider in a \
        program", type=int, default=6)
    command_parser.add_argument("-vars", "--variables", help="Max variables to consider \
        in a rule", type=int, default=3)
    command_parser.add_argument("-d", "--depth", help="Max literals in rules", \
        type=int, default=3)
    command_parser.add_argument("-it", "--iterations", help="Max number of sample and \
        genetic iterations", type=int, default=10)
    command_parser.add_argument("-s", "--sample", help="Number of clauses to sample",\
        type=int, default=1000)
    command_parser.add_argument("-p", "--pop-size", help="Size of the population",\
        type=int, default=50)
    command_parser.add_argument("-itg", "--iterations-genetic", help="Number of \
        iterations for the genetic algorithm", type=int, default=10000)
    command_parser.add_argument("-mp", "--mutation-probability", help="Mutation \
        probability", type=float, default=0.2)
    command_parser.add_argument("-e", "--example", help="Load a predefined example", \
        choices=["coin", "even_odd", "animals_bird", "coloring", \
            "adjacent_to_red", "grandparent", "sudoku", "dummy"], default=None)
    
    command_parser.add_argument("--comparison", help="Set the usage of comparison \
        predicates: less than (<) with lt, greater than (>) with gt, and \
        equal (==) with eq. Example: --comparison lt gt eq diff", nargs='+', \
        required=False, choices=["lt","gt","eq", "neq"])
    command_parser.add_argument("--arithm", help="Enables the usage of arithmetic \
        predicates: add (+), sub(-), mul(*), and div(/). Example: \
        --arithm add sub mul div", nargs='+', required=False, choices=["add","sub",
        "mul","div"])
    command_parser.add_argument("--cr", help="Enables the generation of \
        choice rules.", type=bool, default=False)
    command_parser.add_argument("--invention", help="Enables predicate invention with \
        n predicates. Example --invention=1", type=int, default=0)
    command_parser.add_argument('--aggregates', help="Enable aggregates. Example:\
        --aggregates sum(a/1) count (a/1). Specify the atom to aggregate.", 
        nargs='+', required=False)
    
    args = command_parser.parse_args()
    
    print(args.arithm)
    print(args.comparison)
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
        elif args.example == "dummy":
            background, positive_examples, negative_examples,\
            language_bias_head, language_bias_body = example_programs.dummy()
        else:
            utils.print_error_and_exit("Example not found")

        # folder = "examples/abduce/" # troppo grande
        # folder = "examples/andersen/"
        # folder = "examples/animals_bird/"
        # folder = "examples/buildwall/"
        # folder = "examples/cliquer-leg/"
        # folder = "examples/krk/"
        
        # folder = "../Popper/examples/path/"
        # folder = "../Popper/examples/kinship-ancestor/"
        # folder = "examples/path/" # OK
        # folder = "examples/small/" # ancora troppo complesso
        # folder = "examples/1-type-pointsto/" # TODO: qui mostra il bottleneck nel piazzare le clausole, questo si blocca nel campionamento delle clausole
        # background, positive_examples, negative_examples, language_bias_head, language_bias_body = utils.read_popper_format(folder)

    # print(background, positive_examples, negative_examples, language_bias_head, language_bias_body)
    
    # sys.exit()
    
    s = Solver(
        background, 
        positive_examples, 
        negative_examples, 
        language_bias_head, 
        language_bias_body,
        args
    )

    s.solve()
