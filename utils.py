import itertools
import sys

from clingo import ast
from clingo import Control

### Print utilities
YELLOW = '\33[93m'
RED = '\033[91m'
END = '\033[0m'

class AggregateElement:
    def __init__(self, position_var_terms : 'list[int]', position_var_atom : 'list[int]', var_eq : int) -> None:
        self.position_var_terms = position_var_terms
        self.position_var_atom = position_var_atom
        self.var_eq = var_eq # for the variable after the = sign
    
    def __str__(self) -> str:
        return 'Term: ' + ' '.join([str(a) for a in self.position_var_terms]) +\
                ' - Atoms: ' + ' '.join([str(a) for a in self.position_var_atom]) +\
                f' - Eq: {self.var_eq}'

    def __repr__(self) -> str:
        return self.__str__()

    def __eq__(self, __value: object) -> bool:
        return self.position_var_atom == __value.position_var_atom and self.var_eq == __value.var_eq and self.position_var_terms == __value.position_var_terms 


class RuleCallback:
    '''
    Used while parsing the AST with clingo: process
    is used as callback function to store values
    '''
    def __init__(self) -> None:
        self.head = []
        self.body = []
    
    def process(self, stm):
        # if "body" in stm.child_keys:
        # print(stm.child_keys)
        # print(stm)
        # print(stm.keys())

        if "body" in stm.child_keys:
            bl = [str(lit).replace(' ','') for lit in stm.body]
            self.body = bl
        if "head" in stm.child_keys:
            # print(stm.head)
            self.head = str(stm.head).replace(' ','').split(';')
                # print(h)
            # print(str(lit) for lit in stm.head)


class CheckSanityRulesCallback:
    '''
    Wrapper to check unsafe rules
    '''
    def __init__(self) -> None:
        self.sound_rule : bool = False
    
    def sink(self, x, y):
        # global for the error: info: global variable in tuple of aggregate element
        self.sound_rule = ("unsafe" in y) or ("global" in y)
        

def wrapper_exit_callback(x, y):
    '''
    Clingo callback: exit when there is an error
    '''
    if "error" in y:
        print(x)
        print(y)
        sys.exit()


def print_error_and_exit(message : str):
    '''
    Prints the error message 'message' and exits.
    '''
    print(RED + "Error: " + message + END)
    sys.exit(-1)


def print_warning(message : str):
    '''
    Prints the warning message 'message'.
    '''
    print(YELLOW + "Warning: " + message + END)
###

def get_part_of_iter(p, size : int):
    '''
    Get the first size elements of the iterable p.
    Used since it is fastest than list(p), since it avoids
    unpacking all the elements.
    '''
    lp = []
    while p and size > 0:
        try:
            lp.append(list(next(p)))
        except:
            break
        size -= 1
    return lp


def find_symmetric_answer_sets(current_as : str) -> 'list[str]':
    '''
    Given an answer set current_as returns all the 
    symmetric solutions, i.e., all the ones that have
    another permutation of the same variables.
    '''
    i = 0
    while True:
        # count the used variables
        if not f"v{i}" in current_as:
            break
        i += 1
        
    n_vars = i - 1

    l_vars = [i for i in range(n_vars + 1)]
    l_vars_name = ["v" + str(a) for a in l_vars]

    # this is n! # COMPLEX 
    perm = itertools.permutations(l_vars)
    # TODO: is it possible to write an ASP rule to prune the permutations
    # instead of adding a set of constraints? This would be much faster.

    perms : 'list[str]' = []
    for p in perm:
        lc = current_as
        l1 = ["v_" + str(a) for a in p]
        for f, r in zip(l_vars_name, l1):
            lc = lc.replace(f, r)
        lc = lc.replace('_','')
        perms.append(lc)

    # print(f"--- Permutation {current_as} {l_vars} ---")
    # print(perms)
    return perms



