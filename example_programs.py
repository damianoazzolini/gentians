# Some examples
# https://github.com/metagol/metagol/tree/master/examples
# http://hakank.org/popper/
    

def coin_example():
    # coin example
    # from https://doc.ilasp.com/specification/cdpis.html
    # Expected
    # heads(V1) :- coin(V1), not tails(V1).
    # tails(V1) :- coin(V1), not heads(V1).
    
    background : 'list[str]' = [
        'coin(c1).', 
        'coin(c2).', 
        'coin(c3).'
    ]
    
    # example structure: [Included,Excluded]
    # For positive examples, there should be at least
    # one answer set with all the Included and none of
    # the excluded
    positive_examples : 'list[list[str]]' = [
        ["heads(c1) tails(c2) heads(c3)", "tails(c1) heads(c2) tails(c3)", ""],
        ["heads(c1) heads(c2) tails(c3)", "tails(c1) tails(c2) heads(c3)", ""]
    ]

    
    # positive_examples : 'list[str]' = [
    #     "heads(c1) tails(c2) heads(c3)",
    #     "tails(c1) heads(c2) tails(c3)",
    #     "heads(c1) heads(c2) tails(c3)",
    #     "tails(c1) tails(c2) heads(c3)"
    # ]

    negative_examples : 'list[list[str]]' = []

    language_bias_head : 'list[str]' = [
        'modeh(1, heads(+))',
        'modeh(1, tails(+))'
    ]
    # language_bias_body : 'list[str]' = ['modeb(1, bird(+))', 'modeb(1, ability(+))', 'modeb(*, not can(+,#))']
    language_bias_body : 'list[str]' = [
        'modeb(1, heads(+))', 
        'modeb(1, not heads(+))', 
        'modeb(1, tails(+))',
        'modeb(1, not tails(+))',
        'modeb(1, coin(+))'
    ]
    
    language_bias_aggregates : 'list[str]' = [
        'modeagg(1, #sum)'
    ]

    return background, positive_examples, negative_examples, language_bias_head, language_bias_body

def even_odd_example():
    '''
    # Goal
    even(V0):- odd(V1),prev(V0,V1).
    odd(V0):- even(V1),prev(V0,V1).
    '''
    # even odd example from
    # https://github.com/stassa/louise/blob/master/data/examples/even_odd.pl

    background = [
        'even(0).',
        "prev(1,0).",
        "prev(2,1).",
        "prev(3,2).",
        "prev(4,3)."
    ]
    
    # IMPORTANT: non usare . alla fine senno fallisce tutto
    
    positive_examples = [
        ["odd(1) odd(3) even(2)", "", ""]
    ]
    
    negative_examples = [
        ["even(3)", ""],
        ["even(1)", ""],
        ["odd(2)", ""]
        # "odd(0)"
    ]
    
    language_bias_head = [
        'modeh(1, even(+))',
        'modeh(1, odd(+))'
    ]
    
    language_bias_body = [
        'modeb(1, even(+))', 
        'modeb(1, odd(+))', 
        'modeb(1, prev(+,+))'
    ]
    
    return background, positive_examples, negative_examples, language_bias_head, language_bias_body
    

