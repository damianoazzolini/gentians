import random
import copy
import re

from clingo_interface import ClingoInterface

# numebr of underscore for placeholders in atoms
UNDERSCORE_SIZE = 5

class Literal:
    def __init__(self, name : str, arity : int, recall : int, can_be_negated : bool = False) -> None:
        self.name = name
        self.arity = arity
        self.recall = recall
        self.can_be_negated = can_be_negated
        
    def __str__(self) -> str:
        return f"{self.name} - Arity {self.arity} - Recall {self.recall} - Negated {self.can_be_negated}\n"

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
        if atom.startswith('not '):
            negated = True
        if negated:
            name = atom[4:].split('(')[0]
        else:
            name = atom.split('(')[0]
        if '(' in atom and not(',' in atom):
            arity = 1
        else:
            arity = atom.count(',') + 1

        return Literal(name, arity, recall, negated)


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
        max_clauses : int = 3,
        verbose : int = 0
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
        self.max_clauses : int = max_clauses
        self.verbose : int = verbose
        
    @staticmethod
    def define_distribution_for_body(
        body_atoms : 'list[Literal]'
        ) -> 'tuple[list[float],bool]':
        '''
        Returns a list of float representing the probability
        of selecting an element for the body (uniform probaiblity).
        The bool is True if the list if of all zeros.
        '''
        # print(body_atoms)
        probs : 'list[float]' = [1/len(body_atoms)] * len(body_atoms)
        zeros : int = 0
        for i in range(len(body_atoms)):
            if body_atoms[i].recall <= 0 and body_atoms[i].recall != -9999:
                probs[i] = 0
                zeros += 1
        # print(probs)
        if len(body_atoms) == zeros:
            return [0] * len(body_atoms), True
        
        uniform_prob = 1 / (len(body_atoms) - zeros)
        for i in range(len(body_atoms)):
            if probs[i] != 0:
                probs[i] = uniform_prob
            
        return probs, False

    @staticmethod
    def sample_level_distr_recall(body_atoms : 'list[Literal]') -> 'tuple[str,int]':
        '''
        Randomly samples an element if the recall is not 0
        '''
        probs : 'list[float]'
        probs, all_zeros = ProgramSampler.define_distribution_for_body(body_atoms)
        # print(probs)
        if not all_zeros:
            v : float = random.random()
            # to avoid floating point errors
            epsilon : float = 10e-5
            
            pos = 0
            while (pos < len(probs)) and (v - epsilon - probs[pos] > 0):
                v -= probs[pos]
                pos += 1
            
            return ("not " if (random.random() < 0.5 and body_atoms[pos].can_be_negated) else "") +  body_atoms[pos].get_str_representation(), pos
        else:
            return "", -1

    # @staticmethod
    # def sample_level(body_atoms : 'list[Literal]') -> str:
    #     '''
    #     Randomly samples an element and whether is true or false
    #     '''
    #     pos = random.randint(0, len(body_atoms) - 1)
    #     return ("not " if (random.random() < 0.5 and body_atoms[pos].can_be_negated) else "") +  body_atoms[pos].get_str_representation()

    def generate_asp_program_for_combinations(
        self,
        n_positions : int, 
        n_variables : int, 
        n_vars_in_head : int) -> str:
        '''
        Generate an ASP program to fill the holes in rules.
        '''
        s = f"#const n_positions = {n_positions}.\n"
        
        print(n_vars_in_head)
        print(n_positions)
        print(n_variables)
        
        # generators
        # s += "% generators for the possible positions\nvk(p) states that the k-th variable is at position p\n"
        for i in range(n_variables):
            s += "{v" + str(i) + f"(0..{n_positions - 1})" + '}.\n'
        s += '\n'
        
        # counters for the variables
        for i in range(n_variables):
            s += f"cv{i}(C):- C = #count" + "{" + f"V : v{i}(V)" + "}.\n"
        s += '\n'
        
        # only one variable per position
        if n_variables > 1:
            c = ":- "
            for i in range(n_variables):
                c += f"v{i}(X),"
            c = c[:-1] + '.\n\n'
            s += c
        
        # all the positions must be filled
        c = ":- "
        for i in range(n_variables):
            c += f"cv{i}(X{i}),"
        for i in range(n_variables):
            c += f"X{i}+"
        c = c[:-1] + ' != n_positions.\n\n'
        s += c
        
        # all the variables must be present
        for i in range(n_variables):
            s += f":- cv{i}(0).\n"
        
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
            s += f"cv{i}_tot(C):- C = #count" + "{" + f"V : v{i}(V)" + "}.\n"
            s += f":- cv{i}_tot(C), C < 2.\n"
            
        s += '\n'
        for i in range(n_variables):
            s += f"#show v{i}/1.\n"
        
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


    def place_variables_clause(self, sampled_stub : str) -> 'list[str]':
        '''
        Replaces the _____ with the variables in the clause.
        This now works with only 1 clause
        '''
        res : list[str] = []
        asp_p = self.generate_asp_program_for_combinations(
            sampled_stub.count('_' * UNDERSCORE_SIZE),
            random.randint(1, self.max_variables), # random number of variables
            sampled_stub.split(':-')[0].count('_' * UNDERSCORE_SIZE)
            )
        
        # print(asp_p)

        for el in range(0, sampled_stub.count('_'*UNDERSCORE_SIZE)):
            sampled_stub = re.sub('_'*UNDERSCORE_SIZE, f"_v{el:02d}_", sampled_stub, count=1)

        # print('sampled stub')
        # print(sampled_stub)
        # print(asp_p)
        asp_interface = ClingoInterface([asp_p], ["0"])
        ctl = asp_interface.init_clingo_ctl()        

        with ctl.solve(yield_=True) as handle:  # type: ignore
            for m in handle:  # type: ignore
                # print(str(m))
                res.append(self.reconstruct_clause(str(m), sampled_stub))

        return res
    
    
    def sample_literals_list(self, literals_list : 'list[Literal]', head : bool = False) -> 'list[str]':
        '''
        Samples a list of literals to be used in either in the head
        or in the body.
        '''
        list_indexes_sampled_literals : 'list[int]' = [] # indexes
        sampled_list : 'list[str]' = []
        depth = 0
        prob_increase_level = 0.5
        stop = (random.random() > prob_increase_level) if head else False
        
        while (not stop) and (depth < self.max_depth):
            lv, sampled_literal = ProgramSampler.sample_level_distr_recall(literals_list)
            if sampled_literal == -1:
                stop = True
            else:
                list_indexes_sampled_literals.append(sampled_literal)
                literals_list[sampled_literal].recall -= 1 # decrease the recall
                if lv == '_stop_':
                    stop = True
                else:
                    sampled_list.append(lv)
                stop = (random.random() > prob_increase_level)
                depth += 1

        return sampled_list

    
    def sample_clause_stub(self) -> str:
        '''
        Samples a single clause.
        '''
        body : 'list[str]' = []
        head : 'list[str]' = []
        # body_atoms_copy = self.body_literals.copy()
        
        body = self.sample_literals_list(copy.deepcopy(self.body_literals))
        head = self.sample_literals_list(copy.deepcopy(self.head_atoms), True)

        sampled_program = ';'.join(head) + ":- " + ','.join(body) + '.'

        return sampled_program


    # def sample_program(self) -> 'tuple[list[str],list[str]]':
    def sample_program_stub(self) -> 'list[str]':
        '''
        Samples a program composed of a set of clauses.
        TODO: consider the already taken samples to define
        the distribution
        TODO: by now, only a single clause
        TODO: consider the specialization of clauses and whether
            they cover positive or negative example
        '''
        
        cl : 'list[str]' = []
        for _ in range(0, random.randint(1, self.max_clauses)):
            s = self.sample_clause_stub()
            cl.append(s)

        return cl


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
