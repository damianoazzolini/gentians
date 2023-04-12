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
        # minimum number of clauses in a program
        min_clauses = 1
        # maximum number of clauses in a program
        max_clauses = 2
        
        max_variables = 3 # TODO: make this adaptive
        max_depth = 4 # TODO: make this adaptive
        # a list since there can be multiple optimal programs
        learned_programs : 'list[Program]' = [] # Program([], 0, 0)
        # maximum number of programs to test in an iteration
        # generated from the itertool product method
        max_n_programs_for_iteration : int = 500
        
        debug_mode : bool = False
        # if true, if found a clause with 100% coverage of the positive,
        # add only constraints
        # dig_adding_costraints : bool = True
        
        # sampling loops and test
        sample_loops : int = 10

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
        
        best_found : bool = False
        sampled_programs : 'list[Program]' = []
        
        total_programs_tested : int = 0
    
        clauses_list : 'list[Program]' = []
        # index_clauses_list : 'list[int]' = []
        
        # sample a list of clauses
        for it in range(sample_loops):
            print(f"Sampling loop: {it}")
            start_time = time.time()
            print("Sampling clauses")
            cls = sampler.sample_clause_stub(500)
            sample_time = time.time() - start_time
            print(f"Sampled clauses in {sample_time} seconds")
            
            # remove duplicates: TODO: sample clauses not duplicated
            sampled_clauses = sorted(list(set(cls)))
            if self.verbose >= 1:
                print(f"Total number of clauses sampled: {len(sampled_clauses)}")
                if self.verbose >= 2:
                    print("Sampled clauses:")
                    for current_cl in sampled_clauses:
                        print(current_cl)
            
            # # count the constraints since there can't be only constraints
            # # in a program (and no generators)
            # # Not needed in genetic
            # last_constraint_index : int = 0
            # while last_constraint_index <= len(sampled_clauses):
            #     # constraint
            #     if sampled_clauses[last_constraint_index][0] == ':':
            #         last_constraint_index += 1
            #     else:
            #         # since the clauses are ordered
            #         break
            # # -2 since starts from 0 and there is an extra number due to 
            # # the loop
            # last_constraint_index = last_constraint_index - 1
            # print(f"Last constraint index: {last_constraint_index}")
            # # up to position counter_constraints there are only constraints 
            # # print(counter_constraints)
            # # sys.exit()

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
            print(f"Total clauses: {len(placed_list)}")
            # print(len(sampled_clauses))
            
            current_strategy = strategies.Strategy(placed_list, self.background, positive_examples, negative_examples)
            n_clauses_genetic = 6
            pop_size_genetic = 50
            iterations_genetic = 10000
            mutation_probability = 0.2
            prg, score, best_found = current_strategy.genetic_solver(n_clauses_genetic, pop_size_genetic, mutation_probability, iterations_genetic)
            
            print(f"Iteration {it}")
            print(f"Program: {prg}")
            if best_found:
                print("Best found")
                break
            else:
                print(f"Score: {score}")
        
        sys.exit()
            # cover_only_negative : 'list[str]' = []
            
        
        
        start_time = time.time()
        current_number_of_clauses = min_clauses
        while (current_number_of_clauses < max_clauses + 1) and not best_found:
            # maximum number of combination of indexes to select
            total_combinations = math.comb(len(placed_list), current_number_of_clauses)
            combinations_only_constraints = math.comb(last_constraint_index + 1, current_number_of_clauses)
            # TODO: potrei voler imparare solo vincoli, quindi questo non è sempre generale
            max_combinations = total_combinations - combinations_only_constraints
            print(f"Considering {current_number_of_clauses} clause{'s' if current_number_of_clauses > 1 else ''}")
            if self.verbose >= 1:
                print(f"Total combinations: {total_combinations}")
                print(f"Combinations with only constraints: {combinations_only_constraints}")
                print(f"Maximum number of possible combinations: {max_combinations}")
            # sys.exit()
            # list containing the indexes of the clauses composing the analyzed programs
            selected_indexes_clauses : 'list[list[int]]' = []
            
            # list containing the programs has not been fully analyzed
            # due to max_n_programs_for_iteration (i.e., max_n_programs_for_iteration
            # is greater than the possible programs that has been generated)
            not_fully_explored : 'list[list[int]]' = []
        
            trials = 1000
            if trials < max_combinations:
                # TODO: questo è un problema: senza la scelta delle clausole in ASP
                # (cioè choice rule sulle clausole)
                # rischio di lasciare fuori molte possibili combinazioni.
                # Dall'altro, la scelta delle clausole con choice rule
                # potrebbe diventare assai pesa. Devo fare dei test.
                # Posso mettere la scelta delle choice a True (quindi
                # fixed = False in identify_set_clauses) se non vale ciò?
                print("Number of trials less than the total combinations")
                print("Some solutions can be missed")
            
            while not best_found and trials > 0:
                if len(selected_indexes_clauses) == max_combinations:
                    print(f"Tested all the possible {max_combinations} combinations. Solution not found.")
                    break
                
                # select a random set of clauses of size max_clauses
                # The if is needed in the case there less possible clauses than
                # the specified
                currently_selected_indexes : 'list[int]' = sorted(random.sample(range(len(placed_list)), current_number_of_clauses if len(placed_list) > current_number_of_clauses else len(placed_list)))
                # Loop to avoid sampling the same programs
                only_constraints = all((index <= last_constraint_index) for index in currently_selected_indexes)
                # print(currently_selected_indexes)
                # print(only_constraints)
                # TODO: qui posso migliorare: se la coverage di n regole è < 100% (calcolata
                # da iterazione precedente) allora non ha senso inserire un vincolo.
                while (currently_selected_indexes in selected_indexes_clauses) or only_constraints:
                    currently_selected_indexes = sorted(
                        random.sample(
                            range(len(placed_list)), 
                            current_number_of_clauses if len(placed_list) > current_number_of_clauses else len(placed_list)
                            )
                        )
                    only_constraints = all((index <= last_constraint_index) for index in currently_selected_indexes)
                    # print(currently_selected_indexes)
                    # print(only_constraints)

                
                selected_indexes_clauses.append(sorted(currently_selected_indexes))
                if self.verbose >= 2:
                    print(f"Currently selected indexes: {currently_selected_indexes}")
                # TODO: se ho la modalità ottimizzazione numero di clausole e
                # come lista di clausole scelgo, per esempio, [1,2,3] e l'iterazione
                # successiva [1,2,4] testerò comunque anche i programmi con solo 1,
                # solo 2 ed entrambi. Quindi ne testo 2**3 + 2**3 in totale però
                # tra questi 4 sono in comune, quindi mi basterebbe testarne 16 - 4
                # = 12. Posso salvare gl indici testati in una lista e poi eliminare
                # i programmi. Avrò una lista di vincoli espliciti in ASP che tolgono
                # le combinazioni. Va più forte?

                currently_selected_clauses : 'list[list[str]]' = [placed_list[i] for i in currently_selected_indexes]
                # print(currently_selected_clauses)
                tot_programs = 1
                for el in currently_selected_clauses:
                    tot_programs = tot_programs * len(el)
                if self.verbose >= 2:
                    print(f"Total number of programs current selection: {tot_programs}")

                
                # sys.exit()
                # possible_programs = itertools.product(*placed_list)
                # TODO: product è deterministico? Sembra di sì. Se così sarebbe ottimo
                # salvare l'iteratore per l'insieme di clausole che non sono ancora
                # state analizzate completamente (nella lista not_fully_explored) e poi
                # partire da dove si è arrivati per completare il test

                # print(currently_selected_clauses)
                # cut the possible programs to test to max_n_programs_for_iteration to better search the space
                # Moreover, randomize the list to again improve the search
                # TODO: se taglio la dimensione della lista allora non 
                # posso imporre di non campionare più le stesse regole,
                # altrimenti il programma è incompleto (la soluzione potrebbe
                # essere nella lista ma non considerata)
                # If the number of combinations
                # is greater than the number of the total possible number
                # test them exaustively. Otherwise, sample them.
                possible_programs : 'list[list[str]]' = []
                if tot_programs <= max_n_programs_for_iteration:
                    possible_programs = itertools.product(*currently_selected_clauses) # type: ignore
                    possible_programs = list(possible_programs)
                    if len(possible_programs) == 0 and debug_mode:
                        print("Found empty possible programs, maybe due to an empty sublist")
                        print(currently_selected_clauses)
                        sys.exit()
                else:
                    # a number too big to handle: create a copy of the
                    # selected clauses, shuffle them, create the iterator and
                    # then extracts at most max_n_programs_for_iteration programs
                    cl1 = copy.deepcopy(currently_selected_clauses)
                    for sublist in cl1:
                        random.shuffle(sublist)
                    p = itertools.product(*cl1)
                    while p and (len(possible_programs) < max_n_programs_for_iteration):
                        possible_programs.append(list(next(p)))
                    not_fully_explored.append(currently_selected_indexes)

                for program in possible_programs:
                    # this since only clauses with programs having only negative coverage
                    # cannot contribute
                    # comb_only_negative_coverage = all((cl in cover_only_negative) for cl in program)
                    # # comb_only_negative_coverage = False
                    # if comb_only_negative_coverage:
                    #     print("SOLO NEG")
                    #     print(program)
                    #     print(cover_only_negative)
                    #     sys.exit()
                    if not best_found:
                        if len(program) > 0:
                            # print('-------------------')
                            # print("FISSATO")
                            # program = [":- even(V0), odd(V0).", "odd(V1):- even(V0), prev(V1,V0).", "even(V1):-  prev(V1,V0), odd(V0)."]
                            
                            # program = ["odd(V0):- even(V1), prev(V0,V1).", "even(V0):- odd(V1), prev(V0,V1)."]
                            # print(f"Program {list(program)}")

                            list_program = list(program)

                            # for pp in list_program:
                            #     print(pp)
                            l_results = self.identify_set_clauses(list_program, True)
                            for res in l_results:
                                if res != "Error":
                                    # set to remove duplicates
                                    cp : int = len(list(set(l_results[res].l_pos)))
                                    cn : int = len(list(set(l_results[res].l_neg)))
                                    l_index : 'list[int]' = [int(v) for v in list(res)]
                                    # questo miglioramento sembra non funzionare
                                    # Obiettivo: sottoinsiemi di clausole che coprono
                                    # solo esempi negativi non possono coprire gli esempi
                                    # se combinati. Non sono sicuro.
                                    # if cp == 0 and cn > 0:
                                    #     print("This program covers only negative examples")
                                    #     print(Program([list_program[i] for i in l_index], cp, cn))
                                    #     for i in l_index:
                                    #         if list_program[i] not in cover_only_negative:
                                    #             cover_only_negative.append(list_program[i])
                                    
                                    if len(l_index) == 1:
                                        clauses_list.append(Program([list_program[i] for i in l_index], cp, cn))
                                        # index_clauses_list.append(l_index)
                                    if cp == len(self.positive_examples):
                                        print("Coverage 100% of the positive with")
                                        print(Program([list_program[i] for i in l_index], cp, cn))
                                        # TODO: questo non va sempre bene, vedi il programma even-odd
                                        # if dig_adding_costraints:
                                        #     print("DIG CONSTRAINTS")
                                    #         # remove everything that is not a costraint
                                    #         placed_list = placed_list[:last_constraint_index]
                                    #         # provo a rimuovere tutto ciò che non è un vincolo perché
                                    #         # poi cercherò solo vincoli
                                    #         # print("ARRIVATO QUI: se tolgo il sys si blocca")
                                    #         # sys.exit()

                                    if not(cp == 0 and cn > 0) and not(cp == 0 and cn == 0):
                                        sampled_programs.append(Program([list_program[i] for i in l_index], cp, cn))
                                    if cp == len(self.positive_examples) and cn == 0:
                                        best_found = True
                                        learned_programs.append(Program([list_program[i] for i in l_index], cp, cn))
                                        print("Best found")
                                        print([list_program[i] for i in l_index])
                                        # break

                # TODO: sparare indietro al sampler ciò che è stato già testato
                # così da non ottenere due volte lo stesso insieme di regole 
                # generate. Posso inoltre fare dei ragionamenti su come
                # vincoli o non vincoli influiscono su una maggiore
                # copertura degli esempi?
                trials -= 1

                if self.verbose >= 2:
                    print(f"Total number of tested programs: {len(possible_programs)}")

                total_programs_tested += len(possible_programs)
                
                if len(placed_list) <= current_number_of_clauses:
                    # I've already considered all the possible combinations
                    # of clauses
                    break
            # out of the while loop
            if current_number_of_clauses == 1:
                # print("Programmi testati")
                # clauses_list.sort(key = lambda k : (k.covered_positive/len(positive_examples) - k.covered_negative/len(negative_examples)), reverse=True)
                # print(clauses_list)
                # print(index_clauses_list)
                # print(f"Programmi testati: {len(clauses_list)}")
                # print("Programmi covered negative")
                lcn = [p for p in clauses_list if p.covered_negative > 0]
                # drop the rules with at least one covered negative
                # Does this improve the execution time?
                # print(placed_list)
                
                for pcn in lcn:
                    # TODO: è sempre vero che regole con copertura di
                    # soli esempi negativi non potranno mai coprire
                    # solo esempi positivi, anche aggiungendo dei vincoli?
                    # suppongo pcn con 1 sola regola
                    for placed_clauses in placed_list:
                        if pcn.clauses[0] in placed_clauses:
                            print(f"Remove: {pcn.clauses[0]}")
                            placed_clauses.remove(pcn.clauses[0])

                # remove empty sublists
                placed_list = [x for x in placed_list if x != []]
                            
                    # print(f"Try removing: {pcn.clauses}")
                    # placed_list.remove(pcn.clauses)
                    # print(pcn)
                    # for nv in range(max_variables):
                        # pcn.clauses[0] = pcn.clauses[0].replace(f"V{nv}",'_'*5)
                # print(f'POST: {len(placed_list)}')
                
                # print(lcn)
                # print(placed_list)

            current_number_of_clauses += 1

            print(f"Combinations tested ({len(selected_indexes_clauses)}): {sorted(selected_indexes_clauses)}")
            print(f"Combinations not fully explored ({len(not_fully_explored)}): {sorted(not_fully_explored)}")
            print(f"Tested {total_programs_tested} programs in total")
        
            # print(cover_only_negative)
        ### OUT OF THE LOOP ###
        # print("Sampled programs")
        # print(sampled_programs)
        
        # print("Learned programs")
        # print(learned_program)

        # print("-- sampled --")
        # print(sampled_programs)
        combination_time = time.time() - start_time
        print(f"Sampling clauses took {sample_time} seconds")
        print(f"Placing variables took {placing_time} seconds")
        print(f"Search took {combination_time} seconds")
        if best_found:
            print('--- (OPTIMAL?) FOUND ---')
            # è optimal solo se sono state esplorate tutte le soluzioni
            if len(learned_programs) == 1:
                print("Unique optimal program found")
                print(learned_programs[0])
            else:
                print("Multiple programs found")
                print(learned_programs)
        elif len(sampled_programs) == 0:
            print("No programs found")
        else:
            print('No optimal program found')
            print(f"Total positive: {len(self.positive_examples)}")
            print(f"Total negative: {len(self.negative_examples)}")
            bp = max(sampled_programs, key = lambda k : k.covered_positive)
            print(f'This has the highest number of covered positive ({bp.covered_positive}, {bp.covered_positive/len(self.positive_examples)}%)')
            print(bp)
            bp = min(sampled_programs, key = lambda k : k.covered_negative)
            if len(self.negative_examples) > 0:
                perc = bp.covered_negative/len(self.negative_examples)
            else:
                perc = 0
            print(f'This has the lowest number of covered negative ({bp.covered_negative}, {perc}%)')
            print(bp)



