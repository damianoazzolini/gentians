import random
import copy
import re
import sys
import itertools # to generate unbalanced aggregates

from clingo_interface import ClingoInterface

import utils
from utils import AggregateElement

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
        prob_increase_level : float = 0.5,
        # max_clauses : int = 3,
        verbose : int = 0,
        enable_find_max_vars_stub : bool = False,
        find_all_possible_pos_for_vars_one_shot : bool = True,
        disjunctive_head_length : int = 1, # number of atoms allowed in the head
        unbalanced_aggregates : bool = False, # to allow #count{X : a(X,Y)} = C, g(Y).
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
        # max number of atoms in the head
        self.disjunctive_head_length : int = disjunctive_head_length
        # a boolean, false by default, that allows unbalanced aggregates, 
        # i.e., aggregates where some terms may appear in the body of the
        # rule itself. For instance: #count{X : a(X,Y)} = C, g(Y).
        # is allowed when the bool is set to true, but not allowed
        # when false
        self.unbalanced_aggregates : bool = unbalanced_aggregates
        
        # probability to add another literal in the current clause,
        # i.e., of going down one more level
        self.prob_increase_level : float = prob_increase_level
        
        # enable recursion: super carefully with aggregates since this may
        # cause loops: for instance, this program loops
        # {el(1,2)}.
        # s1(V0):- V2+V1=V0,s0(V1),s1(V2).
        # s0(V0):- #sum{V2,V1:el(V1,V2)}=V0.
        # s1(V0):-  #sum{V2,V1:el(V1,V2)}=V0,#sum{V2,V1:el(V2,V1)}=V0.
        self.enable_recursion = False
        
        
        # allowed aggregates
        # self.aggregates : 'list[Literal]' = []
        # store the already placed clauses to avoid recomputation
        self.stub_placed_dict : 'dict[str,list[str]]' = {}
        
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
                

    # def __replace_operators(self, body : 'list[str]') -> 'tuple[list[str],bool]':
    def __replace_operators(self, body : 'list[str]') -> 'list[str]':
        '''
        Replaces the placeholder names with the comparison or arithmetic operator.
        The boolean is false if the number of operators is the same as the number
        of atoms in the body, i.e, the clause is not valid (removed).
        '''
        # body = ['__add__(_____,_____,_____)', '__sum(el/2)(_____)', '__min(el/2)(_____)', 's0(_____)']
        # body = ['__add__(_____,_____,_____)', '__sum(el/2,x/1)(_____)','s0(_____)']
        # body = ['__add__(_____,_____,_____)', '__count(el/2)(_____)','s0(_____)']
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
            # aggregates
            elif el.startswith("__sum(") or el.startswith("__count(") or el.startswith("__min(") or el.startswith("__max("):
                # TODO: count non funziona perché è lungo 4 e non 3
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
                if self.unbalanced_aggregates:
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
        
        
        # p = itertools.product(*all_aggr)
        # for el in p:
        #     print('p: ' + str(el))
        # print(all_aggr)
        
        nb = []
        for agg_comb in itertools.product(*all_aggr):
            cb = body_literals[:]
            for agg, index in zip(agg_comb,aggregates_indexes):
                # print(f"agg: {agg}")
                cb[index] = agg
            # print(cb)
            nb.append(cb)
        
        # self.unbalanced_aggregates = True
        # if len(all_aggr) > 0 and self.unbalanced_aggregates:
        #     # for pair in a
        #     nb = body_literals
        #     print(nb)
        # print(body_literals)
        # return body_literals #, operators_count != len(body)
        return nb #, operators_count != len(body)
    

    def __define_distribution_atoms(
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
        to_find_max_number : bool = False,
        aggregates : 'list[AggregateElement]' = [],
        pos_arithm : 'list[list[int]]' = [],
        pos_comparison : 'list[list[int]]' = [],
        same_atoms : 'list[str]' = [],
        arity_same_atoms : int = 0
        ) -> str:
        '''
        Generate an ASP program to fill the holes in rules.
        to_find_max_number adds some rules to maximize the number
        of clauses. In this way we find the maximum number according
        to the constraints and avoid the generation of unused rules 
        to compute the possible choices.
        '''
        
        # generate all the combinations of variables and positions
        s = "% generate all the combinations of variables and positions\n"
        s += f"var(0..{n_variables - 1}).\n"
        s += f"pos(0..{n_positions - 1}).\n"
        
        # last index for the variable in the head
        s += "\n% last index for the variable in the head\n"
        s += f"last_index_var_in_head({n_vars_in_head - 1}).\n"

        # exactly one varible per position
        s += "\n% exactly one varible per position\n"
        s += "1{var_pos(Var,Pos) : var(Var)}1:- pos(Pos).\n"
        
        # only, safe variables (a variable in the head must appear in the body)
        s += "\n% only, safe variables (a variable in the head must appear in the body)\n"
        # s += "\n% excluded positions: the ones involved in aggregates and comparison operators\n"
        # if len(aggregates) > 0:
        #     s += "\nexclude_pos(P):- aggregate_term_position(_,P).\n"
        #     s += "\nexclude_pos(P):- aggregate_atom_position(_,P).\n"
        # if len(pos_comparison) > 0:
        #     s += "\nexclude_pos(P):- comparison_term_position(_,P).\n"
        # if len(pos_arithm) > 0:
        #     # TODO: controllare che sia lo stesso nome
        #     s += "\nexclude_pos(P):- arithm_term_position(_,P).\n"

        if len(aggregates) > 0 or len(pos_comparison) > 0 or len(pos_arithm) > 0:
            s += """
                v_body(V,P):-
                    var_pos(V,P), 
                    P > VHI, 
                    last_index_var_in_head(VHI).
                
                % placeholders to suppress warnings
                aggregate_term_position(-1,-1).
                v_body_atp(V,P):-
                    var_pos(V,P), 
                    P > VHI, 
                    last_index_var_in_head(VHI),
                    aggregate_term_position(_,P).

                aggregate_atom_position(-2,-2).
                v_body_aap(V,P):-
                    var_pos(V,P), 
                    P > VHI, 
                    last_index_var_in_head(VHI),
                    aggregate_atom_position(_,P).

                arithm_term_position(-3,-3).
                v_body_arp(V,P):-
                    var_pos(V,P), 
                    P > VHI, 
                    last_index_var_in_head(VHI),
                    arithm_term_position(_,P).
                
                comparison_term_position(-4,-4).
                v_body_ctp(V,P):-
                    var_pos(V,P), 
                    P > VHI, 
                    last_index_var_in_head(VHI),
                    comparison_term_position(_,P).
                

                cv_body(Var,C):-
                    CT = #count{P : v_body(Var,P)},
                    CATP = #count{P : v_body_atp(Var,P)},
                    CAAP = #count{P : v_body_aap(Var,P)},
                    CARP = #count{P : v_body_arp(Var,P)},
                    CCOMP = #count{P : v_body_ctp(Var,P)},
                    var(Var),          
                    C = CT - CATP - CAAP - CARP - CCOMP.
            """
        else:
            # s += "cv_body(Var, C):- C = #count{Pos : var_pos(Var,Pos), Pos > VHI}, var(Var), last_index_var_in_head(VHI).
            s += '''
                v_in_head(V):- last_index_var_in_head(I), var_pos(V,P), P <= I.
                v_in_body(V):- last_index_var_in_head(I), var_pos(V,P), P > I.
                :- v_in_head(V), not v_in_body(V).
            '''

        if len(aggregates) > 0 or len(pos_comparison) > 0 or len(pos_arithm) > 0:
            # old version to improve for aggregates
            s += "cv_head(Var, C):- C = #count{Pos : var_pos(Var,Pos), Pos <= VHI}, var(Var), last_index_var_in_head(VHI).\n"
            s += ":- cv_head(Var,CH), cv_body(Var,0), CH > 0.\n"
        
        # no variable should appear only once
        s += '''
            % no variable should appear only once
            at_least_twice(V):- var_pos(V,P0), var_pos(V,P1), P0 != P1.
            :- var_pos(V,_), not at_least_twice(V).
            '''
        # do not use variables of index k+1 if k is not used
        s += "\n% do not use variables of index k+1 if k is not used\n"
        # old
        # s += ":- var(Var0), var(Var1), Var0 < Var1, #count{Pos : var_pos(Var0,Pos)} = 0,  #count{Pos : var_pos(Var1,Pos)} > 0.\n"
        # wrong
        # s += ":- var_pos(V0,_), var_pos(V1,_), var_pos(V2,_), V0 < V1, V1 < V2.\n"
        s += ":- var(Var0), var(Var1), Var0 < Var1, not var_pos(Var0,_), var_pos(Var1,_)."
        
        # fix variable 0 in position 0 to remove some symmetries
        s += "\n% fix variable 0 in position 0 to remove some symmetries\n"
        s += ":- not var_pos(0,0).\n"
        
        # to keep the compatibility with the previous version
        for i in range(n_variables):
            s += f"v{i}(I):- var_pos({i},I).\n"
            s += f"#show v{i}/1.\n"
        
        # s += "\n#show var_pos/2."
        
        # additional constraints coming from aggregates:
        # [Term: 1 - Atoms: 2 - Eq: 3] # the number denotes positions
        # X, Y : a(X,Y)
        # term : atom
        # i) all the terms must be different
        # ii) all the terms must appear in literals
        # iiiii) the result of the aggregate must be used: implicit in the constraint
        # imposing that no variables should appear only once
        
        if len(aggregates) > 0:
            s += "\n% constraints for aggregates\n"
            s += f"aggregate(0..{len(aggregates) - 1}).\n"
            for index, aggregate in enumerate(aggregates):
                last_i = -1
                for t in aggregate.position_var_terms:
                    s += f"aggregate_term_position({index},{t}).\n"
                for a in aggregate.position_var_atom:
                    s += f"aggregate_atom_position({index},{a}).\n"
                    last_i = aggregate.position_var_atom[len(aggregate.position_var_atom) - 1]
                s += f"aggregate_result_position({index},{last_i + 1}).\n"
        

            # i) all the terms must be different
            # old with aggregates 
            # s += ":- aggregate(A), #count{X : var_in_term_agg(A, X)} = CVT, CAT = #count{X : aggregate_term_position(A,X)}, CVT != CAT.\n"
            s += '''
            % i) all the terms must be different
            :- var_pos(V0,P0), 
                var_pos(V1,P1), 
                P0 != P1, 
                aggregate_term_position(A,P0), 
                aggregate_term_position(A,P1),
                V0 = V1.
            '''
            
            # ii) all the terms must appear in literals, i.e., remove #count{X:a(Y)}
            s += '''
            % ii) all the terms must appear in literals
            var_in_term_agg(A,V):- aggregate_term_position(A,VPos), var_pos(V,VPos).
            var_in_atom_agg(A,V):- aggregate_atom_position(A,VPos), var_pos(V,VPos).
            :- var_in_term_agg(A,V), not var_in_atom_agg(A,V).
            '''
            
            # iii) no global variables in tuple of aggregate elements: terms cannot appear elsewhere
            # apart from other terms
            if not self.unbalanced_aggregates:
                # TODO: secondo me basta solo uno dei due vincoli ma singolarmente non funzionano
                s += "\n% no global variables in tuple of aggregate elements\n"
                # s += "not_in_aggregate_term(V):- aggregate(A), var(V), not var_in_term_agg(A,V).\n"
                # s += ":- var(V), aggregate(A), aggregate_term_position(A,V), not_in_aggregate_term(V).\n"
                # s += "not_agg_pos(P):- pos(P), not aggregate_term_position(_,P), not aggregate_atom_position(_,P).\n"
                # s += ":- var(V), var_pos(V,P), var_in_term_agg(A,V), aggregate(A), not_agg_pos(P).\n"
                # qui escludo la possibilità di avere #count{X : a(X,Y)} = C, g(Y).
                s += "not_agg_pos(P):- pos(P), not aggregate_term_position(_,P), not aggregate_atom_position(_,P).\n"
                s += ":- not_agg_pos(P), var_pos(V,P), aggregate_term_position(_,PosTermAgg), var_pos(V,PosTermAgg).\n"

        if len(pos_arithm) > 0:
            # the variables involved in arithmetic operators must be already defined
            # in another term
            # TODO: the same as comparison
            s += "\n% constraints for arithm operators\n"
            s += f"arithm(0..{len(pos_arithm) - 1}).\n"
            for index, el in enumerate(pos_arithm):
                for ii in range(0,len(el)):
                    # if index > 0 and (index + 1) % 3 != 0:
                    if (ii + 1) % 3 != 0:
                        # since in A + B = C, C can appear in the head
                        s += f"arithm_term_position({index},{el[ii]}).\n"
                    else:
                        s += f"result_term_position({index},{el[ii]}).\n"
                    s += f"all_arithm_term_position({index},{el[ii]}).\n"

            # variables in arithm should appear elsewhere and not only in arithm
            s += '''
            var_not_in_arithm(Var):-
                var_pos(Var,Pos),
                not all_arithm_term_position(_,Pos).
  
            :- var_pos(Var,Pos), all_arithm_term_position(_,Pos), not var_not_in_arithm(Var).
            '''
            
            # questo sotto taglia di più ma non va bene (inoltre è orrendo) 
            # però talvolta è interessante, vedi con esempio subset sum double
            # # get the variables involved in arithm operators
            # s += "\n% get the variables involved in arithm operators\n"
            # s += "in_arithm_and_not(Var):- \
            #     arithm_term_position(IndexArithm,Position0),\
            #     var_pos(Var, Position0),\
            #     var_pos(Var, Position1),\
            #     Position0 != Position1.\n"
            
            # # impose that the varibles in arithm operators appear elsewhere
            # s += "\n% impose that the varibles in arithm operators appear elsewhere\n"
            # s += ":- #count{Var : in_arithm_and_not(Var)} = VP,\
            #         #count{P : arithm_term_position(I,P),arithm(I)} = NP,\
            #         NP != VP.\n"
            
            # impose that arithm operators must have different variables
            # involved (i.e., V1 + V0 = V1 is not ok)
            s += "\n% impose that arithm operators must have different variables\n" 
            s += """
            :-  arithm_term_position(C,P0),
                result_term_position(C,P1),
                P0 != P1,
                var_pos(Var0,P0),
                var_pos(Var1,P1),
                Var0 == Var1.
            """
        if len(pos_comparison) > 0:
            s += "\n% constraints for comparison operators\n"
            s += f"comparison(0..{len(pos_comparison) - 1}).\n"
            for index, el in enumerate(pos_comparison):
                for v in el:
                    s += f"comparison_term_position({index},{v}).\n"

            
            # variables in comparison should appear elsewhere and not only in comparison
            s += '''
            var_not_in_comparison(Var):-
                var_pos(Var,Pos),
                not comparison_term_position(_,Pos).
  
            :- var_pos(Var,Pos), comparison_term_position(_,Pos), not var_not_in_comparison(Var).
            '''
            # some sopra, forse taglia troppo
            # # get the variables involved in comparison operators
            # s += "\n% get the variables involved in comparison operators\n"
            # s += "in_comparison_and_not(Var):- comparison(IndexComparison),\
            #     comparison_term_position(IndexComparison,Position0),\
            #     var_pos(Var, Position0),\
            #     var_pos(Var, Position1),\
            #     Position0 != Position1.\n"
            
            # # impose that the varibles in comparison operators appear elsewhere
            # s += "\n% impose that the varibles in comparison operators appear elsewhere\n"
            # s += ":- #count{Var : in_comparison_and_not(Var)} = VP,\
            #         #count{P : comparison_term_position(I,P),comparison(I)} = NP,\
            #         NP != VP.\n"

            # impose that comparison operators must have different variables
            # involved (i.e., V1 > V1 is not ok)
            s += "\n% impose that comparison operators must have different variables\n"
            s += ":- comparison_term_position(C,P0),\
                    comparison_term_position(C,P1),\
                    P0 != P1,\
                    var_pos(Var0,P0),\
                    var_pos(Var1,P1),\
                    Var0 == Var1.\n"
            
            s += '''
            % there should be at least one atom in the rule
            atom_pos(Pos):-
                pos(Pos),
                not comparison_term_position(_,Pos),
                not all_arithm_term_position(_,Pos).
            :- not atom_pos(_).
            '''
            # alternative to :- not atom_pos(_).
            # :- #count{P : atom_pos(P)} = CP, CP = 0.
        
        equal_1 = '''
        equal:-
            same1(Id,P0),
            same1(Id,P1),
            var_pos(V0,P0),
            var_pos(V1,P1),
            P0 != P1,
            V0 = V1.
        '''
        equal_2 = '''
        equal:-
            same2(Id,PA0,PA1),
            same2(Id,PB0,PB1),
            var_pos(VA0,PA0),
            var_pos(VA1,PA1),
            var_pos(VB0,PB0),
            var_pos(VB1,PB1),
            PA0 != PB0,
            PA1 != PB1,
            VA0 = VB0,
            VA1 = VB1.
        '''
        l_eq = [equal_1,equal_2]
        # add the constraints to prevent two equal atoms in a solution
        if arity_same_atoms > 0:
            for i in range(1, arity_same_atoms + 1):
                if i < 3: # for the moment only arity 1 and 2, later add arity 3+
                    s += l_eq[i - 1]

            for v in same_atoms:
                s += v + '\n'
            
            s += ":- equal."
        
        # print(s)
        # sys.exit()
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
        
        for index, clause in enumerate(sampled_clauses):
            if clause in self.stub_placed_dict:
                # print("FOUND")
                placed_list.append(self.stub_placed_dict[clause])
                if self.verbose > 1:
                    for c in self.stub_placed_dict[clause]:
                        print(c)
            else:
                # print("FISSATO")
                # clause = ":- can(_____,_____),can(_____,_____)."
                if self.verbose >= 1:
                    print(f"({index}/{len(sampled_clauses) - 1}) Placing variables for {clause}")
                # TODO: miglioria. Qui i valori sono sempre gli stessi,
                # Per esempio: :- a(_), b(_) e :- a(_), c(_) hanno le
                # stesse possibili combinazioni quindi posso evitare di
                # calcolarle nuovamente. Stesso numero di variabili e di
                # posizioni
                r = self.place_variables_clause(clause)
                # print('PLACED')
                # for a in r:
                #     print(a)
                if len(r) > 0: # and not (r in placed_list):
                    r.sort()
                    valid_rules : 'list[str]' = []
                    pruned_count = 0
                    for rl in r:
                        if utils.is_valid_rule(rl):
                            valid_rules.append(rl)
                            if self.verbose > 1:
                                print(f"Valid: {rl}")
                        else:
                            pruned_count += 1
                            if self.verbose > 1:
                                print(f"Pruned: {rl}")
                    if self.verbose > 1:
                        print(f"Valid / Total = {len(r) - pruned_count} / {len(r)} = {(len(r) - pruned_count) / len(r)}")
                    if len(valid_rules) > 0:
                        self.stub_placed_dict[clause] = valid_rules
                        placed_list.append(valid_rules)
                else:
                    if self.verbose >= 1:
                        print("No possible placements.")

            # sys.exit()
        return placed_list


    def place_variables_clause(self, sampled_stub : str) -> 'list[str]':
        '''
        Replaces the _____ with the variables in the clause.
        This now works with only 1 clause
        '''
        # print("-- FIXED STUB ")
        # sampled_stub = ":- _____+_____=_____,_____-_____=_____,_____<_____,_____==_____,q(_____,_____)."
        # sampled_stub = ":- _____+_____=_____,_____==_____,q(_____,_____)." # qui attenzione che se ho > o < invece di == allora è unsafe
        # sampled_stub = ":- _____+_____=_____,q(_____,_____)."
        # sampled_stub = ":- _____==_____,q(_____,_____)."
        # sampled_stub = ":- _____-_____=_____,_____<_____."
        # sampled_stub = ":- _____>_____,q(_____,_____)."
        # sampled_stub = ":- q(_____,_____),q(_____,_____),a(_____),a(_____)."
        # sampled_stub = "sp(_____,_____):- #sum{_____,_____:p(_____,_____)}=_____, partition(_____)."
        # sampled_stub = ":- _____-_____=_____,_____<=_____,hd(_____),pos(_____),sd(_____),v1(_____,_____)."
        # sampled_stub = ":- #sum{_____,_____:d(_____,_____)}=_____,_____-_____=_____,_____>=_____."
        # sampled_stub = "s0(_____):- #sum{_____,_____:el(_____,_____)}=_____,#sum{_____,_____:el(_____,_____)}=_____."
        # sampled_stub = "s1(_____):- #sum{_____,_____:el(_____,_____)}=_____,#sum{_____,_____:el(_____,_____)}=_____,s1(_____)."
        # sampled_stub = "odd(_____):- even(_____), prev(_____,_____)."
        
        # sampled_stub = "a(_____):- _____ + _____ = _____, b(_____), c(_____)."
        # sampled_stub = ":- #sum{ _____,_____ : el  ( _____,_____ )} = _____,#sum{ _____,_____ : el  ( _____,_____ )} = _____,s0(_____),s1(_____)."
        
        # sampled_stub = "s(_____,_____):- g(_____), h(_____,_____), i(_____)."
        # sampled_stub = "ok(_____):- #sum{ _____,_____ : el  ( _____,_____ )} = _____,#sum{ _____,_____ : el  ( _____,_____ )} = _____,_____ + _____ = _____."
        # sampled_stub = ":- s(_____), s(_____), s(_____), _____ + _____ = _____."
        # sampled_stub = "s(_____):- #sum{ _____ : el  ( _____ )} = _____, _____ != _____."
        # sampled_stub = ":- #sum{ _____ : el  ( _____ )} = _____,_____ != _____,s(_____)."
        # sampled_stub = "g(_____):- #sum{ _____, _____ : a  ( _____, _____ )} = _____."
        # sampled_stub = "g(_____):- #sum{ _____ : a  ( _____ )} = _____, #sum{ _____ : a  ( _____ )} = _____."
        # sampled_stub = "g(_____):- #sum{ _____ : a  ( _____ )} = _____."
        # sampled_stub = "count_row(_____,_____):- _____ = #count{_____ : x(_____,_____,_____), cell(_____)}, cell(_____)."
        # sampled_stub = ":- in(_____), in(_____), v(_____), v(_____), _____!=_____, not e(_____,_____), not e(_____,_____)."
        res : 'list[str]' = []
        # number of positions to insert the variables
        n_positions : int = sampled_stub.count('_' * UNDERSCORE_SIZE)
        # number of variables to insert
        # rv = random.randint(1, self.max_variables)
        rv = self.max_variables # deterministic is better
        if n_positions <= 2:
            n_variables = 1
        else:
            n_variables = rv
        
        # print("--- STUB ---")
        if self.verbose > 1:
            print(f"Placing for the stub: {sampled_stub}")
        # print("TODO: introdurre ulteriori vincoli per aggregati e arithm")
        # number of variables in the head
        
        # sampled_stub = ":- #sum{ _____,_____ : a  ( _____,_____ )} = _____,a(_____),a(_____)."
        n_vars_in_head = sampled_stub.split(':-')[0].count('_' * UNDERSCORE_SIZE)
        # print(n_positions, n_variables, n_vars_in_head)
        aggregates : 'list[AggregateElement]' = []
        pos_arithm : 'list[list[int]]' = []
        pos_comparison : 'list[list[int]]' = []

        if '#' in sampled_stub:
            aggregates = utils.get_aggregates(sampled_stub)
            # additional_constraints = utils.get_constraint_from_aggregates(aggregates)
            # print(aggregates)
            # sys.exit()
            # pass
        if utils.contains_arithm(sampled_stub) or utils.contains_comparison(sampled_stub):
            pos_arithm, pos_comparison = utils.get_arithm_or_comparison_position(sampled_stub)
            # print(pos_arithm)
            # print(pos_comparison)
            # per i comparison, i due valori devono apparire da altre parti
            # sys.exit()

        # TODO: migliorie
        # 1) la variabile coinvolta in una ricorsione deve variare
        # es: a(X):- b(X), a(X).
        # 2) no variabili unsafe (quando c'è negazione)   
        if not(n_positions == 1 and n_variables == 1 and n_vars_in_head == 0):
            # the if is false if there is a constraint :- a(_).
            if self.enable_find_max_vars_stub:
                ### add the optimization part to find the max number of vars
                # TODO: test whether is hella slow - NON USATO QUESTO
                asp_p = self.generate_asp_program_for_combinations(
                    n_positions,
                    n_variables,
                    n_vars_in_head,
                    True,
                    aggregates,
                    pos_arithm=pos_arithm,
                    pos_comparison=pos_comparison
                )

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
            
            same_atoms, arity_same = utils.get_same_atoms(sampled_stub)
            
            asp_p = self.generate_asp_program_for_combinations(
                n_positions,
                n_variables,
                n_vars_in_head,
                False,
                aggregates,
                pos_arithm=pos_arithm,
                pos_comparison=pos_comparison,
                same_atoms=same_atoms,
                arity_same_atoms=arity_same           
            )

            # print(asp_p)
            # print(asp_p)
            # sys.exit()

            # generates the clause to fill
            for el in range(0, sampled_stub.count('_'*UNDERSCORE_SIZE)):
                sampled_stub = re.sub('_'*UNDERSCORE_SIZE, f"_v{el:02d}_", sampled_stub, count=1)

            # print('sampled stub')
            # print(sampled_stub)

            if self.find_all_possible_pos_for_vars_one_shot:
                asp_interface = ClingoInterface([asp_p], ["0"])
                ctl = asp_interface.init_clingo_ctl()      

                answer_sets : 'list[str]' = []
                answer_sets_in_list : 'list[list[list[int]]]' = []
                if self.verbose > 1:
                    print("Generating variables placements")
                with ctl.solve(yield_=True) as handle:  # type: ignore
                    for m in handle:  # type: ignore
                        # print(str(m))
                        a = str(m).split(' ')
                        a.sort()
                        a = ' '.join(a)
                        answer_sets.append(a)
                        answer_sets_in_list.append(utils.from_as_to_list(str(m)))
                        # res.append(self.reconstruct_clause(str(m), sampled_stub))
                if self.verbose > 1:
                    print("Removing symmetries")
                # print("start")
                # remove duplicated: sort the list
                answer_sets_in_list.sort()
                # remove duplicates
                r = list(k for k,_ in itertools.groupby(answer_sets_in_list))
                # reconstruct the clause
                for rt in r:
                    res.append(self.reconstruct_clause(utils.from_list_to_as(rt), sampled_stub))
                return res
                
                # old version very slow - with the new one there is no need to generate
                # the permutations
                # # print(la)
                # # if len(aggregates) > 0:
                # #     print(answer_sets)
                # # print(len(answer_sets))
                # # generate all the combinations and prune the symmetric
                # lo : 'list[str]' = copy.deepcopy(answer_sets)
                # # for i in range(0, len(answer_sets)):
                # removed : 'list[str]' = []
                # for answer in answer_sets:
                #     symmetric_as = utils.find_symmetric_answer_sets(answer)
                #     current = symmetric_as[0]
                #     symm = symmetric_as[1:]
                #     if len(symmetric_as) > 0:
                #         # print(f"AS: {answer}, symmetric: {symmetric_as}")
                #         # print(symmetric_as)
                #         if current not in removed:
                #             # print("Not in")
                #             # print(symmetric_as)
                #             for s in symm:
                #                 # print(s)
                #                 s = s.split(' ')
                #                 s.sort()
                #                 s = ' '.join(s)
                #                 removed.append(s)
                #                 if s in lo:
                #                     # this because the answer set programs already
                #                     # removes some symmetries
                #                     lo.remove(s)

                # for a in lo:
                #     res.append(self.reconstruct_clause(a, sampled_stub))
           
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
        
        # # Remove solutions that have the same atom repeated twice
        # # initial setup to find duplicates
        # # print('pre res -- non va bene perché con aggregati non funziona')
        # # print(res)
        # temp_l = copy.deepcopy(res)
        # for i in range(0, len(temp_l)):
        #     temp_l[i] = temp_l[i].replace('not ', 'not_')
        #     temp_l[i] = temp_l[i].replace(' ', '')
        #     temp_l[i] = temp_l[i].replace('),',') ').replace(').',')')
            
        #     # temp_l[i] = temp_l[i].replace('  ', ' ')
        
        # # find the index of the duplicates
        # dup : 'list[int]' = []
        # for i in range(0, len(temp_l)):
        #     tmp = temp_l[i].split(' ')
        #     # print(tmp)
        #     # print(set(tmp))
        #     if len(tmp) != len(set(tmp)):
        #         dup.append(i)
        
        # print(dup)
        # print('temp l')
        # print(temp_l)
        
        # # remove the duplicates from the original list
        # dup.reverse()
        # for idx in dup:
        #     del res[idx]
        
        # # print('post res')
        # # print(res)
        # # find other symmetric elements, i.e., that have the same atoms but in different order
        # temp_l = copy.deepcopy(res)
        # for i in range(0, len(temp_l)):
        #     # print(get_atoms(temp_l[i]))
        #     # print(temp_l[i])
        #     head = temp_l[i].split(':-')[0]
        #     # head = utils.get_atoms(temp_l[i].split(':-')[0])
        #     body = temp_l[i].split(':-')[1].lstrip()
        #     # print('body')
        #     # print(body)
        #     # body = utils.get_atoms(temp_l[i].split(':-')[1])
        #     body_t = ' '.join(sorted(body.replace('not ', 'not_').replace('),',') ').replace(').',')').split(' ')))
        #     head_t = ' '.join(sorted(head.replace('not ', 'not_').replace('),',') ').replace(').',')').split(' ')))
        #     # print(head_t)
        #     # print(body_t)
        #     # temp_l[i] = ';'.join(sorted(head)) + ':- ' + ','.join(sorted(body)) + '.'
        #     # temp_l[i] = ' '.join(sorted(temp_l[i].replace('not ', 'not_').replace('),',')').replace(').',')').split(' ')))
        #     temp_l[i] = head_t + ':- ' + body_t
        # temp_l.sort()

        # # for el in temp_l:
        # #     print(el)
        
        # s = list(set(temp_l))
        # for i in range(0, len(s)):
        #     s[i] = ', '.join(s[i].replace('  ',' ').split(' ')).replace(',,',',').replace(':-,',':-').replace('not_', 'not ') + ('.' if not s[i].endswith('.') else '')
        # res = s


        # print(len(temp_l))
        # print(len(s))
        # for el in res:
        #     print(el)
        # # print(res)

        # if len(aggregates) > 0 or len(pos_arithm) > 0 or len(pos_comparison) > 0:
        #     print(len(res))

        
        # print(res)
        # print(f"len(res): {len(res)}")
        # print(res)

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
        stop = (random.random() > self.prob_increase_level) if head else False
        max_depth_head = self.disjunctive_head_length
        
        while (not stop) and (depth < self.max_depth) and (max_depth_head > 0):
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
                    stop = (random.random() > self.prob_increase_level)
                depth += 1
            if head:
                max_depth_head -= 1
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
        # not_merged_clauses = []
        
        for _ in range(0, how_many):
            body : 'list[str]' = []
            head : 'list[str]' = []
            
            if len(self.head_atoms) > 0:
                # if self.verbose:
                #     print("No modeh specified")
                head = self.sample_literals_list(copy.deepcopy(self.head_atoms), True) # true allows constraints
                if len(head) == 0:
                    self.body_constraint = True
                else:
                    self.body_constraint = False
            
            # decrease the depth since we already sampled atoms for the head
            self.max_depth -= len(head)
            
            # print(self.body_literals)
            # sys.exit()
            body = self.sample_literals_list(copy.deepcopy(self.body_literals))
            
            # replace __lt__, __gt__, __eq__, __neq__, __add__, __sub__, __mul__
            # body, is_valid = self.__replace_operators(body)
            body = self.__replace_operators(body)
            
            is_valid = True
            if is_valid and self.enable_recursion is False:
                for b in body:
                    subs_h = set(head).issubset(set(b)) and len(set(head)) > 0
                    subs_b = set(b).issubset(set(head)) and len(set(b)) > 0
                    is_valid = not (subs_h or subs_b)
                    if is_valid:
                        clauses.append(';'.join(sorted(head)) + ":- " + ','.join(sorted(b)) + '.')
                        # not_merged_clauses.append([sorted(head),sorted(b)])
            # TODO: and what happens with enable resursion True?
            
            self.max_depth = original_depth
        # print(not_merged_clauses)
        # print(clauses)
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
