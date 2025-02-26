import random
import copy
import sys
import itertools # to generate unbalanced aggregates

from .arguments import Arguments
from .utils import UNDERSCORE_SIZE, print_error_and_exit
from .parser import ModeDeclaration

# number of underscore for placeholders in atoms
# UNDERSCORE_SIZE = 5

# class Literal:
#     def __init__(self, name : str, arity : int, recall : int, can_be_negated : bool = False) -> None:
#         self.name = name
#         self.arity = arity
#         self.recall = recall
#         self.can_be_negated = can_be_negated
        
#     def __str__(self) -> str:
#         return f"\n{self.name} - Arity {self.arity} - Recall {self.recall} - Negated {self.can_be_negated}"

#     def __repr__(self) -> str:
#         return self.__str__()

#     @staticmethod
#     def parse_mode_from_string(modeb : str, head_or_body : str) -> 'Literal':
#         # modeb/modeh(1, bird(+))
#         # print(modeb)
#         modeb = modeb.replace(f'{head_or_body}(','')[:-1]
#         # first occurrence of , identifies the two fields
#         pos = modeb.find(',')
#         recall = modeb[0 : pos]
        
#         if recall == '*':
#             recall = -9999
#         else:
#             recall = int(recall)
        
#         atom = modeb[pos + 1 : ]
#         negated = False
#         if atom.lstrip().startswith('not '):
#             negated = True
#         if negated:
#             name = atom.lstrip()[4:].split('(')[0]
#         else:
#             name = atom.lstrip().split('(')[0]
#         if '(' in atom and not(',' in atom):
#             arity = 1
#         else:
#             arity = atom.count(',') + 1

#         return Literal(name, arity, recall, negated)


#     def get_str_representation(self, negated : bool = False) -> str:
#         s = self.name
#         if self.arity > 0:
#             s += '('
#             for i in range(0,self.arity):
#                 s += ('_' * UNDERSCORE_SIZE) + ','
#             s = s[:-1] + ')'
#         return s if (not negated) else f"not {s}"