def get_atoms(clause: str) -> 'list[str]':
    '''
    Get the atoms from a clause.
    '''
    r = RuleCallback()
    ast.parse_string(clause, r.process)
    return r.head + r.body


def get_v0_v1_v2_arithm(rule : str, p : int) -> 'tuple[str,str,str]':
    '''
    From V0+V1=V2 returns V0, V1, and V2
    '''
    v0 = rule[p-2:p]
    v1 = rule[p+1:p+3]
    v2 = rule[p+4:p+6]
    return v0 ,v1, v2


def get_v0_v1_comparison(rule : str, p : int, incr : int) -> 'tuple[str,str]':
    '''
    From V0>V1 returns V0 and V1
    Incr is 1 if the operator has 2 elements (>=,<=,==,!=)
    '''
    v0 = rule[p-2:p]
    v1 = rule[p+incr+1:p+incr+3]
    return v0, v1


def is_valid_arithm_rule(rule : str) -> bool:
    '''
    Hardcoded rules to remove arithm nonsense.
    '''
    arithm = ['+','-','*','/']
    rule = rule.replace(' ','')
    for ch in arithm:
        pos = [pos for pos, char in enumerate(rule) if char == ch]
        if len(pos) > 0:
            for p in pos:
                v0, v1, v2 = get_v0_v1_v2_arithm(rule,p)
                if v0 == v1 or v0 == v2 or v1 == v2:
                    return False
    return True


def is_valid_comparison_rule(rule : str) -> bool:
    '''
    Hardcoded rules to remove comparison nonsense.
    TODO: check this, since the ASP program should already prune this.
    '''
    comp_2 = ['<=','>=',"!=","=="]
    rule = rule.replace(' ','')
    for ch in comp_2:
        pos = [i for i in range(len(rule)) if rule.startswith(ch, i)]
        if len(pos) > 0:
            for p in pos:
                v0, v1 = get_v0_v1_comparison(rule, p, 1)
                if v0 == v1:
                    return False
    
    comp_1 = ['<','>']
    for ch in comp_1:
        pos = [pos for pos, char in enumerate(rule) if char == ch]
        if len(pos) > 0:
            for p in pos:
                v0, v1 = get_v0_v1_comparison(rule, p, 0)
                if v0 == v1:
                    return False

    return True


def check_sound(clause : str) -> bool:
    '''
    Returns true if the rule is unsafe.
    '''
    l = CheckSanityRulesCallback()
    ctl = Control(logger=l.sink)
    ctl.add('base', [], clause)
    try:
        ctl.ground([("base", [])])
    except:
        pass

    return l.sound_rule


def is_valid_rule(rule : str) -> bool:
    '''
    Returns true if the rule is valid, i.e., there are no
    two equal atoms. For example: 
    :- blue(V1),blue(V1),e(V0,V0),green(V0). is not valid (blue(V1) repeated), while
    :- blue(V1),blue(V0),e(V0,V1),green(V0). it is
    TODO: this should be done with an ASP constraint instead of generating
    all the rules and then discard the not valid ones.
    '''
    atoms = get_atoms(rule)
    # print(atoms)
    return len(atoms) == len(list(set(atoms))) and is_valid_comparison_rule(rule) and is_valid_arithm_rule(rule) and (not check_sound(rule))


def generate_clauses_for_coverage_interpretations(
    interpretations : 'list[list[str]]',
    positive : bool
    ) -> str:
    '''
    Generates the clauses for the ASP solver to check the coverage.
    '''
    generated_str : str = ""
    suffix : str = "cp" if positive else "cn"
    cl_index = 0
    # print(interpretations)
    for atoms in interpretations:
        # inclusion
        if len(atoms[0]) > 0:
            r = f"{suffix}i({cl_index}):- {','.join(atoms[0].split(' '))}.\n"
            generated_str += r
        
        if len(atoms) > 1:
            # exclusion
            if len(atoms[1]) > 0:
                for atom in atoms[1].split(' '):
                    r = f"{suffix}e({cl_index}):- {atom}.\n"
                    generated_str += r
        
        if len(atoms) > 2:
            # context dependent examples
            if len(atoms[2]) > 0:
                for atom in atoms[2].split(' '):
                    generated_str += atom + '.\n'
        
        cl_index += 1
    generated_str += '\n'
    
    return generated_str
    

