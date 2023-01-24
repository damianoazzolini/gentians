import math
import sys
import itertools

from clingo_interface import ClingoInterface

from program_sampler import ProgramSampler

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
        self.clauses = clauses
        self.covered_positive : float = covered_positive
        self.covered_negative : float = covered_negative

    def get_program_str(self) -> str:
        s = ''
        for c in self.clauses:
            # s += c.get_clause() + '\n' 
            s += c + '\n' 
        return s

    def get_program_list(self) -> 'list[str]':
        s : 'list[str]' = []
        for c in self.clauses:
            # s.append(c.get_clause()) 
            s.append(c) 
        return s

    def __str__(self) -> str:
        return self.get_program_str() + f"Covered -> positive: {self.covered_positive} - negative: {self.covered_negative}\n"
    
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
        learned_program : 'Program' = Program([], -1, -1)
        sampler = ProgramSampler(
            self.language_bias_head,
            self.language_bias_body,
            max_depth = 2,
            max_variables = 2,
            max_clauses = 3,
            verbose = self.verbose
        )
        
        best_found : bool = False
        sampled_programs : 'list[Program]' = []

                
        # Main loop: iteratively 
        # sample a program from the PCFG
        # check the coverage of the program
        
        step = 100
 
        while not best_found and step > 0:
            sampled_clauses = sampler.sample_program_stub()
            
            if self.verbose > 1:
                print(f'sampled {len(sampled_clauses)} clauses')
                print(*sampled_clauses, sep='\n')
                print('---')
            
            # IMPROVE: generation of all the possible replacements
            # in the lists and then combine these
            # print(sampled_clauses)
            # sampled_clauses = [":-  coin(_____), tails(_____)."]
            placed_list : 'list[list[str]]' = []
            for clause in sampled_clauses:
                r = sampler.place_variables_clause(clause)
                if len(r) > 0 and not (r in placed_list):
                    placed_list.append(r)
                
            # TODO NEXT: ora la condifica ASP funziona solo con 1 regola
            # estenderla a più regole
            # r = sampler.place_variables_clause(sampled_clauses)
            # print(placed_list)
            possible_programs = itertools.product(*placed_list)
            
            # for el in possible_programs:
            #     print(list(el))
            
            
            # Generate the possible combinations of the lists
            
            
            # sys.exit()
            # print(r)

            
            # penguin(V1):-  not can(V0,V1), ability(V0), bird(V1).
            # s = "penguin(V0):-  can(V0,fly), ability(fly), bird(V0)."
            # covered_positive, covered_negative = self.test_coverage([s])
            # print(covered_positive, covered_negative)
            
            # sys.exit()
            # sampled_program = self.sample_program()
            for program in possible_programs:
                # print(list(program))
                # program = ["heads(V1) :- coin(V1), not tails(V1).", "tails(V1) :- coin(V1), not heads(V1)."]
                covered_positive, covered_negative = self.test_coverage(list(program))
                #     # an error occurred
                #     break
                # else:
                if covered_positive != -1:
                    sampled_programs.append(Program(list(program), covered_positive, covered_negative))
                    # print(covered_positive, covered_negative)
                    if covered_positive == len(self.positive_examples) and covered_negative == 0:
                        best_found = True
                        learned_program = Program(list(program), covered_positive, covered_negative)
                        print("Best found")
                        # TODO: simplify the program

            step -= 1

        print("-- sampled --")
        print(sampled_programs)
        if best_found:
            print('--- BEST ---')
            print(learned_program)
        else:
            print('No program found')


if __name__ == "__main__":
    
    # bird example 
    # background : 'list[str]' = [
    #     'bird(alice).', 
    #     'bird(betty).', 
    #     'can(alice,fly).', 
    #     'can(betty,swim).', 
    #     'ability(fly).', 
    #     'ability(swim).'
    # ]
    # positive_examples : 'list[str]' = ["penguin(betty)"]

    # negative_examples : 'list[str]' = ["penguin(alice)"]

    # language_bias_head : 'list[str]' = ['modeh(1, penguin(+))']
    # # language_bias_body : 'list[str]' = ['modeb(1, bird(+))', 'modeb(1, ability(+))', 'modeb(*, not can(+,#))']
    # language_bias_body : 'list[str]' = ['modeb(1, bird(+))', 'modeb(1, ability(+))', 'modeb(*, not can(+,#))']

    # coin example
    # from https://doc.ilasp.com/specification/cdpis.html
    background : 'list[str]' = [
        'coin(c1).', 
        'coin(c2).', 
        'coin(c3).'
    ]

    positive_examples : 'list[str]' = [
        "heads(c1) tails(c2) heads(c3)",
        "tails(c1) heads(c2) tails(c3)",
        "heads(c1) heads(c2) tails(c3)",
        "tails(c1) tails(c2) heads(c3)"
    ]

    negative_examples : 'list[str]' = []

    language_bias_head : 'list[str]' = [
        'modeh(1, heads(+))',
        'modeh(1, tails(+))'
    ]
    # language_bias_body : 'list[str]' = ['modeb(1, bird(+))', 'modeb(1, ability(+))', 'modeb(*, not can(+,#))']
    language_bias_body : 'list[str]' = [
        'modeb(1, heads(+))', 
        'modeb(1, not heads(+))', 
        'modeb(1, tails(+))',
        'modeb(1, not tails(+))',
        'modeb(1, coin(+))'
    ]

    s = Solver(
        background, 
        positive_examples, 
        negative_examples, 
        language_bias_head, 
        language_bias_body,
        verbose = 2
    )

    s.solve()
    # c1 = Clause(["penguin(X)"],["bird(X)","not can(X,fly)"])
    # # c1 = Clause(["penguin(X)"],["bird(X)"])
    # p = Program([c1], 0, 0)
    # a,b = s.test_coverage(p)
    
    # print(p)
    # print(f"Pos covered: {a} - Neg covered: {b}")
    