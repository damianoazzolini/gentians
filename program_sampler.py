import random
import copy
import re
import sys

from clingo_interface import ClingoInterface

import utils

# number of underscore for placeholders in atoms
UNDERSCORE_SIZE = 5

class Literal:
    def __init__(self, name : str, arity : int, recall : int, can_be_negated : bool = False) -> None:
        self.name = name
        self.arity = arity
        self.recall = recall
        self.can_be_negated = can_be_negated
        
    def __str__(self) -> str:
        return f"\n{self.name} - Arity {self.arity} - Recall {self.recall} - Negated {self.can_be_negated}"

    def __repr__(self) -> str:
        return self.__str__()

    @staticmethod
    def parse_mode_from_string(modeb : str, head_or_body : str) -> 'Literal':
        # modeb/modeh(1, bird(+))
        # print(modeb)
        modeb = modeb.replace(f'{head_or_body}(','')[:-1]
        # first occurrence of , identifies the two fields
        pos = modeb.find(',')
        recall = modeb[0 : pos]
        
        if recall == '*':
            recall = -9999
        else:
            recall = int(recall)
        
        atom = modeb[pos + 1 : ]
        negated = False
        if atom.lstrip().startswith('not '):
            negated = True
        if negated:
            name = atom.lstrip()[4:].split('(')[0]
        else:
            name = atom.lstrip().split('(')[0]
        if '(' in atom and not(',' in atom):
            arity = 1
        else:
            arity = atom.count(',') + 1

        return Literal(name, arity, recall, negated)
    

    # @staticmethod
    # def get_literak_for_aggregate(aggregate : str) -> 'Literal':
    #     '''
    #     modeagg(#sum, n) where n is the number of atoms
    #     '''
    #     return Literal(f"#{aggregate}",)


    def get_str_representation(self, negated : bool = False) -> str:
        s = self.name
        if self.arity > 0:
            s += '('
            for i in range(0,self.arity):
                s += ('_' * UNDERSCORE_SIZE) + ','
            s = s[:-1] + ')'
        return s if (not negated) else f"not {s}"


