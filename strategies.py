import random
import sys
import math
import time

import clingo_interface


def compute_n_vars(clause : str):
    i = 0
    found = True
    while found:
        if f'V{i}' not in clause:
            found = False
        i +=1
    
    return i - 1
    

class PlacedClause:
    '''
    Class containing a clause.
    '''
    def __init__(self,
        placed_clauses : 'list[str]'
        ) -> None:
        self.placed_clauses = placed_clauses
        self.n_vars_clauses : 'list[int]' = []
        self.n_atoms = 0

        for cl in self.placed_clauses:
            self.n_vars_clauses.append(compute_n_vars(cl))

        cl = placed_clauses[0]
        cl = cl.split(':-')
        head = cl[0]
        body = cl[1]

        # print(len(head))
        if len(head) != 0:
            self.n_atoms += len(head.split(';'))
            
        self.n_atoms += len(body.split('),'))

    def __str__(self) -> str:
        s = ""
        for cl in self.placed_clauses:
            s += cl + '\n'
        s += f"n_vars: {self.n_vars_clauses}\nn_atoms: {self.n_atoms}\n"
        return s

    def __repr__(self) -> str:
        return self.__str__()


class Strategy:
    def __init__(self,
        # placed_list : 'list[list[str]]',
        placed_list : 'list[PlacedClause]',
        background : 'list[str]',
        positive_examples : 'list[list[str]]',
        negative_examples : 'list[list[str]]',
        ) -> None:
        # self.placed_list : 'list[list[str]]' = placed_list
        self.placed_list : 'list[PlacedClause]' = placed_list
        self.background : 'list[str]' = background
        self.positive_examples : 'list[list[str]]' = positive_examples
        self.negative_examples : 'list[list[str]]' = negative_examples

    def genetic_solver(self,
        number_clauses : int, # number of clauses to consider for each program
        population_size : int, # number of programs to keep
        mutation_probability : float, # mutation probability
        max_interations : int, # maximum number of iterations
        do_tournament : bool = True, # choose tournament to pick the elements
        tournament_size : int = 12, # number of elements considered for the tournament
        prob_replacing_oldest : float = 0.5, # the probability to replace the oldest instead of the one with the lowest fittness
        k_best_for_the_next_round : int = 5 # the top k individuals to keep for the next round
        ) -> 'tuple[list[str], float, bool, list[int]]':
        '''
        Genetic algorithm to find the best program
        '''
        class Individual:
            def __init__(self,
                program : 'list[str]',
                stub_indexes : 'list[int]',
                prog_indexes : 'list[int]',
                score : float,
                is_best : bool = False, # does this covers everyting positive and no negative?
                l_best_indexes : 'list[int]' = [] # best indexes, if it is the best
                ) -> None:
                self.program = program
                # stub_indexes is a list of int representing the index of the stub 
                # clauses selected
                self.stub_indexes = stub_indexes
                # prog_indexes is a list of int representing the index of the program 
                # selected for the stub_indexes clauses - maybe not needed
                self.prog_indexes = prog_indexes
                self.score = score
                self.is_best = is_best
                self.l_best_indexes = l_best_indexes
                self.generated_timestamp = time.time()

            def __str__(self) -> str:
                return f"Program: {self.program} - score: {self.score}"

            def __repr__(self) -> str:
                return self.__str__()


        def evaluate_score(
                stub_indexes : 'list[int]',
                prog_indexes : 'list[int]',
                program : 'list[str]'
            ) -> 'tuple[float, bool, list[int]]':
            # returns covered positive, covered negative, score
            # how to assign a score?
            # Current: cp covered positive, cn covered negative
            # if cp = 0 and cn > 0 -> score = - cn
            # if cp > 0 -> score = cp / (cp + cn)
            # if score = 1 -> optimum found
            # print(self.background)
            # TODO: better define a score. Also consider the number of variables?
            asp_solver = clingo_interface.ClingoInterface(
                self.background, ['-Wnone', '0', '--project'])
            # program[1] = "odd(V0):- even(V1),prev(V0,V1)."
            # program[0] = "even(V0):- odd(V1),prev(V0,V1)."
            # for l in asp_solver.lines:
            #     print(l) 
            # # print(asp_solver.lines)
            # for p in program:
            #     print(p)
            # sys.exit()
            cov = asp_solver.extract_coverage_and_set_clauses(
                program, self.positive_examples, self.negative_examples, False)
            
            # print(program)

            # print(cov)
            # sys.exit()
            best_found = False
            best_cp = -1000
            best_cn = 1000
            l_index : 'list[int]' = []
            l_best_indexes : 'list[str]' = []
            # best_index : 'list[int]' = []
            best_l_index = []

            for res, element_coverage in cov.items():
                if res != "Error":
                    # set to remove duplicates
                    cp : int = len(list(set(element_coverage.l_pos)))
                    cn : int = len(list(set(element_coverage.l_neg)))
                    # print(cp,cn)
                    l_index = [int(v) for v in list(res)]
                    # qui non va bene: se copro tutti allora mai cp > best_cp
                    # if cp > best_cp:
                    if cp >= best_cp and cn <= best_cn:
                        # print(cp, cn, l_index)
                        best_cp = cp
                        best_cn = cn
                        best_l_index = l_index

                    if cp == len(self.positive_examples):
                        if cn == 0:
                            print(f"Best found with indexes {res}")
                            print(program)
                            l_best_indexes.append(res)
                            best_found = True
                        # else:
                        #     print("Coverage 100% of the positive with")
                        # print([program[i] for i in l_index], cp, cn)

            score = best_cp - best_cn

            # if score != 0:
            scores : 'list[float]' = []
            # The score is now computed as the sum of exp(n_atoms + n_vars)
            # for each clause
            # print(f"best_l_index: {best_l_index}")
            # print(f"score: {score}")
            if len(best_l_index) == 0:
                # for the empty list (no program) i assume that the
                # score is simply the covered positive - covered negative
                scores.append(score)
            for i in best_l_index:
                # gather the complexity from the list
                si = stub_indexes[i]
                pi = prog_indexes[i]
                # print(placed_list[si].placed_clauses[pi])
                # print(placed_list[si].n_atoms)
                na = self.placed_list[si].n_atoms
                nv = self.placed_list[si].n_vars_clauses[pi]
                
                scores.append(score*math.exp(-(na+nv)))
            # print(program)
            # print(scores)
            score = sum(scores)
            # print(score)
            
            # sys.exit()

            # shortest one
            l_best_indexes.sort(key = lambda s : len(s))
            l_index = [int(v) for v in list(l_best_indexes[0])] if len(l_best_indexes) > 0 else []

            return score, best_found, l_index

    
        def get_fittest(selected_individuals : 'list[Individual]') -> Individual:
            '''
            Returns the fittest element in the current selection
            '''
            return max(selected_individuals, key=lambda x : x.score)

        
        def tournament(
            population: 'list[Individual]',
            tournament_size : int = 12,
            prob_selecting_fittest : float = 0.9
            ):
            '''
            Tournament to select the individuals to combine and mutate
            '''
            random_subset = random.sample([x for x in population], tournament_size)
            stop = False
            best_element = get_fittest(random_subset)
            while len(random_subset) > 0 and not stop:
                if random.random() > prob_selecting_fittest:
                    random_subset.remove(best_element)
                    best_element = get_fittest(random_subset)
                else:
                    stop = True

            return best_element
        
        
        def pick_two_fittest(
            population: 'list[Individual]',
            pick_uniform : bool = True
            ) -> 'tuple[Individual,Individual]':
            '''
            Pick the two fittest elements.
            If pick_uniform is true, select a random element between the ones with
            the highest fit (since most programs have the same fitness).
            '''
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
            if not pick_uniform:
                # this is the naive version. However, since many programs have the same
                # score, # i should choose a random one among these
                best_a = population[0]
                best_b = population[1]
            else:
                idx_a, idx_b = random.sample(range(0, j), 2)
                # print(f"Combining: {idx_a}, {idx_b}")
                best_a = population[idx_a]
                best_b = population[idx_b]

            return best_a, best_b

        
        def crossover(best_a : Individual, best_b : Individual) -> 'tuple[Individual,Individual]':
            '''
            Crossover: pick a random index and generate a element
            '''
            crossover_position = random.randint(0, len(best_a.program) - 1)
            # print(f"Crossover: {crossover_position}")
            new_program = list(best_a.program[:crossover_position] + best_b.program[crossover_position:])
            new_stub_indexes = best_a.stub_indexes[:crossover_position] + best_b.stub_indexes[crossover_position:]
            new_program_indexes = best_a.prog_indexes[:crossover_position] + best_b.prog_indexes[crossover_position:]
            current_score, is_best, l_indexes = evaluate_score(new_stub_indexes, new_program_indexes, new_program)
            i0 = Individual(new_program, new_stub_indexes, new_program_indexes, current_score, is_best, l_indexes)

            new_program = list(best_b.program[:crossover_position] + best_a.program[crossover_position:])
            new_stub_indexes = best_b.stub_indexes[:crossover_position] + best_a.stub_indexes[crossover_position:]
            new_program_indexes = best_b.prog_indexes[:crossover_position] + best_a.prog_indexes[crossover_position:]
            current_score, is_best, l_indexes = evaluate_score(new_stub_indexes, new_program_indexes, new_program)
            i1 = Individual(new_program, new_stub_indexes, new_program_indexes, current_score, is_best, l_indexes)

            return i0, i1
        
        
        def mutate(element : Individual, change_stub : bool = True):
            '''
            Mutation of an element
            '''
            change_stub = True
            new_element = element
            something_changed = False
            
            for i, _ in enumerate(element.program):
                if random.random() < mutation_probability:
                    something_changed = True
                    # versione 1: cambio solamente il posizionamento delle variabili
                    if not change_stub:
                        possibilities = self.placed_list[element.stub_indexes[i]]
                        rand_el = random.randint(0, len(possibilities.placed_clauses) - 1)
                        new_element.program[i] = possibilities.placed_clauses[rand_el]
                        new_element.prog_indexes[i] = rand_el
                    else:
                        # versione 2: cambio la regola
                        new_stub = random.randint(0, len(self.placed_list) - 1)
                        new_prog_pos = random.randint(0, len(self.placed_list[new_stub].placed_clauses) - 1)
                        # print(f"{new_program[i]} replaced with")
                        new_element.program[i] = self.placed_list[new_stub].placed_clauses[new_prog_pos]
                        # print(f"This: {new_program[i]}")
                        new_element.prog_indexes[i] = new_prog_pos
                        new_element.stub_indexes[i] = new_stub
            
            # TODO: add annealing to accept or reject the mutated program?
            # compute the new score if something has changed
            if something_changed:
                new_element.generated_timestamp = time.time()
                new_element.score, new_element.is_best, new_element.l_best_indexes =\
                    evaluate_score(new_element.stub_indexes, new_element.prog_indexes, 
                                   new_element.program)
            
            return new_element


        def initialize_population(
            number_clauses : int,
            # placed_list : 'list[list[str]]',
            placed_list : 'list[PlacedClause]',
            population_size : int
            ) -> 'tuple[list[Individual],bool]':
            '''
            Initialize the population of individuals
            '''
            sampled_individuals : 'list[Individual]' = []
            best_found = False
            
            while len(sampled_individuals) < population_size:
                # pick a program
                # TODO: non necessariamente il sampling deve essere senza ripetizioni
                stub_indexes : 'list[int]' = sorted(
                    random.sample(
                        range(len(self.placed_list)),
                        number_clauses if len(placed_list) > number_clauses
                                        else len(placed_list)
                    )
                )

                # for every index, select one of the possible variable placement
                program : 'list[str]' = []
                prog_indexes : 'list[int]' = []
                for i in stub_indexes:
                    # el = random.randint(0, len(placed_list[i]) - 1)
                    el = random.randint(0, len(placed_list[i].placed_clauses) - 1)
                    prog_indexes.append(el)
                    # program.append(placed_list[i][el])
                    program.append(placed_list[i].placed_clauses[el])

                program = sorted(program)
                # cp is the current program
                # cp, cn, current_score, best_found, l_index = evaluate_score(program)
                # print("evaluate score in init")
                current_score, best_found, l_index = evaluate_score(stub_indexes, prog_indexes, program)

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
            return population[0].program, population[0].score, True, [-1]

        # step 1: sort in terms of decreasing fittnes
        population.sort(key = lambda x : x.score, reverse=True)

        # step 2: iterate trough programs
        print(f"Running for {max_interations} iterations")
        for it in range(max_interations + 1):
            # print(f"it: {it}")
            if it % 100 == 0:
                print(f"Iteration {it} - best: {population[0]}")

            # 2.1: selection of the two fittest elements
            # print('pre torunament')
            if do_tournament:
                best_a = tournament(population, tournament_size)
                best_b = tournament(population, tournament_size)
            else:
                best_a, best_b = pick_two_fittest(population)
            

            # either do crossover or mutation seems to be not effective
            # prob_crossover = 0.05
            
            # 2.2: crossover
            # print('pre cross')
            new_program_1, new_program_2 = crossover(best_a, best_b)
            # TODO: check whether best found, to stop the iteration
            # if one of the two covers all the positive and none of the negative?
            
            # 2.3: mutation
            # https://arxiv.org/pdf/2305.01582.pdf
            # print('pre mutate')
            new_mutated_1 = mutate(new_program_1)
            new_mutated_2 = mutate(new_program_2)
            
            l_mutated = [new_mutated_1, new_mutated_2]
            
            # 3: replace elements in the population
            # print('pre replace')
            for el in l_mutated:
                # if best, return
                if el.is_best:
                    return [el.program[i] for i in el.l_best_indexes], el.score, True, [-1]

                found = False
                # if not best, check whether it is already in the population
                for pop in population:
                    if sorted(pop.program) == sorted(el.program):
                        found = True
                        break
                
                # if not in the population, insert
                if not found:
                    i = 0
                    for i, element in enumerate(population):
                        # equal to have some variability?
                        if el.score >= element.score:
                            break
                    population.insert(i, el)

                    # drop the element
                    if random.random() < prob_replacing_oldest:
                        # drop the oldest element
                        oldest = min(population, key=lambda x : x.generated_timestamp)
                        population.remove(oldest)
                    else:
                        # drop the element with the lowest fitness
                        population = population[:-1]

        print("Iterations completed")
        
        # keep the elements for the next round: extract all the stubs from
        # the top k programs. Then, count the occurrences of each and return the top
        # k stubs that occur the most
        all_indexes_list : 'list[int]' = [] 
        for i in range(1, k_best_for_the_next_round + 1):
            print(population[i].program)
            all_indexes_list.extend(population[i].stub_indexes)
        
        # create a dict to count the occurrences, sort it, and return the top
        # k elements that occur the most
        s = {x:all_indexes_list.count(x) for x in set(all_indexes_list)}
        a = sorted(s.items(), key=lambda x: x[1], reverse=True)
   
        return population[0].program, population[0].score, False, [i[0] for i in a[:k_best_for_the_next_round]]