def read_popper_format(folder : str):
    # file: bias.pl, bk.pl, exs.pl
    background : 'list[str]' = []
    positive_examples : 'list[str]' = []
    negative_examples : 'list[str]' = []
    language_bias_head : 'list[str]' = []
    language_bias_body : 'list[str]' = []
    
    # background
    fp = open(folder + "bk.pl")
    lines = fp.readlines()
    fp.close()
    
    for l in lines:
        background.append(l.replace('\n',''))
        
    # language bias
    fp = open(folder + "bias.pl")
    lines = fp.readlines()
    fp.close()
    
    for line in lines:
        if line.startswith('head_pred') or line.startswith('body_pred'):
            t = ""
            if line.startswith('head_pred'):
                line = line.split('head_pred')[1][1:].replace(')','').replace('.','')
                t = "head"
            elif line.startswith('body_pred'):
                line = line.split('body_pred')[1][1:].replace(')','').replace('.','')
                t = "body"

            arity = int(line.split(",")[1])
            name = line.split(",")[0]
            if arity > 0:
                name += '('
                for i in range(0,arity):
                    name += '+,'
                name = name[:-1] + ')'
            
            if t == "head":
                name = "modeh(1," + name + ")."
                language_bias_head.append(name)
            elif t == "body":
                name = "modeb(1," + name + ")."
                language_bias_body.append(name)
                
    # examples
    fp = open(folder + "exs.pl")
    lines = fp.readlines()
    fp.close()    
    
    for line in lines:
        if line.startswith('pos'):
            line = line.split('pos')[1][1:].replace('\n','')[:-2]
            positive_examples.append(line)
        elif line.startswith('neg'):
            line = line.split('neg')[1][1:].replace('\n','')[:-2]
            negative_examples.append(line)
    
    
    return background, positive_examples, negative_examples, language_bias_head, language_bias_body

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
        # troppe opzioni da esplorare
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
        # background, positive_examples, negative_examples, language_bias_head, language_bias_body = read_popper_format(folder)

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