class ProgramSampler:
    def __init__(
        self,
        language_bias_head : 'list[str]',
        language_bias_body : 'list[str]',
        max_depth : int = 3,
        max_variables : int = 2,
        # max_clauses : int = 3,
        verbose : int = 0,
        enable_find_max_vars_stub : bool = False,
        find_all_possible_pos_for_vars_one_shot : bool = True,
        allowed_aggregates : 'list[str]' = [],
        arithmetic_operators : 'list[str]' = [],
        comparison_operators : 'list[str]' = []
        ) -> None:
        self.head_atoms : 'list[Literal]' = []
        self.body_literals : 'list[Literal]' = []
        # print(language_bias_head)
        for el in language_bias_head:
            self.head_atoms.append(Literal.parse_mode_from_string(el, "modeh"))

        # print(language_bias_body)
        for el in language_bias_body:
            self.body_literals.append(Literal.parse_mode_from_string(el, "modeb"))

        self.max_depth : int = max_depth
        self.max_variables : int = max_variables
        # self.max_clauses : int = max_clauses
        self.verbose : int = verbose
        self.enable_find_max_vars_stub : bool = enable_find_max_vars_stub
        
        # If true, generates all the answer sets and then deletes the symmetric
        # ones. If false, iteratively generates one answer set, computes the
        # symmetric and then add to the ASP program a constraint for each symmetric.
        # The iterative version is way slower, so True is preferred.
        self.find_all_possible_pos_for_vars_one_shot : bool = find_all_possible_pos_for_vars_one_shot
        
        # True if we are sampling for a constraint, changed every iteration
        self.body_constraint : bool = False
        
        # allowed aggregates
        # self.aggregates : 'list[Literal]' = []
        
        if allowed_aggregates:
            for el in allowed_aggregates:
                # genero automaticamente il prodotto cartesiano tra aggregati e atomi body
                # cioè se ho come modeb a/1 e b/1 e come aggregati #sum e #count ottengo
                # #sum{X : a(X)} #count{X : a(X)} #sum{X : b(X)} #count{X : b(X)}
                # print("AGGREGATES TODO")
                # print(el)
                self.body_literals.append(Literal(f"__{el}",1,1,False))
        
        # sys.exit()
        if arithmetic_operators:
            for el in arithmetic_operators:
                self.body_literals.append(Literal(f"__{el}__",3,1,False))
        
        if comparison_operators:
            for el in comparison_operators:
                self.body_literals.append(Literal(f"__{el}__",2,1,False))

    
    def replace_operators(self, body : 'list[str]') -> 'tuple[list[str],bool]':
        '''
        Replaces the placeholder names with the comparison or arithmetic operator.
        The boolean is false if the number of operators is the same as the number
        of atoms in the body, i.e, the clause is not valid.
        '''
        # body = ["__neq__(_,_)", "__add__(_,_,_)"]
        body_literals = body
        placeholder = 5*'_'
        operators_count = 0
        for i, el in enumerate(body):
            operators_count += 1
            # comparison
            if el.startswith("__lt__"):
                body_literals[i] = placeholder + " < " + placeholder
            elif el.startswith("__gt__"):
                body_literals[i] = placeholder + " > " + placeholder
            elif el.startswith("__eq__"):
                body_literals[i] = placeholder + " == " + placeholder
            elif el.startswith("__neq__"):
                body_literals[i] = placeholder + " != " + placeholder
            # arithmetic
            elif el.startswith("__add__"):
                body_literals[i] = f"{placeholder} + {placeholder} = {placeholder}"
            elif el.startswith("__sub__"):
                body_literals[i] = f"{placeholder} - {placeholder} = {placeholder}"
            elif el.startswith("__mul__"):
                body_literals[i] = f"{placeholder} * {placeholder} = {placeholder}"
            elif el.startswith("__div__"):
                body_literals[i] = f"{placeholder} * {placeholder} = {placeholder}"
            # aggregates
            elif el.startswith("__sum(") or el.startswith("__count(") or el.startswith("__min(") or el.startswith("__max("):
                agg = el[2:5]
                pos = el[6:].find(')')
                atom_to_aggregate = el[6:pos+6]
                name = atom_to_aggregate.split('/')[0]
                arity = atom_to_aggregate.split('/')[1]
                ph = ','.join([UNDERSCORE_SIZE*'_'] * int(arity))
                body_literals[i] = "#" + agg + "{ " + ph + f" : {name}  ( {ph} )" + "} = " + UNDERSCORE_SIZE*'_'
                # print(body_literals[i])
                operators_count -= 1
                # sys.exit()
            else:
                operators_count -= 1
        
        return body_literals, operators_count != len(body)
    
    


    def define_distribution_atoms(
        self,
        available_atoms : 'list[Literal]'
        ) -> 'tuple[list[float],bool]':
        '''
        Returns a list of float representing the probability
        of selecting an atom for the clause (uniform probability).
        The bool is True if the list if of all zeros.
        '''
        # print(body_atoms)
        probs : 'list[float]' = [1/len(available_atoms)] * len(available_atoms)
        zeros : int = 0
        for i in range(len(available_atoms)):
            if available_atoms[i].recall <= 0 and available_atoms[i].recall != -9999:
                probs[i] = 0
                zeros += 1
        # print(probs)
        if len(available_atoms) == zeros:
            return [0] * len(available_atoms), True
        
        uniform_prob = 1 / (len(available_atoms) - zeros)
        for i in range(len(available_atoms)):
            if probs[i] != 0:
                probs[i] = uniform_prob
            
        return probs, False


    def sample_level_distr_recall(self, available_atoms : 'list[Literal]') -> 'tuple[str,int]':
        '''
        Randomly samples an element if the recall is not 0
        '''
        probs : 'list[float]'
        probs, all_zeros = self.define_distribution_atoms(available_atoms)
        # print(probs)
        if not all_zeros:
            v : float = random.random()
            # to avoid floating point errors
            epsilon : float = 10e-5
            
            pos = 0
            while (pos < len(probs)) and (v - epsilon - probs[pos] > 0):
                v -= probs[pos]
                pos += 1
            
            return (
                "not " if (random.random() < 0.5 and available_atoms[pos].can_be_negated) 
                else ""
                ) + available_atoms[pos].get_str_representation(), pos
        else:
            return "", -1


    def generate_asp_program_for_combinations(
        self,
        n_positions : int, 
        n_variables : int, 
        n_vars_in_head : int,
        to_find_max_number : bool = False
        ) -> str:
        '''
        Generate an ASP program to fill the holes in rules.
        to_find_max_number adds some rules to maximize the number
        of clauses. In this way we find the maximum number according
        to the constraints and avoid the generation of unused rules 
        to compute the possible choices.
        '''
        
        # # TEST
        # print("VALORI FISSATI")
        # n_positions = 4
        # n_variables = 3
        # n_vars_in_head = 1
        
        # print(f"n_positions: {n_positions}")
        # print(f"n_variables: {n_variables}")
        # print(f"n_vars_in_head: {n_vars_in_head}")

        s = f"#const n_positions = {n_positions}.\n"
        # generators
        # s += "% generators for the possible positions\n
        # vk(p) states that the k-th variable is at position p\n"
        for i in range(n_variables):
            s += "{v" + str(i) + f"(0..{n_positions - 1})" + '}.\n'
        s += '\n'
        
        # counters for the variables
        for i in range(n_variables):
            s += f"cv{i}(C):- C = #count" + "{" + f"V : v{i}(V)" + "}.\n"
        s += '\n'
        
        # exactly one variable per position
        if n_variables > 1:
            c = ""
            for i in range(n_variables):
                c += f"p(X) :- v{i}(X).\n"
            c = c + '\n\n'
            for i in range(n_positions):
                c += f":- not p({i}).\n"
            c = c + '\n\n'
            s += c
        
        # all the positions must be filled
        c = ":- "
        for i in range(n_variables):
            c += f"cv{i}(X{i}),"
        for i in range(n_variables):
            c += f"X{i}+"
        c = c[:-1] + ' != n_positions.\n\n'
        s += c
        
        # all the variables must be present - removed, that can be 0
        # for i in range(n_variables):
        #     s += f":- cv{i}(0).\n"
        
        # only safe rules: all the variables in the heads must
        # be in a positive literal in the body
        r = "\n"
        # for i in range(n_vars_in_head):
        if n_vars_in_head > 0:
            for i in range(n_variables):
                # cv0_body(C):- C = #count{V : v0(V), V != 0}.
                # :- v0(0), cv0_body(C), C = 0.
                r += f"cv{i}_body(C):- C = #count" + '{' + f"V : v{i}(V), V > {n_vars_in_head - 1}" + "}.\n"
                r += f"cv{i}_head(C):- C = #count" + '{' + f"V : v{i}(V), V <= {n_vars_in_head - 1}" + "}.\n"
                r += f":- cv{i}_head(CH), cv{i}_body(0), CH > 0.\n\n"
            
        s += r
        
        # no variables appearing only once
        for i in range(n_variables):
            # cv0_tot(C):- C = #count{V : v0(V)}.
            # :- cv0_tot(C), C < 2.
            # già inserito prima per il contatore delle variabili, cv{i}
            # s += f"cv{i}_tot(C):- C = #count" + "{" + f"V : v{i}(V)" + "}.\n"
            # = 1 e non < 2 perché permetto che una variabile
            # non sia usata
            s += f":- cv{i}(C), C = 1.\n"
            
        # impose an order to avoid solutions of the form
        # this is done by inserting constraints
        # that are equivalent
        for i in range(n_variables - 1):
            for j in range(i + 1, n_variables):
                s += f":- cv{i}(0), cv{j}(V{j}), V{j} > 0.\n"
            
        s += '\n'
        
        if not to_find_max_number:
            for i in range(n_variables):
                s += f"#show v{i}/1.\n"
        else:
            # add the part to find the maximum number of variables
            # TODO: maybe is hella slow
            for i in range(n_variables):
                s += f"cnt{i}(N):- N = #count" + "{" + f"X : cv{i}(X), X > 0" + "}.\n"
            
            c = "\nn_vars(X):- "
            for i in range(n_variables):
                c += f"cnt{i}(X{i}),"
            for i in range(n_variables):
                c += f"X{i}+"
            c = c[:-1] + ' = X.\n\n'

            s += c + "\n#maximize{X : n_vars(X)}.\n#show n_vars/1.\n"


        return s
    

    def reconstruct_clause(self, model : str, rule_stub : str) -> str:
        atoms = model.split(' ')

        # print(f'IN: {rule_stub}')
        r = rule_stub
        for el in atoms:
            position = int(el.split('(')[1][:-1])
            var = int(el.split('(')[0][1:])
            r = r.replace(f'_v{position:02d}_',f"V{var}")

        # print(f'OUT: {r}')
        return r


    def place_variables_list_of_clauses(self, sampled_clauses : 'list[str]') -> 'list[list[str]]':
        '''
        Loop to place the variable sin all the sampled clauses
        '''
        placed_list : 'list[list[str]]' = []
        
        for clause in sampled_clauses:
            # print("FISSATO")
            # clause = ":- can(_____,_____),can(_____,_____)."
            print(f"Placing variables for {clause}")
            # TODO: miglioria. Qui i valori sono sempre gli stessi,
            # Per esempio: :- a(_), b(_) e :- a(_), c(_) hanno le
            # stesse possibili combinazioni quindi posso evitare di
            # calcolarle nuovamente. Stesso numero di variabili e di
            # posizioni
            r = self.place_variables_clause(clause)
            print('PLACED')
            # for a in r:
            #     print(a)
            if len(r) > 0: # and not (r in placed_list):
                r.sort()
                valid_rules : 'list[str]' = []
                for rl in r:
                    if utils.is_valid_rule(rl):
                        valid_rules.append(rl)
                        print(f"Valid: {rl}")
                    else:
                        print(f"Pruned: {rl}")

                if len(valid_rules) > 0:
                    placed_list.append(valid_rules)
            # print("---------- STOP QUI -------------")
            # sys.exit()
        
        return placed_list


    def place_variables_clause(self, sampled_stub : str) -> 'list[str]':
        '''
        Replaces the _____ with the variables in the clause.
        This now works with only 1 clause
        '''
        res : 'list[str]' = []
        # number of position to insert the variables
        n_positions : int = sampled_stub.count('_' * UNDERSCORE_SIZE)
        # number of variables to insert
        # rv = random.randint(1, self.max_variables)
        rv = self.max_variables # deterministic is better
        if n_positions <= 2:
            n_variables = 1
        else:
            n_variables = rv
        # number of variables in the head
        n_vars_in_head = sampled_stub.split(':-')[0].count('_' * UNDERSCORE_SIZE)
        # print(n_positions, n_variables, n_vars_in_head)
        # TODO: migliorie
        # 1) la variabile coinvolta in una ricorsione deve variare
        # es: a(X):- b(X), a(X).
        # 2) no variabili unsafe (quando c'è negazione)   
        if not(n_positions == 1 and n_variables == 1 and n_vars_in_head == 0):
            # the if is false if there is a constraint :- a(_).
            if self.enable_find_max_vars_stub:
                ### add the optimization part to find the max number of vars
                # TODO: test whether is hella slow
                asp_p = self.generate_asp_program_for_combinations(
                    n_positions,
                    n_variables,
                    n_vars_in_head,
                    True
                )
                # print(asp_p)
                asp_interface = ClingoInterface([asp_p], ["--opt-mode=opt"])
                ctl = asp_interface.init_clingo_ctl()
                
                max_num = 0
                with ctl.solve(yield_=True) as handle:  # type: ignore
                    for m in handle:  # type: ignore
                        max_num = int(str(m).split('n_vars(')[1][:-1])
                # print(max_num)
                n_variables = max_num
            #####
            # sys.exit()
            
            asp_p = self.generate_asp_program_for_combinations(
                n_positions,
                n_variables,
                n_vars_in_head,
                False
            )

            # print(asp_p)
            # TODO: dire che una coppia di atomi uguali non può
            # avere le stesse variabili
            # generates the clause to fill
            for el in range(0, sampled_stub.count('_'*UNDERSCORE_SIZE)):
                sampled_stub = re.sub('_'*UNDERSCORE_SIZE, f"_v{el:02d}_", sampled_stub, count=1)

            # print('sampled stub')
            # print(sampled_stub)
            
            # TEST
            # print("VALORI FISSATI")
            # sampled_stub =  "odd(_v00_):-  odd(_v01_), prev(_v02_,_v03_)."
            # print(asp_p)
            # print("FISSATO")
            # self.find_all_possible_pos_for_vars_one_shot = True
            # res0 = []  
            # res1 = []  
            
            if self.find_all_possible_pos_for_vars_one_shot:
                asp_interface = ClingoInterface([asp_p], ["0"])
                ctl = asp_interface.init_clingo_ctl()      
                
                answer_sets : 'list[str]' = []
                with ctl.solve(yield_=True) as handle:  # type: ignore
                    for m in handle:  # type: ignore
                        # print(str(m))
                        a = str(m).split(' ')
                        a.sort()
                        a = ' '.join(a)
                        answer_sets.append(a)
                        # res.append(self.reconstruct_clause(str(m), sampled_stub))
                
                # print(answer_sets)
                # print(len(answer_sets))
                # generate all the combinations and prune the symmetric
                lo : 'list[str]' = copy.deepcopy(answer_sets)
                # for i in range(0, len(answer_sets)):
                removed : 'list[str]' = []
                for answer in answer_sets:
                    symmetric_as = utils.find_symmetric_answer_sets(answer)
                    current = symmetric_as[0]
                    symm = symmetric_as[1:]
                    if len(symmetric_as) > 0:
                        # print(symmetric_as)
                        if current not in removed:
                            # print("Not in")
                            # print(symmetric_as)
                            for s in symm:
                                s = s.split(' ')
                                s.sort()
                                s = ' '.join(s)
                                removed.append(s)
                                lo.remove(s)
                
                for a in lo:
                    res.append(self.reconstruct_clause(a, sampled_stub))
                # print(len(lo))                
            else:
                # iteratively (until SAT): compute 1 answer set, compute the equivalent
                # answer sets, add them (and the initial) in the program as
                # constraint and continue.
                # This is way more efficient if we know he max number of variables,
                # since we need to add less constraints.
                # print(asp_p)
                enumerated_all = False
                while not enumerated_all:
                    # TODO? Invece di generare un vincolo e poi aggiungerlo,
                    # enumerare tutti gli AS e poi scandirli e scartarli
                    asp_interface = ClingoInterface([asp_p], ["1"])
                    ctl = asp_interface.init_clingo_ctl()
                    current_as = "" 
                    with ctl.solve(yield_=True) as handle:  # type: ignore
                        for m in handle:  # type: ignore
                            current_as = str(m)


                    if len(current_as) > 0:
                        # print(current_as)
                        res.append(self.reconstruct_clause(current_as, sampled_stub))
                        symmetric_as = utils.find_symmetric_answer_sets(current_as)
                        # print(f"Found {len(symmetric_as)} symmetric AS")
                        for sa in symmetric_as:
                            symm = ':- ' + ','.join(sa.split(' ')) + '.\n'
                            asp_p += symm
                    else:
                        enumerated_all = True

        return res
    
    
    def sample_literals_list(self,
        literals_list : 'list[Literal]',
        head : bool = False
        ) -> 'list[str]':
        '''
        Samples a list of literals to be used in either in the head
        or in the body.
        head: True if the sampling is for the head of the rule (to allow constraints)
        body_constraint: True if the sampling is for a constraint (to 
            discard the possibility to sample constraints with a single
            atom, i.e., :- a(_).)
        '''
        list_indexes_sampled_literals : 'list[int]' = [] # indexes
        sampled_list : 'list[str]' = []
        depth = 0
        prob_increase_level = 0.5
        stop = (random.random() > prob_increase_level) if head else False
        
        while (not stop) and (depth < self.max_depth):
            lv, sampled_literal_index = self.sample_level_distr_recall(literals_list)
            if sampled_literal_index == -1:
                stop = True
            else:
                list_indexes_sampled_literals.append(sampled_literal_index)
                literals_list[sampled_literal_index].recall -= 1 # decrease the recall
                if lv == '_stop_':
                    stop = True
                else:
                    sampled_list.append(lv)
                    # here we are in the body of a constraint: we need at least 2 atoms
                if self.body_constraint and depth == 0:
                    stop = False
                else:
                    stop = (random.random() > prob_increase_level)
                depth += 1

        return sampled_list

    
    def sample_clause_stub(self, how_many : int = 0) -> 'list[str]':
        '''
        Samples a single clause.
        '''
        # TODO: 
        # a(_):- b(_), c(_) è equivalente a
        # a(_):- c(_), b(_)
        original_depth : int = self.max_depth
        clauses : 'list[str]' = []
        
        for _ in range(0, how_many):
            body : 'list[str]' = []
            head : 'list[str]' = []
            
            if len(self.head_atoms) > 0:
                if self.verbose:
                    print("No modeh specified")
                head = self.sample_literals_list(copy.deepcopy(self.head_atoms), True) # true allows constraints
                if len(head) == 0:
                    self.body_constraint = True
                else:
                    self.body_constraint = False
            
            # decrease the depth since we already sampled atoms for the head
            self.max_depth -= len(head)
            
            print(self.body_literals)
            # sys.exit()
            body = self.sample_literals_list(copy.deepcopy(self.body_literals))
            
            # print(body)
            
            # replace __lt__, __gt__, __eq__, __neq__, __add__, __sub__, __mul__
            
            body, is_valid = self.replace_operators(body)
            
            print(body, is_valid)
            # sys.exit()

            if is_valid:
                clauses.append(';'.join(sorted(head)) + ":- " + ','.join(sorted(body)) + '.')
            
            # sys.exit()
            self.max_depth = original_depth

            # print(head)
            # print(body)
            
            # super ugly but more interpretable
            # remove the clauses a(_) :- a(_)
            if len(head) == 1 and len(body) == 1 and head == body:
                # print(f'removed: {clauses[-1]}')
                clauses = clauses[:-1]
            # remove the causes :- a(_), a(_)
            elif len(head) == 0 and len(body) == 2:
                if body[0].count('_') == UNDERSCORE_SIZE and body[1].count('_') == UNDERSCORE_SIZE and body[0] == body[1]:
                    # print(f'removed: {clauses[-1]}')
                    clauses = clauses[:-1]

                
            
            # sys.exit()
        return clauses


    #     --- UNUSED ---
    # # def sample_program(self) -> 'tuple[list[str],list[str]]':
    # def sample_program_stub(self) -> 'list[str]':
    #     '''
    #     Samples a program composed of a set of clauses.
    #     TODO: consider the already taken samples to define
    #     the distribution
    #     TODO: by now, only a single clause
    #     TODO: consider the specialization of clauses and whether
    #         they cover positive or negative example
    #     '''
        
    #     cl : 'list[str]' = []
    #     for _ in range(0, random.randint(1, self.max_clauses)):
    #         s = self.sample_clause_stub()
    #         cl.append(s)

    #     return cl


# l0 = Literal("_stop_", 0, 1, False)
# l1 = Literal("bird", 1, 2, False)
# l2 = Literal("can", 2, 2, True)

# body_atoms : 'list[Literal]' = [l0, l1, l2]

# max_depth = 3
# samples = 5
# res = []

# # stores the count of how may times the current literal
# # appeared in the body
# # sampled = {}

# for _ in range(samples):
#     sample = sample_program(body_atoms, max_depth)
#     if sample not in res:
#         res.append(sample)
    
# print(res)
