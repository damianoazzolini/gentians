import random
import sys

import clingo_interface

class Strategy:
    def __init__(self, 
        placed_list : 'list[list[str]]',
        background : 'list[str]',
        positive_examples : 'list[list[str]]',
        negative_examples : 'list[list[str]]',
        ) -> None:
        self.placed_list : 'list[list[str]]' = placed_list
        self.background : 'list[str]' = background
        self.positive_examples : 'list[list[str]]' = positive_examples
        self.negative_examples : 'list[list[str]]' = negative_examples
    
    def genetic_solver(self,
        number_clauses : int, # number of clauses to consider for each program
        population_size : int, # number of programs to keep 
        mutation_probability : float, # mutation probability
        max_interations : int # maximum number of iterations
        ) -> 'tuple[list[str], float, bool]':
        '''
        Genetic algorithm to find the best program
        '''
        class Individual:
            def __init__(self, program : 'list[str]', stub_indexes : 'list[int]', prog_indexes : 'list[int]', score : float) -> None:
                self.program = program
                # stub_indexes is a list of int representing the index of the stub clauses selected
                self.stub_indexes = stub_indexes
                # prog_indexes is a list of int representing the index of the program selected for the stub_indexes clauses - maybe not needed
                self.prog_indexes = prog_indexes
                self.score = score
                
            def __str__(self) -> str:
                return f"Program: {self.program} - score: {self.score}"

            def __repr__(self) -> str:
                return self.__str__()
        
        
        def compute_score_vars_and_rules(program : 'list[str]', best_l_index : 'list[int]', cp : int, cn : int) -> float:
            '''
            Compute the score of a rule by considering the covered positive, covered
            negative, number of variables for the best indexes and the number of clauses
            to be selected. The goal is to select programs with few variables and rules.
            TODO
            '''
            return -1


        def evaluate_score(program : 'list[str]') -> 'tuple[int, int, float, bool, list[int]]':
            # returns covered positive, covered negative, score
            # how to assign a score?
            # Current: cp covered positive, cn covered negative
            # if cp = 0 and cn > 0 -> score = - cn
            # if cp > 0 -> score = cp / (cp + cn)
            # if score = 1 -> optimum found
            # print(self.background)
            # TODO: better define a score. Also consider the number of variables?
            asp_solver = clingo_interface.ClingoInterface(self.background, ['-Wnone', '0', '--project'])
            # program[1] = "odd(V0):- even(V1),prev(V0,V1)."
            # program[0] = "even(V0):- odd(V1),prev(V0,V1)."
            cov = asp_solver.extract_coverage_and_set_clauses(program, self.positive_examples, self.negative_examples, False)

            # print(program)
            best_found = False
            best_cp = 0
            best_cn = 0
            l_index : 'list[int]' = []
            l_best_indexes : 'list[str]' = []
            for res in cov:
                if res != "Error":
                    # set to remove duplicates
                    cp : int = len(list(set(cov[res].l_pos)))
                    cn : int = len(list(set(cov[res].l_neg)))
                    # l_index = [int(v) for v in list(res)]
                    # print(cp, cn, l_index)
                    if cp > best_cp:
                        best_cp = cp
                        best_cn = cn
                        # best_l_index = l_index
                        
                    if cp == len(self.positive_examples):
                        if cn == 0:
                            print(f"Best found with {res}")
                            print(program)
                            l_best_indexes.append(res)
                            best_found = True
                        # else:
                        #     print("Coverage 100% of the positive with")
                        # print([program[i] for i in l_index], cp, cn)
            
            # sys.exit()        
            # if best_found:
            #     break
            # print(cov)
            # print(len(cov))
            # sys.exit()
            # test 1 score
            # if best_cp > 0:
            #     score = best_cp/(best_cp + best_cn)
            # else:
            #     score = -best_cn
            # test 2 score
            # TODO: improve the score
            score = best_cp - best_cn
            
            # shortest one
            l_best_indexes.sort(key = lambda s : len(s))
            l_index = [int(v) for v in list(l_best_indexes[0])] if len(l_best_indexes) > 0 else []
            
            return best_cp, best_cn, score, best_found, l_index 
        
        def initialize_population(
            number_clauses : int, 
            placed_list : 'list[list[str]]',
            population_size : int
            ) -> 'tuple[list[Individual],bool]':
            sampled_individuals : 'list[Individual]' = []
            best_found = False
            
            while len(sampled_individuals) < population_size:
                # pick a program
                stub_indexes : 'list[int]' = sorted(
                    random.sample(
                        range(len(self.placed_list)), number_clauses if len(placed_list) > number_clauses else len(placed_list)
                    )
                )
                
                # for every index, select one of the possible variable placement
                program : 'list[str]' = []
                prog_indexes : 'list[int]' = []
                for i in stub_indexes:
                    el = random.randint(0, len(placed_list[i]) - 1)
                    prog_indexes.append(el)
                    program.append(placed_list[i][el])
                
                program = sorted(program)
                # cp is the current program
                cp, cn, current_score, best_found, l_index = evaluate_score(program)
                if best_found:
                    # TODO: restituire anche la combinazione di elementi
                    return [Individual([program[i] for i in l_index], stub_indexes, prog_indexes, current_score)], best_found
            
                sampled_individuals.append(Individual(program, stub_indexes, prog_indexes, current_score))
            
            return sampled_individuals, best_found

        ###### BODY OF THE METHOD ######
        
        # step 0: initialize the population
        population : 'list[Individual]' = []
        best_found = False
        
        population, best_found = initialize_population(number_clauses, self.placed_list, population_size)
        
        if best_found:
            return population[0].program, population[0].score, True
        
        # step 1: sort in terms of decreasing fittnes
        population.sort(key = lambda x : x.score, reverse=True)
        
        # print("--- POPULATION ---")
        # for p in population:
        #     print(p)
        # print(population)
        # sys.exit()
        
        # step 2: iterate trough programs
        print(f"Running for {max_interations} iterations")
        for it in range(max_interations + 1):
            # print(f"it: {it}")
            if it % 100 == 0:
                print(f"Iteration {it} - best: {population[0]}")
            
            # this since may programs have the same score
            max_score = population[0].score
            i = 1
            j = 1
            for i in range(1, len(population)):
                if population[i].score < max_score:
                    break
            
            if i < 2:
                max_score = population[i].score
                for j in range(i, len(population)):
                    if population[j].score < max_score:
                        break
            else:
                j = i
            # 2.1: pick the two fittest
            pick_uniform = True
            # this is the naive version. However, since many programs have the same score,
            # i should choose a random one among these
            if not pick_uniform: 
                best_a = population[0]
                best_b = population[1]
            else:
                idx_a, idx_b = random.sample(range(0, j), 2)
                # print(f"Combining: {idx_a}, {idx_b}")
                best_a = population[idx_a]
                best_b = population[idx_b]

            # print("Best A")
            # print(best_a)
            # print("Best B")
            # print(best_b)
            
            # print(f"i: {i} j: {j}")
            # print(max_score)
            
            # sys.exit()
            
            # 2.2: crossover
            # TODO: controllare che la nuova regola dopo 2.2 e 2.3 non sia già
            # presente nel programma
            crossover_position = random.randint(0, len(best_a.program) - 1)
            # print(f"Crossover: {crossover_position}")
            new_program = list(best_a.program[:crossover_position] + best_b.program[crossover_position:])
            new_stub_indexes = best_a.stub_indexes[:crossover_position] + best_b.stub_indexes[crossover_position:]
            new_program_indexes = best_a.prog_indexes[:crossover_position] + best_b.prog_indexes[crossover_position:]
            
            # 2.3: mutation
            change_stub = True
            for i in range(len(new_program)):
                if random.random() < mutation_probability:                    
                    # versione 1: cambio solamente il posizionamento delle variabili
                    if not change_stub:
                        if i < crossover_position:
                            st_index = population[0].stub_indexes[i]
                        else:
                            st_index = population[1].stub_indexes[i]
                        
                        possibilities = self.placed_list[st_index]
                        rand_el = random.randint(0, len(possibilities) - 1)
                        new_program[i] = possibilities[rand_el]
                        new_program_indexes[i] = rand_el
                    else:
                        # versione 2: cambio la regola
                        # print("Change rule")
                        new_stub = random.randint(0, len(self.placed_list) - 1)
                        new_prog_pos = random.randint(0, len(self.placed_list[new_stub]) - 1)
                        # print(f"{new_program[i]} replaced with")
                        new_program[i] = self.placed_list[new_stub][new_prog_pos]
                        # print(f"This: {new_program[i]}")
                        new_program_indexes[i] = new_prog_pos
                        new_stub_indexes[i] = new_stub
                        
            # sort the new_program
            new_program.sort()
            
            # check if in list
            found = False
            # print("Current program")
            # print(new_program)
            for el in population:
                if el.program == new_program:
                    # print("Already existing")
                    found = True
                    break
            
            # sys.exit()
            if not found:
                # 3: insert the new element in the population
                cp, cn, current_score, best_found, l_index = evaluate_score(new_program)
                
                if best_found:
                    return [new_program[i] for i in l_index], current_score, True
                
                # ordered insert: find the position
                i = 0
                for i in range(0, len(population)):
                    if current_score > population[i].score:
                        break
                
                population.insert(i, Individual(new_program, new_stub_indexes, new_program_indexes, current_score))
                
                # 4: drop the element with the lowest score
                population = population[:-1]
        print("Iterations completed")
            
        return population[0].program, population[0].score, False