def animals_bird_example():
    # from https://github.com/logic-and-learning-lab/Popper/tree/main/examples/animals_bird
    background = [
        "feathers(feathers).",
        "scales(scales).",
        "hair(hair).",
        "has_covering(dog,hair).",
        "has_covering(dolphin,none).",
        "has_covering(platypus,hair).",
        "has_covering(bat,hair).",
        "has_covering(trout,none).",
        "has_covering(herring,none).",
        "has_covering(shark,none).",
        "has_covering(eel,none).",
        "has_covering(lizard,scales).",
        "has_covering(crocodile,scales).",
        "has_covering(t_rex,scales).",
        "has_covering(snake,scales).",
        "has_covering(turtle,scales).",
        "has_covering(eagle,feathers).",
        "has_covering(ostrich,feathers).",
        "has_covering(penguin,feathers).",
        "has_milk(dog).",
        "has_milk(cat).",
        "has_milk(dolphin).",
        "has_milk(bat).",
        "has_milk(platypus).",
        "homeothermic(dog).",
        "homeothermic(cat).",
        "homeothermic(dolphin).",
        "homeothermic(platypus).",
        "homeothermic(bat).",
        "homeothermic(eagle).",
        "homeothermic(ostrich).",
        "homeothermic(penguin).",
        "has_eggs(platypus).",
        "has_eggs(trout).",
        "has_eggs(herring).",
        "has_eggs(shark).",
        "has_eggs(eel).",
        "has_eggs(lizard).",
        "has_eggs(crocodile).",
        "has_eggs(t_rex).",
        "has_eggs(snake).",
        "has_eggs(turtle).",
        "has_eggs(eagle).",
        "has_eggs(ostrich).",
        "has_eggs(penguin).",
        "has_gills(trout).",
        "has_gills(herring).",
        "has_gills(shark).",
        "has_gills(eel)."
    ]
    
    # questi devono essere veri tutti nello stesso AS o in AS diversi?
    # direi diversi
    positive_examples = [
        ["bird(eagle)", ""],
        ["bird(ostrich)", ""],
        ["bird(penguin)", ""]
    ]
    
    negative_examples = [
        ["bird(dog)", ""],
        ["bird(dolphin)", ""],
        ["bird(platypus)", ""],
        ["bird(bat)", ""],
        ["bird(trout)", ""],
        ["bird(herring)", ""],
        ["bird(shark)", ""],
        ["bird(eel)", ""],
        ["bird(lizard)", ""],
        ["bird(crocodile)", ""],
        ["bird(t_rex)", ""],
        ["bird(snake)", ""],
        ["bird(turtle)", ""]
    ]
    
    language_bias_head = [
        'modeh(1, bird(+))'
    ]
    
    language_bias_body = [        
        'modeb(1, feathers(+))',
        'modeb(1, scales(+))',
        'modeb(1, hair(+))',
        'modeb(2, has_covering(+,+))',
        'modeb(1, has_milk(+))',
        'modeb(1, homeothermic(+))',
        'modeb(1, has_eggs(+))',
        'modeb(1, has_gills(+))'
    ]
    
    return background, positive_examples, negative_examples, language_bias_head, language_bias_body