def read_popper_format(folder : str):
    # file: bias.pl, bk.pl, exs.pl
    background : 'list[str]' = []
    positive_examples : 'list[list[str]]' = []
    negative_examples : 'list[list[str]]' = []
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
            positive_examples.append([line, "", ""]) # three: included, excluded, context_dependent_example
        elif line.startswith('neg'):
            line = line.split('neg')[1][1:].replace('\n','')[:-2]
            negative_examples.append([line, "", ""])
    
    return background, positive_examples, negative_examples, language_bias_head, language_bias_body


def get_aggregates(clause : str) -> 'list[AggregateElement]':
    '''
    Extracts the variables in the aggregates in the clause
    '''
    # t_1, ..., t_k : \phi()
    # t1, ..., tk are terms
    # \phi is a literal
    # #sum{ _____,_____ : a  ( _____,_____ )} = _____, #sum{ _____,_____ : a  ( _____,_____ )} = _____
    # i need to return, a list of list. Each sublist contains the
    # variables in the terms
    open_brackets = [i for i, ch in enumerate(clause) if ch == '{']
    closed_brackets = [i for i, ch in enumerate(clause) if ch == '}']
    
    aggregates : 'list[AggregateElement]' = []
    
    prev_pos = 0
    prev_count = 0
    for s, e in zip(open_brackets, closed_brackets):
        var_terms = []
        var_atom = []
        current_index = clause[prev_pos : s].count("_____") + prev_count
        aggr = clause[s + 1 : e]
        aggr = aggr.split(':')
        n_terms = aggr[0].count('_____')
        n_var_in_atom = aggr[1].count('_____')
        var_terms = list(range(current_index, n_terms + current_index))
        var_atom = list(range(current_index + n_terms, n_var_in_atom + current_index + n_terms))
        
        # print(aggr)
        # print(f"current index: {current_index}")
        # print(f"var terms: {var_terms}")
        # print(f"var atom: {var_atom}")
        
        prev_pos = e
        prev_count = current_index + n_terms + n_var_in_atom
        
        aggregates.append(AggregateElement(var_terms, var_atom, prev_count))
        
    
    return aggregates

# def get_constraint_from_aggregates(agg_list : 'list[AggregateElement]', n_positions : int):
#     # aggregate, add additional constraints on the variables
#     # #aggr{ Xt1, Xt2, ... : a(X1, X2,...)}
#     # i) all the Xti in the term must be different
#     # ii) a term must appear in th atom
#     # iii) no global variables, i.e., Xti cannot appear elsewhere
#     for agg in agg_list:
        

#     pass


def contains_arithm(stub : str) -> bool:
    return '+' in stub or '-' in stub or '*' in stub or '/' in stub

def contains_comparison(stub : str) -> bool:
    return '>' in stub or '<' in stub or '==' in stub or '!=' in stub

def get_arithm_or_comparison_position(stub : str) -> 'tuple[list[list[int]],list[list[int]]]':
    '''
    Extracts the positions of the variables involved in arithmetic or
    comparison operators.
    '''
    els = stub.replace(' ','').split("_____")
    pos_arithm : 'list[list[int]]' = []
    pos_comparison : 'list[list[int]]' = []
    for index, el in enumerate(els):
        if el == '>' or el == '>=' or el == '<' or el == '=<' or el == '==' or el == '!=':
            pos_comparison.append([index - 1,index])
        
        if el == '+' or el == '-' or el == '*' or el == '/':
            pos_arithm.append([index-1,index,index+1])
    
    return pos_arithm, pos_comparison