class ProgramSampler:
    def __init__(
            self,
            language_bias_head : 'list[ModeDeclaration]',
            language_bias_body : 'list[ModeDeclaration]',
            args : Arguments
        ) -> None:
        self.args : Arguments = args
        self.language_bias_head : 'list[ModeDeclaration]' = language_bias_head
        self.language_bias_body : 'list[ModeDeclaration]' = language_bias_body

        # # print(language_bias_head)
        # for el in language_bias_head:
        #     self.head_atoms.append(Literal.parse_mode_from_string(el, "modeh"))

        # # print(language_bias_body)
        # for el in language_bias_body:
        #     self.body_literals.append(Literal.parse_mode_from_string(el, "modeb"))
        
        # # True if we are sampling for a constraint, changed every iteration
        self.body_constraint : bool = False
        
        # enable recursion: super carefully with aggregates since this may
        # cause loops: for instance, this program loops
        # {el(1,2)}.
        # s1(V0):- V2+V1=V0,s0(V1),s1(V2).
        # s0(V0):- #sum{V2,V1:el(V1,V2)}=V0.
        # s1(V0):-  #sum{V2,V1:el(V1,V2)}=V0,#sum{V2,V1:el(V2,V1)}=V0.
        self.enable_recursion = False

        # store the already placed clauses to avoid recomputation
        # removed since all the clauses are different
        # self.stub_placed_dict : 'dict[str,list[str]]' = {}
        
        if self.args.aggregates:
            for el in self.args.aggregates:
                # compute the cartesian product between aggregates and body atoms
                # ex: modeb a/1 and b/1 and aggregates #sum e #count i get
                # #sum{X : a(X)} #count{X : a(X)} #sum{X : b(X)} #count{X : b(X)}
                # self.body_literals.append(Literal(f"__{el}",1,1,False))
                self.language_bias_body.append(ModeDeclaration(("1",f"__{el}","1","positive"), False))
        
        # sys.exit()
        if self.args.arithmetic_operators:
            for el in self.args.arithmetic_operators:
                # self.body_literals.append(Literal(f"__{el}__",3,1,False))
                self.language_bias_body.append(ModeDeclaration(("1",f"__{el}__","3","positive"), False))
        
        if self.args.comparison_operators:
            for el in self.args.comparison_operators:
                # self.body_literals.append(Literal(f"__{el}__",2,1,False))
                self.language_bias_body.append(ModeDeclaration(("1",f"__{el}__","2","positive"), False))
                

    def __replace_operators(self, body : 'list[str]') -> 'list[list[str]]':
        '''
        Replaces the placeholder names with the comparison or arithmetic operator.
        The boolean is false if the number of operators is the same as the number
        of atoms in the body, i.e, the clause is not valid (removed).
        '''
        # TODO: improve this, it is awful.
        body_literals = body
        # print(body_literals)
        placeholder = 5*'_'
        operators_count = 0
        aggregates_indexes : list[int] = []
        all_aggr : 'list[list[str]]' = []
        for i, el in enumerate(body):
            operators_count += 1
            # comparison
            if el.startswith("__lt__"):
                body_literals[i] = placeholder + "<" + placeholder
            if el.startswith("__leq__"):
                body_literals[i] = placeholder + "<=" + placeholder
            elif el.startswith("__gt__"):
                body_literals[i] = placeholder + ">" + placeholder
            elif el.startswith("__geq__"):
                body_literals[i] = placeholder + ">=" + placeholder
            elif el.startswith("__eq__"):
                body_literals[i] = placeholder + "==" + placeholder
            elif el.startswith("__neq__"):
                body_literals[i] = placeholder + "!=" + placeholder
            # arithmetic
            elif el.startswith("__add__"):
                body_literals[i] = f"{placeholder}+{placeholder}={placeholder}"
            elif el.startswith("__sub__"):
                body_literals[i] = f"{placeholder}-{placeholder}={placeholder}"
            elif el.startswith("__mul__"):
                body_literals[i] = f"{placeholder}*{placeholder}={placeholder}"
            elif el.startswith("__div__"):
                body_literals[i] = f"{placeholder}/{placeholder}={placeholder}"
            elif el.startswith("__abs__"):
                body_literals[i] = f"|{placeholder}-{placeholder}|={placeholder}"
            # aggregates
            elif el.startswith("__sum(") or el.startswith("__count(") or el.startswith("__min(") or el.startswith("__max("):
                inc = 0
                if el.startswith("__count("):
                    inc = 2
                agg = el[2:5 + inc]
                pos = el[6 + inc : ].find(')')
                atom_to_aggregate = el[6 + inc : pos + 6 + inc]
                max_arity = 0
                names : 'list[str]' = []
                arities : 'list[int]' = []
                for atom_in_agg in atom_to_aggregate.split(','):
                    names.append(atom_in_agg.split('/')[0])
                    arities.append(int(atom_in_agg.split('/')[1]))
                    max_arity = max_arity + int(atom_in_agg.split('/')[1])

                # if self.unbalanced_aggregates
                # sum/2 -> #sum{ _ : a(_,_)} e #sum{ _, _ : a(_,_)}
                if self.args.unbalanced_aggregates:
                    current : 'list[str]' = []
                    for current_arity in range(1, max_arity + 1):
                        ph = ','.join([UNDERSCORE_SIZE*'_'] * int(current_arity))
                        atoms_in_agg = ":"
                        for name, arity in zip(names,arities):
                            ph_atom = ','.join([UNDERSCORE_SIZE*'_'] * int(arity))
                            atoms_in_agg += f"{name}({ph_atom}),"
                        current.append("#" + agg + "{" + ph + atoms_in_agg[:-1] + "}=" + UNDERSCORE_SIZE*'_')
                    all_aggr.append(current)
                else:
                    atoms_in_agg = ":"
                    for name, arity in zip(names,arities):
                        ph_atom = ','.join([UNDERSCORE_SIZE*'_'] * int(arity))
                        atoms_in_agg += f"{name}({ph_atom}),"
                    ph = ','.join([UNDERSCORE_SIZE*'_'] * sum(arities))
                    body_literals[i] = "#" + agg + "{" + ph + atoms_in_agg[:-1] + "}=" + UNDERSCORE_SIZE*'_'

                operators_count -= 1
                aggregates_indexes.append(i)
            else:
                operators_count -= 1

        
        nb : 'list[list[str]]' = []
        for agg_comb in itertools.product(*all_aggr):
            cb = body_literals[:]
            for agg, index in zip(agg_comb,aggregates_indexes):
                cb[index] = agg
            nb.append(cb)

        return nb
    

    def __define_distribution_atoms(
            self,
            available_atoms : 'list[ModeDeclaration]'
        ) -> 'tuple[list[float],bool]':
        '''
        Returns a list of float representing the probability
        of selecting an atom for the clause (uniform probability).
        The bool is True if the list if of all zeros.
        '''
        zeros : int = 0
        probs : 'list[float]' = []

        try:
            probs = [1/len(available_atoms)] * len(available_atoms)
        except:
            print_error_and_exit("No atoms available.")
        
        for i in range(len(available_atoms)):
            if available_atoms[i].recall <= 0 and available_atoms[i].recall != -9999:
                probs[i] = 0
                zeros += 1

        if len(available_atoms) == zeros:
            return [0] * len(available_atoms), True
        
        uniform_prob = 1 / (len(available_atoms) - zeros)
            
        for i in range(len(available_atoms)):
            if probs[i] != 0:
                probs[i] = uniform_prob
            
        return probs, False


    def __sample_level_distr_recall(self, available_atoms : 'list[ModeDeclaration]') -> 'tuple[str,int]':
        '''
        Randomly samples an element if the recall is not 0
        '''
        probs : 'list[float]'
        probs, all_zeros = self.__define_distribution_atoms(available_atoms)
        # print(probs)
        if not all_zeros:
            v : float = random.random()
            # to avoid floating point errors
            epsilon : float = 10e-5
            
            pos = 0
            while (pos < len(probs)) and (v - epsilon - probs[pos] > 0):
                v -= probs[pos]
                pos += 1
            
            negated = random.random() < 0.5 and (not available_atoms[pos].positive)
            return available_atoms[pos].get_str_representation(negated), pos
        else:
            return "", -1


    def __sample_literals_list(self,
            literals_list : 'list[ModeDeclaration]',
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
        stop = (random.random() > self.args.prob_increase) if head else False
        max_depth_head = self.args.disjunctive_head_length
        
        while (not stop) and (depth < self.args.max_depth) and (max_depth_head > 0):
            lv, sampled_literal_index = self.__sample_level_distr_recall(literals_list)
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
                    stop = (random.random() > self.args.prob_increase)
                depth += 1
            if head:
                max_depth_head -= 1
        return sampled_list

    
    def sample_clause_stub(self, how_many : int = 0) -> 'list[str]':
        '''
        Samples a single clause.
        '''
        original_depth : int = self.args.max_depth
        clauses : 'list[str]' = []
        # not_merged_clauses = []
        
        for _ in range(0, how_many):
            body : 'list[str]' = []
            head : 'list[str]' = []
            
            if len(self.language_bias_head) > 0:
                head = self.__sample_literals_list(copy.deepcopy(self.language_bias_head), True) # true allows constraints
                self.body_constraint = (len(head) == 0)
                # if len(head) == 0:
                #     self.body_constraint = True
                # else:
                #     self.body_constraint = False
            
            # decrease the depth since we already sampled atoms for the head
            self.args.max_depth -= len(head)
            
            # print(self.body_literals)
            body = self.__sample_literals_list(copy.deepcopy(self.language_bias_body))
            
            # replace __lt__, __gt__, __eq__, __neq__, __add__, __sub__, __mul__
            # body, is_valid = self.__replace_operators(body)
            body = self.__replace_operators(body) # TODO: fix this
            
            is_valid = True
            if is_valid and self.enable_recursion is False:
                for b in body:
                    subs_h = set(head).issubset(set(b)) and len(set(head)) > 0
                    subs_b = set(b).issubset(set(head)) and len(set(b)) > 0
                    is_valid = not (subs_h or subs_b)
                    if is_valid:
                        clauses.append(';'.join(sorted(head)) + ":- " + ','.join(sorted(b)) + '.')
                        # not_merged_clauses.append([sorted(head),sorted(b)])
            # TODO: and what happens with enable recursion True?
            
            self.args.max_depth = original_depth

        return clauses
    