def coloring_example():
    '''
    # Original program
    red(X) ; green(X) ; blue(X) :- node(X).
    e(X,Y) :- edge(X,Y).
    e(Y,X) :- edge(Y,X).

    node(1..6).

    edge(1, 2).
    edge(1, 3).
    edge(2, 5).
    edge(2, 6).
    edge(3, 4).
    edge(4, 5).
    edge(5, 6).

    #show red/1.
    #show green/1.
    #show blue/1.
    
    # TO LEARN
    red(X) ; green(X) ; blue(X) :- node(X).
    :- e(X,Y), red(X), red(Y).
    :- e(X,Y), green(X), green(Y).
    :- e(X,Y), blue(X), blue(Y).


    '''
    background = [
        "edge(1, 2).",
        "edge(1, 3).",
        "edge(2, 5).",
        "edge(2, 6).",
        "edge(3, 4).",
        "edge(4, 5).",
        "edge(5, 6).",
        "node(1..6).",
        "e(X,Y) :- edge(X,Y).",
        "e(Y,X) :- edge(Y,X).",
        "node(1..6)."
    ]
    
    # IMPORTANT: non usare . alla fine senno fallisce tutto
    # esempi positivi: lista di stringhe con atomi separati
    # da spazi (stessa struttura di un AS output di clingo). 
    # Ciascuna stringa identifica un insieme di atomi che 
    # devono essere presenti nell'answer set. Per esempio
    # ["odd(1) odd(3) even(2)"] significa che
    # deve esistere almeno 1 answer set tale che tutti e tre
    # gli atomi sopra siano veri nello stesso answer set.
    # Se invece ho ["odd(1)","odd(3)"] ho 2 esempi positivi
    # che impongono che cia sia almeno 1 answer set con odd(1)
    # ed almeno 1 answer set con odd(3). In questo esempio sono
    # equivalenti
    
    positive_examples = [
        ["red(1) blue(2) blue(3) red(4) green(5) red(6)", ""],
        ["red(1) blue(2) green(3) blue(4) green(5) red(6)", ""],
        ["red(1) blue(2) green(3) red(4) green(5) red(6)", ""],
        ["green(1) blue(2) red(3) blue(4) green(5) red(6)", ""],
        ["green(1) blue(2) blue(3) red(4) green(5) red(6)", ""],
        ["red(1) blue(2) green(3) blue(4) red(5) green(6)", ""]
    ]

    # esempi negativi: stessa struttura di quelli positivi.
    # Ciascun esempio negativo
    # ci dice che cosa non deve contenere un AS. Per esempio
    # [ "even(3) even(1) odd(2)" ] dice che non deve
    # esistere un AS che abbia al suo interno tutti e 3 gli atomi.
    negative_examples = [
        ["red(1) red(2)", ""],
        ["red(1) red(3)", ""],
        ["blue(1) blue(2)", ""],
        ["green(3) green(4)", ""]
    ]

    language_bias_head = [
        'modeh(1, red(+))',
        'modeh(1, green(+))',
        'modeh(1, blue(+))'
    ]

    language_bias_body = [
        'modeb(1, e(+, +))', 
        'modeb(2, red(+))', 
        'modeb(2, green(+))',
        'modeb(2, blue(+))',
        'modeb(1, node(+))'
    ]
    
    return background, positive_examples, negative_examples, language_bias_head, language_bias_body


def sudoku():
    '''
    Sudoku example from ILASP
    '''
    background = [
        "cell((1..4,1..4)).",
        "block((X, Y), tl) :- cell((X, Y)), X < 3, Y < 3.",
        "block((X, Y), tr) :- cell((X, Y)), X > 2, Y < 3.",
        "block((X, Y), bl) :- cell((X, Y)), X < 3, Y > 2.",
        "block((X, Y), br) :- cell((X, Y)), X > 2, Y > 2.",
        "same_row((X1,Y),(X2,Y)) :- X1 != X2, cell((X1,Y)), cell((X2, Y)).",
        "same_col((X,Y1),(X,Y2)) :- Y1 != Y2, cell((X,Y1)), cell((X, Y2)).",
        "same_block(C1,C2) :- block(C1, B), block(C2, B), C1 != C2.",
        "1 {value(V1,1);value(V1,2);value(V1,3);value(V1,4) } 1 :- same_block(V2,V1)."
    ]
    
    positive_examples = [
        ["value((1,1),1) value((1,2),2) value((1,3),3) value((1,4),4) value((2,3),2)",
         "value((1,1),2) value((1,1),3) value((1,1),4)"]
    ]
    
    negative_examples = [
        ["value((1,1),1) value((1,3),1)", ""],
        ["value((1,1),1) value((3,1),1)", ""],
        ["value((1,1),1) value((2,2),1)", ""]
    ]
    
    language_bias_head : 'list[str]' = []
    
    language_bias_body = [
        'modeb(2, value(+, +))', 
        'modeb(1, same_row(+, +))', 
        'modeb(1, same_block(+,+))',
        'modeb(1, same_col(+,+))'
        # 'modeb(1, cell(+))'
    ]

    return background, positive_examples, negative_examples, language_bias_head, language_bias_body


