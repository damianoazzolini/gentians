import itertools
import sys

### Print utilities
YELLOW = '\33[93m'
RED = '\033[91m'
END = '\033[0m'


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
    clause_list = clause.replace(' ','').split(':-')
    head = clause_list[0]
    body = clause_list[1]
    head = head.split(';')
    body = body.split('),')
    body[-1] = body[-1][:-2]
    for i in range(0, len(body)):
        body[i] = body[i] + ')'

    return head + body


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
    return len(atoms) == len(list(set(atoms)))


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
