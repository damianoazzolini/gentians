import itertools

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

    perms : 'list[str]' = []
    for p in perm:
        lc = current_as
        l1 = ["v_" + str(a) for a in p]
        for f, r in zip(l_vars_name, l1):
            lc = lc.replace(f, r)
        lc = lc.replace('_','')
        perms.append(lc)

    return perms