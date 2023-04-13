import math
import sys
import itertools
import random
import copy
import time

import strategies

from clingo_interface import ClingoInterface
from clingo_interface import Coverage

from program_sampler import ProgramSampler

import example_programs

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


class Clause:
    def __init__(self,
        head : 'list[str]',
        body : 'list[str]'
        ) -> None:
        self.head : 'list[str]' = head
        self.body : 'list[str]' = body
        self.length : int = len(self.head) + len(self.body)

    def get_clause(self) -> str:
        cl : str = ''
        for h in self.head:
            cl += h + ';'
        cl = cl[:-1] + ' :- '
        
        for b in self.body:
            cl += b + ', '
        cl = cl[:-2] + '.'
        return cl
    
    def __str__(self) -> str:
        return self.get_clause()
    
    def __repr__(self) -> str:
        return self.__str__()
    

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
        positive_examples : 'list[str]',
        negative_examples : 'list[str]',
        language_bias_head : 'list[str]',
        language_bias_body : 'list[str]',
        verbose : int = 1
        ) -> None:
        self.background : 'list[str]' = background
        self.positive_examples : 'list[str]' = positive_examples
        self.negative_examples : 'list[str]' = negative_examples
        self.language_bias_head : 'list[str]' = language_bias_head
        self.language_bias_body : 'list[str]' = language_bias_body
        self.verbose : int = verbose

    
    def sample_program(self) -> Program:
        return Program([], 0, 0)
    
    
    def identify_set_clauses(self, program : 'list[str]', fixed : bool = True) -> 'dict[str,Coverage]':
        '''
        Set up the solver and call the method.
        If fixed is true then use all the specified clauses. If false,
        let the ASP solver to compute the set of clauses (with choice
        rules). fixed is True for the loop with an increasing number of
        clauses.
        '''
        # use projective solutions on the selected rules and atoms
        asp_solver = ClingoInterface(self.background, ['-Wnone', '0', '--project'])
        # print(program)
        # sys.exit()
        return asp_solver.extract_coverage_and_set_clauses(program, self.positive_examples, self.negative_examples, fixed=fixed)
    
    
    def test_coverage(self, program : 'list[str]') -> 'tuple[int,int]':
        '''
        Tests the coverage represented as the number of positive
        and negative examples covered.
        '''
        pos_covered : int = 0
        neg_covered : int = 0
        asp_solver = ClingoInterface(program + self.background)
        
        return asp_solver.test_coverage_example(self.positive_examples, self.negative_examples)

        for el in self.positive_examples:
            pos_covered += int(asp_solver.test_coverage_example(el.split('.')[0:-1], True))
        for el in self.negative_examples:
            asp_solver = ClingoInterface(program + self.background)
            neg_covered += int(asp_solver.test_coverage_example(el.split('.')[0:-1], False))
            
        return pos_covered, neg_covered


    def solve(self) -> None:
        '''
        Main loop
        '''
        # maximum number of clauses in a program
        max_clauses = 2
        max_variables = 3
        max_depth = 4
 
        # sampling loops and test
        sample_loops : int = 10
        
        best_found : bool = False

        sampler = ProgramSampler(
            self.language_bias_head,
            self.language_bias_body,
            max_depth = max_depth,
            max_variables = max_variables,
            max_clauses = max_clauses,
            verbose = self.verbose,
            enable_find_max_vars_stub=False,
            find_all_possible_pos_for_vars_one_shot=True
        )
        

        start_total_time = time.time()
        for it in range(sample_loops):
            # Step 0: sample a list of clauses
            print(f"Sampling loop: {it}")
            start_time = time.time()
            print("Sampling clauses")
            cls = sampler.sample_clause_stub(1000)
            sample_time = time.time() - start_time
            print(f"Sampled clauses in {sample_time} seconds")
        
            # Step 1: remove duplicates: TODO?: sample clauses not duplicated
            sampled_clauses = sorted(list(set(cls)))
            # print(sampled_clauses)
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
            # QUI
            # for p in placed_list:
            #     print(p)
            # sys.exit()
            print(f"Total clauses: {len(placed_list)}")
            # print(len(sampled_clauses))
            
            # Step 3: genetic algorithm
            start_time = time.time()
            current_strategy = strategies.Strategy(placed_list, self.background, positive_examples, negative_examples)
            n_clauses_genetic = 6
            pop_size_genetic = 50
            iterations_genetic = 10000
            mutation_probability = 0.2
            prg, score, best_found = current_strategy.genetic_solver(n_clauses_genetic, pop_size_genetic, mutation_probability, iterations_genetic)
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
    if len(sys.argv) > 1:
        folder = sys.argv[1]
    else:
        # even - odd
        # OK
        # background, positive_examples, negative_examples, language_bias_head, language_bias_body = example_programs.even_odd_example()
        
        # coin
        # OK
        # background, positive_examples, negative_examples, language_bias_head, language_bias_body = example_programs.coin_example()
        
        # animals bird
        # OK
        # background, positive_examples, negative_examples, language_bias_head, language_bias_body = example_programs.animals_bird_example()

        # grandparent
        # background, positive_examples, negative_examples, language_bias_head, language_bias_body = example_programs.grandparent_example()

        # adjacient to red
        # background, positive_examples, negative_examples, language_bias_head, language_bias_body = example_programs.adjacent_to_red_example()
        
        # coloring
        background, positive_examples, negative_examples, language_bias_head, language_bias_body = example_programs.coloring_example()
        
        # QUESTO
        # non risolubile perché non imparo regole ground
        # background, positive_examples, negative_examples, language_bias_head, language_bias_body = example_programs.penguin_example()

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
        verbose = 2
    )

    s.solve()