def penguin_example():
    '''
    TODO: questo programma non ha soluzione perché imparo solamente
    regole con solo variabili. Questo richiede anche regole con una
    costante.
    
    % Programma
    bird(a).
    bird(b).
    can(a, fly).
    can(b, swim).
    ability(fly).
    ability(swim).

    % penguin(X):- bird(X).
    % This is the solution
    % penguin(X):- bird(X), not can(X, fly).
    % penguin(X):- bird(X), not can(X, swim).
    % penguin(X):- bird(X), not can(X, fly), not can(X, swim).
    '''
    background : 'list[str]' = [
        "bird(a).",
        "bird(b).",
        "can(a, fly).",
        "can(b, swim).",
        "ability(fly).",
        "ability(swim)."
    ]

    positive_examples : 'list[str]' = [
        "penguin(b)"
    ]

    negative_examples : 'list[str]' = [
        "penguin(a)"
    ]

    language_bias_head : 'list[str]' = [
        'modeh(1, penguin(+))'
    ]
    
    # twice by now
    language_bias_body : 'list[str]' = [
        'modeb(2, not can(+,+))',
        'modeb(1, bird(+))',
        'modeb(1, ability(+))'
    ]

    return background, positive_examples, negative_examples, language_bias_head, language_bias_body


def adjacent_to_red_example():
    # from https://github.com/metagol/metagol/blob/master/examples/adjacent-to-red.pl
    # goal target(A) :- edge(A,B),colour(B,C),red(C).
    bg = [
        "edge(a,b).",
        "edge(b,a).",
        "edge(c,d).",
        "edge(c,e).",
        "edge(d,e).",
        "colour(a,red).",
        "colour(b,green).",
        "colour(c,red).",
        "colour(d,red).",
        "colour(e,green).",
        "red(red).",
        "green(green)."
    ]
    
    pe = [
        ["target(b)", ""], 
        ["target(c)", ""]
    ]
    
    ne = [
        ["target(a)", ""], 
        ["target(d)", ""], 
        ["target(e)", ""]
    ]
    
    lbh = ['modeh(1, target(+))']
    
    lbb = [
        'modeb(1, target(+))', 
        'modeb(1, edge(+,+))', 
        'modeb(1, colour(+,+))',
        'modeb(1, red(+))',
        'modeb(1, green(+))'
    ]
    
    return bg, pe, ne, lbh, lbb


def grandparent_example():
    # from metagol
    '''
    % soluzione metagol
    target(A,B):-target_1(A,C),target_1(C,B).
    target_1(A,B):-mother(A,B).
    target_1(A,B):-father(A,B).
    '''
    
    bg = ["mother(i,a).", "mother(c,f).", "mother(c,g).", "mother(f,h).", "father(a,b).", "father(a,c).", "father(b,d).", "father(b,e)."]
    
    pe = [
        ["target(i,b) target(i,c) target(a,d) target(a,e) target(a,f) target(a,g) target(c,h)", ""]
    ]
    
    ne = [
        ["target(a,b)", ""], 
        ["target(b,c)", ""], 
        ["target(c,d)", ""], 
        ["target(d,e)", ""], 
        ["target(e,f)", ""], 
        ["target(f,g)", ""], 
        ["target(g,h)", ""], 
        ["target(h,i)", ""]
    ]
    
    lbh = ['modeh(1, target(+, +))', 'modeh(1, target_1(+, +))']
    
    lbb = [
        'modeb(1, father(+, +))', 
        'modeb(1, mother(+,+))',
        'modeb(1, target_1(+, +))',
        'modeb(1, target_1(+, +))'
    ]
    
    return bg, pe, ne, lbh, lbb
    
def dummy():
    '''
    g(X) :- a(Y), a(Z), X = Y + Z.
    '''
    bg = ["a(1).", "a(2)."]
    
    pe = [
        ["g(3)", ""]
    ]
    
    ne = []
    
    lbh = ['modeh(1, g(+))']
    
    lbb = ['modeb(2, a(+))']
    
    return bg, pe, ne, lbh, lbb
    
# def hamiltonian():
#     '''
#     Goal: learn the rules for hamiltonian graph.
#     '''

#     return bg, pe, ne, lbh, lbb