# Some examples
# https://github.com/metagol/metagol/tree/master/examples
# http://hakank.org/popper/
# https://users.dimi.uniud.it/~agostino.dovier/AIGAMES/DISPENSA.pdf <-- molti interessanti

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


def subset_sum():
    '''
    % Subset sum problem.
    {el(1)}.
    {el(2)}.
    {el(3)}.
    {el(4)}.
    {el(5)}.
    s(S):- S = #sum{X : el(X)}.
    :- s(S), S != 6.
    '''
    bg : 'list[str]' = ["{el(1)}.", "{el(2)}.", "{el(3)}.", "{el(4)}.", "{el(5)}."]

    pe : 'list[list[str]]' = [
        ["s(6)", ""]
    ]

    ne : 'list[list[str]]' = []

    lbh : 'list[str]' = ['modeh(1, s(+))']

    lbb : 'list[str]' = ['modeb(1, s(+))']

    return bg, pe, ne, lbh, lbb


def subset_sum_double():
    '''
    % Double subset sum problem.
    {el(1,2)}.
    {el(2,3)}.
    {el(3,5)}.
    {el(4,1)}.
    {el(5,9)}.
    
    % to learn
    s0(S):- S = #sum{X,Y : el(X,Y)}.
    s1(S):- S = #sum{Y,X : el(X,Y)}.
    ok(X):- s0(X), s1(X).
    #show ok/1.
    % results: ok(8). ok(9).
    '''
    bg : 'list[str]' = [
        "{el(1,2)}.",
        "{el(2,3)}.",
        "{el(3,5)}.",
        "{el(4,1)}.",
        "{el(5,9)}."
    ]

    pe : 'list[list[str]]' = [
        ["ok(0)", ""],
        ["ok(8)", ""],
        ["ok(9)", ""],
    ]

    ne : 'list[list[str]]' = [
        ["ok(1)", ""],
        ["ok(2)", ""],
        ["ok(10)", ""],
    ]

    lbh : 'list[str]' = [
        'modeh(1, ok(+))',
        'modeh(1, s0(+))',
        'modeh(1, s1(+))'
    ]

    lbb : 'list[str]' = [
        'modeb(1, s0(+))',
        'modeb(1, s1(+))'
    ]

    return bg, pe, ne, lbh, lbb


def subset_sum_double_and_sum():
    '''
    % Double subset sum problem.
    {el(1,2)}.
    {el(2,3)}.
    {el(3,5)}.
    {el(4,1)}.
    {el(5,9)}.
    
    % to learn
    ok(S):- S0 = #sum{X,Y : el(X,Y)}, S0 = #sum{Y,X : el(X,Y)}, S = S0 + S0.
    #show ok/1.
    % results: ok(8). ok(9).
    '''
    bg : 'list[str]' = [
        "{el(1,2)}.",
        "{el(2,3)}.",
        "{el(3,5)}.",
        "{el(4,1)}.",
        "{el(5,9)}."
    ]

    pe : 'list[list[str]]' = [
        ["ok(0)", ""],
        ["ok(16)", ""],
        ["ok(18)", ""],
    ]

    ne : 'list[list[str]]' = [
        ["ok(1)", ""],
        ["ok(2)", ""],
        ["ok(10)", ""],
    ]

    lbh : 'list[str]' = [
        'modeh(1, ok(+))',
        'modeh(1, s0(+))',
        'modeh(1, s1(+))'
    ]

    lbb : 'list[str]' = [
        'modeb(1, s0(+))',
        'modeb(1, s1(+))'
    ]

    return bg, pe, ne, lbh, lbb


def subset_sum_triple():
    '''
    Sum of the terms at each position.
    {el(1,2,3)}.
    {el(2,3,5)}.
    {el(3,5,1)}.
    {el(4,1,3)}.
    {el(5,9,4)}.
    ok(V0):- #sum{V1,V2,V3:el(V1,V2,V3)}=V0,#sum{V2,V1,V3:el(V1,V2,V3)}=V0,#sum{V3,V1,V2:el(V1,V2,V3)}=V0.
    '''
    bg : 'list[str]' = [
        "{el(1,2,3)}.",
        "{el(2,3,5)}.",
        "{el(3,5,1)}.",
        "{el(4,1,3)}.",
        "{el(5,9,4)}."
    ]

    pe : 'list[list[str]]' = [
        ["ok(0)", ""],
        # ["ok(8)", ""],
        ["ok(9)", ""],
    ]

    ne : 'list[list[str]]' = [
        ["ok(1)", ""],
        ["ok(2)", ""],
        ["ok(10)", ""],
        ["ok(15)", ""],
    ]

    lbh : 'list[str]' = [
        'modeh(1, ok(+))'
        # 'modeh(1, s0(+))',
        # 'modeh(1, s1(+))'
    ]

    lbb : 'list[str]' = [
        # 'modeb(1, s0(+))',
        # 'modeb(1, s1(+))'
    ]

    return bg, pe, ne, lbh, lbb


def hamming(target_distance : int, harder : bool):
    '''
    Hamming distance between two binary strings.
    Given:
    pos(0..2).
    num(0..1).
    hd(1). % target distance
    % with hd(0), the constraint :- V0!=V1,v0(V1,V2),v1(V0,V2). suffices
    1{v0(Val,Pos) : num(Val)}1 :- pos(Pos).
    1{v1(Val,Pos) : num(Val)}1 :- pos(Pos).
    % too slow if i add these two rules to learn
    Learn if harder:
    d(Pos,X):- v0(V0,Pos), v1(V1,Pos), X = |V0 - V1|.
    :- Distance = #sum{X,P : d(P,X)}, hd(D), Distance != D.
    else only the constraint
    '''
    if not (target_distance in [0,1]):
        import sys
        sys.exit('Hamming requires distance 0 or 1')
    
    bg : 'list[str]' = [
        "pos(0..2).",
        "num(0..1).",
        f"hd({target_distance}). % target distance",
        "1{v0(Val,Pos) : num(Val)}1 :- pos(Pos).",
        "1{v1(Val,Pos) : num(Val)}1 :- pos(Pos)."
    ]
    
    if not harder:
        bg.append("d(Pos,X):- v0(V0,Pos), v1(V1,Pos), X = |V0 - V1|.")

    if target_distance == 1:
        # all the 24 solutions for hd(1)
        pe : 'list[list[str]]' = [
            ["v0(1,0) v0(1,1) v0(1,2) v1(0,1) v1(1,0) v1(1,2)",""],
            ["v0(0,1) v0(0,2) v0(1,0) v1(0,1) v1(1,0) v1(1,2)",""],
            ["v0(0,1) v0(1,0) v0(1,2) v1(0,1) v1(0,2) v1(1,0)",""],
            ["v0(0,2) v0(1,0) v0(1,1) v1(0,1) v1(0,2) v1(1,0)",""],
            ["v0(0,1) v0(1,0) v0(1,2) v1(1,0) v1(1,1) v1(1,2)",""],
            ["v0(1,0) v0(1,1) v0(1,2) v1(0,2) v1(1,0) v1(1,1)",""],
            ["v0(0,2) v0(1,0) v0(1,1) v1(1,0) v1(1,1) v1(1,2)",""],
            ["v0(0,1) v0(0,2) v0(1,0) v1(0,2) v1(1,0) v1(1,1)",""],
            ["v0(0,0) v0(1,1) v0(1,2) v1(1,0) v1(1,1) v1(1,2)",""],
            ["v0(0,0) v0(0,1) v0(1,2) v1(0,1) v1(1,0) v1(1,2)",""],
            ["v0(0,0) v0(0,2) v0(1,1) v1(0,2) v1(1,0) v1(1,1)",""],
            ["v0(0,0) v0(0,1) v0(0,2) v1(0,1) v1(0,2) v1(1,0)",""],
            ["v0(0,2) v0(1,0) v0(1,1) v1(0,0) v1(0,2) v1(1,1)",""],
            ["v0(0,0) v0(0,2) v0(1,1) v1(0,0) v1(0,1) v1(0,2)",""],
            ["v0(0,0) v0(0,2) v0(1,1) v1(0,0) v1(1,1) v1(1,2)",""],
            ["v0(0,0) v0(1,1) v0(1,2) v1(0,0) v1(0,2) v1(1,1)",""],
            ["v0(1,0) v0(1,1) v0(1,2) v1(0,0) v1(1,1) v1(1,2)",""],
            ["v0(0,0) v0(1,1) v0(1,2) v1(0,0) v1(0,1) v1(1,2)",""],
            ["v0(0,1) v0(1,0) v0(1,2) v1(0,0) v1(0,1) v1(1,2)",""],
            ["v0(0,1) v0(0,2) v0(1,0) v1(0,0) v1(0,1) v1(0,2)",""],
            ["v0(0,0) v0(0,1) v0(1,2) v1(0,0) v1(1,1) v1(1,2)",""],
            ["v0(0,0) v0(0,1) v0(1,2) v1(0,0) v1(0,1) v1(0,2)",""],
            ["v0(0,0) v0(0,1) v0(0,2) v1(0,0) v1(0,1) v1(1,2)",""],
            ["v0(0,0) v0(0,1) v0(0,2) v1(0,0) v1(0,2) v1(1,1)",""]
        ]
        # all the 64 - 24 = 40 solutions for hd(1)
        ne : 'list[list[str]]' = [
            ["v0(0,1) v0(1,0) v0(1,2) v1(0,1) v1(1,0) v1(1,2)",""],
            ["v0(0,2) v0(1,0) v0(1,1) v1(0,1) v1(1,0) v1(1,2)",""],
            ["v0(1,0) v0(1,1) v0(1,2) v1(0,1) v1(0,2) v1(1,0)",""],
            ["v0(0,1) v0(0,2) v0(1,0) v1(0,1) v1(0,2) v1(1,0)",""],
            ["v0(0,1) v0(1,0) v0(1,2) v1(0,2) v1(1,0) v1(1,1)",""],
            ["v0(1,0) v0(1,1) v0(1,2) v1(1,0) v1(1,1) v1(1,2)",""],
            ["v0(0,2) v0(1,0) v0(1,1) v1(0,2) v1(1,0) v1(1,1)",""],
            ["v0(0,1) v0(0,2) v0(1,0) v1(1,0) v1(1,1) v1(1,2)",""],
            ["v0(0,0) v0(1,1) v0(1,2) v1(0,2) v1(1,0) v1(1,1)",""],
            ["v0(0,0) v0(0,1) v0(1,2) v1(0,2) v1(1,0) v1(1,1)",""],
            ["v0(0,0) v0(0,1) v0(0,2) v1(0,2) v1(1,0) v1(1,1)",""],
            ["v0(0,0) v0(1,1) v0(1,2) v1(0,1) v1(0,2) v1(1,0)",""],
            ["v0(0,0) v0(0,2) v0(1,1) v1(0,1) v1(0,2) v1(1,0)",""],
            ["v0(0,0) v0(0,1) v0(1,2) v1(0,1) v1(0,2) v1(1,0)",""],
            ["v0(0,0) v0(0,1) v0(1,2) v1(1,0) v1(1,1) v1(1,2)",""],
            ["v0(0,0) v0(1,1) v0(1,2) v1(0,1) v1(1,0) v1(1,2)",""],
            ["v0(0,0) v0(0,2) v0(1,1) v1(1,0) v1(1,1) v1(1,2)",""],
            ["v0(0,0) v0(0,2) v0(1,1) v1(0,1) v1(1,0) v1(1,2)",""],
            ["v0(0,0) v0(0,1) v0(0,2) v1(1,0) v1(1,1) v1(1,2)",""],
            ["v0(0,0) v0(0,1) v0(0,2) v1(0,1) v1(1,0) v1(1,2)",""],
            ["v0(1,0) v0(1,1) v0(1,2) v1(0,0) v1(0,2) v1(1,1)",""],
            ["v0(0,2) v0(1,0) v0(1,1) v1(0,0) v1(1,1) v1(1,2)",""],
            ["v0(0,1) v0(1,0) v0(1,2) v1(0,0) v1(0,2) v1(1,1)",""],
            ["v0(0,1) v0(1,0) v0(1,2) v1(0,0) v1(1,1) v1(1,2)",""],
            ["v0(0,1) v0(0,2) v0(1,0) v1(0,0) v1(0,2) v1(1,1)",""],
            ["v0(0,1) v0(0,2) v0(1,0) v1(0,0) v1(1,1) v1(1,2)",""],
            ["v0(0,0) v0(0,1) v0(1,2) v1(0,0) v1(0,2) v1(1,1)",""],
            ["v0(0,0) v0(0,2) v0(1,1) v1(0,0) v1(0,2) v1(1,1)",""],
            ["v0(0,0) v0(1,1) v0(1,2) v1(0,0) v1(1,1) v1(1,2)",""],
            ["v0(0,0) v0(0,1) v0(0,2) v1(0,0) v1(1,1) v1(1,2)",""],
            ["v0(1,0) v0(1,1) v0(1,2) v1(0,0) v1(0,1) v1(0,2)",""],
            ["v0(0,0) v0(1,1) v0(1,2) v1(0,0) v1(0,1) v1(0,2)",""],
            ["v0(0,1) v0(1,0) v0(1,2) v1(0,0) v1(0,1) v1(0,2)",""],
            ["v0(1,0) v0(1,1) v0(1,2) v1(0,0) v1(0,1) v1(1,2)",""],
            ["v0(0,0) v0(0,1) v0(1,2) v1(0,0) v1(0,1) v1(1,2)",""],
            ["v0(0,2) v0(1,0) v0(1,1) v1(0,0) v1(0,1) v1(0,2)",""],
            ["v0(0,2) v0(1,0) v0(1,1) v1(0,0) v1(0,1) v1(1,2)",""],
            ["v0(0,0) v0(0,2) v0(1,1) v1(0,0) v1(0,1) v1(1,2)",""],
            ["v0(0,1) v0(0,2) v0(1,0) v1(0,0) v1(0,1) v1(1,2)",""],
            ["v0(0,0) v0(0,1) v0(0,2) v1(0,0) v1(0,1) v1(0,2)",""]
        ]
    else:
        # all the 8 solutions for hd(0)
        pe : 'list[list[str]]' = [
            ["v0(1,0) v1(1,0) v1(0,1) v0(0,1) v0(1,2) v1(1,2)",""],
            ["v0(1,0) v1(1,0) v1(0,1) v0(0,1) v1(0,2) v0(0,2)",""],
            ["v0(1,0) v1(1,0) v0(1,1) v1(1,1) v0(1,2) v1(1,2)",""],
            ["v0(1,0) v1(1,0) v0(1,1) v1(1,1) v1(0,2) v0(0,2)",""],
            ["v1(0,0) v0(0,0) v1(0,1) v0(0,1) v0(1,2) v1(1,2)",""],
            ["v1(0,0) v0(0,0) v0(1,1) v1(1,1) v0(1,2) v1(1,2)",""],
            ["v1(0,0) v0(0,0) v1(0,1) v0(0,1) v1(0,2) v0(0,2)",""],
            ["v1(0,0) v0(0,0) v0(1,1) v1(1,1) v1(0,2) v0(0,2)",""]
        ]
        # all the 64 - 8 = 56 solutions for hd(0)
        ne : 'list[list[str]]' = [
            ["v0(1,0) v0(1,1) v0(1,2) v1(0,1) v1(1,0) v1(1,2)",""],
            ["v0(0,2) v0(1,0) v0(1,1) v1(0,1) v1(1,0) v1(1,2)",""],
            ["v0(0,1) v0(0,2) v0(1,0) v1(0,1) v1(1,0) v1(1,2)",""],
            ["v0(1,0) v0(1,1) v0(1,2) v1(0,1) v1(0,2) v1(1,0)",""],
            ["v0(0,2) v0(1,0) v0(1,1) v1(0,1) v1(0,2) v1(1,0)",""],
            ["v0(0,1) v0(1,0) v0(1,2) v1(0,1) v1(0,2) v1(1,0)",""],
            ["v0(1,0) v0(1,1) v0(1,2) v1(0,2) v1(1,0) v1(1,1)",""],
            ["v0(0,1) v0(1,0) v0(1,2) v1(0,2) v1(1,0) v1(1,1)",""],
            ["v0(0,1) v0(1,0) v0(1,2) v1(1,0) v1(1,1) v1(1,2)",""],
            ["v0(0,2) v0(1,0) v0(1,1) v1(1,0) v1(1,1) v1(1,2)",""],
            ["v0(0,1) v0(0,2) v0(1,0) v1(0,2) v1(1,0) v1(1,1)",""],
            ["v0(0,1) v0(0,2) v0(1,0) v1(1,0) v1(1,1) v1(1,2)",""],
            ["v0(0,0) v0(1,1) v0(1,2) v1(0,2) v1(1,0) v1(1,1)",""],
            ["v0(0,0) v0(0,1) v0(1,2) v1(0,2) v1(1,0) v1(1,1)",""],
            ["v0(0,0) v0(0,2) v0(1,1) v1(0,2) v1(1,0) v1(1,1)",""],
            ["v0(0,0) v0(0,1) v0(0,2) v1(0,2) v1(1,0) v1(1,1)",""],
            ["v0(0,0) v0(1,1) v0(1,2) v1(0,1) v1(0,2) v1(1,0)",""],
            ["v0(0,0) v0(0,2) v0(1,1) v1(0,1) v1(0,2) v1(1,0)",""],
            ["v0(0,0) v0(0,1) v0(1,2) v1(0,1) v1(0,2) v1(1,0)",""],
            ["v0(0,0) v0(0,1) v0(0,2) v1(0,1) v1(0,2) v1(1,0)",""],
            ["v0(0,0) v0(1,1) v0(1,2) v1(1,0) v1(1,1) v1(1,2)",""],
            ["v0(0,0) v0(0,1) v0(1,2) v1(1,0) v1(1,1) v1(1,2)",""],
            ["v0(0,0) v0(1,1) v0(1,2) v1(0,1) v1(1,0) v1(1,2)",""],
            ["v0(0,0) v0(0,1) v0(1,2) v1(0,1) v1(1,0) v1(1,2)",""],
            ["v0(0,0) v0(0,2) v0(1,1) v1(1,0) v1(1,1) v1(1,2)",""],
            ["v0(0,0) v0(0,2) v0(1,1) v1(0,1) v1(1,0) v1(1,2)",""],
            ["v0(0,0) v0(0,1) v0(0,2) v1(1,0) v1(1,1) v1(1,2)",""],
            ["v0(0,0) v0(0,1) v0(0,2) v1(0,1) v1(1,0) v1(1,2)",""],
            ["v0(1,0) v0(1,1) v0(1,2) v1(0,0) v1(0,2) v1(1,1)",""],
            ["v0(0,2) v0(1,0) v0(1,1) v1(0,0) v1(0,2) v1(1,1)",""],
            ["v0(1,0) v0(1,1) v0(1,2) v1(0,0) v1(1,1) v1(1,2)",""],
            ["v0(0,2) v0(1,0) v0(1,1) v1(0,0) v1(1,1) v1(1,2)",""],
            ["v0(0,1) v0(1,0) v0(1,2) v1(0,0) v1(0,2) v1(1,1)",""],
            ["v0(0,1) v0(1,0) v0(1,2) v1(0,0) v1(1,1) v1(1,2)",""],
            ["v0(0,1) v0(0,2) v0(1,0) v1(0,0) v1(0,2) v1(1,1)",""],
            ["v0(0,1) v0(0,2) v0(1,0) v1(0,0) v1(1,1) v1(1,2)",""],
            ["v0(0,0) v0(1,1) v0(1,2) v1(0,0) v1(0,2) v1(1,1)",""],
            ["v0(0,0) v0(0,1) v0(1,2) v1(0,0) v1(0,2) v1(1,1)",""],
            ["v0(0,0) v0(0,1) v0(0,2) v1(0,0) v1(0,2) v1(1,1)",""],
            ["v0(0,0) v0(0,2) v0(1,1) v1(0,0) v1(1,1) v1(1,2)",""],
            ["v0(0,0) v0(0,1) v0(1,2) v1(0,0) v1(1,1) v1(1,2)",""],
            ["v0(0,0) v0(0,1) v0(0,2) v1(0,0) v1(1,1) v1(1,2)",""],
            ["v0(1,0) v0(1,1) v0(1,2) v1(0,0) v1(0,1) v1(0,2)",""],
            ["v0(0,0) v0(1,1) v0(1,2) v1(0,0) v1(0,1) v1(0,2)",""],
            ["v0(0,1) v0(1,0) v0(1,2) v1(0,0) v1(0,1) v1(0,2)",""],
            ["v0(0,0) v0(0,1) v0(1,2) v1(0,0) v1(0,1) v1(0,2)",""],
            ["v0(1,0) v0(1,1) v0(1,2) v1(0,0) v1(0,1) v1(1,2)",""],
            ["v0(0,1) v0(1,0) v0(1,2) v1(0,0) v1(0,1) v1(1,2)",""],
            ["v0(0,0) v0(1,1) v0(1,2) v1(0,0) v1(0,1) v1(1,2)",""],
            ["v0(0,2) v0(1,0) v0(1,1) v1(0,0) v1(0,1) v1(0,2)",""],
            ["v0(0,0) v0(0,2) v0(1,1) v1(0,0) v1(0,1) v1(0,2)",""],
            ["v0(0,2) v0(1,0) v0(1,1) v1(0,0) v1(0,1) v1(1,2)",""],
            ["v0(0,0) v0(0,2) v0(1,1) v1(0,0) v1(0,1) v1(1,2)",""],
            ["v0(0,1) v0(0,2) v0(1,0) v1(0,0) v1(0,1) v1(0,2)",""],
            ["v0(0,1) v0(0,2) v0(1,0) v1(0,0) v1(0,1) v1(1,2)",""],
            ["v0(0,0) v0(0,1) v0(0,2) v1(0,0) v1(0,1) v1(1,2)",""]
        ]

    # d(Pos,X):- v0(V0,Pos), v1(V1,Pos), X = |V0 - V1|.
    # :- Distance = #sum{X,P : d(P,X)}, hd(D), Distance != D.

    lbh : 'list[str]' = [
    ]
    if harder:
        lbh.append('modeh(1, d(+,+))')

    lbb : 'list[str]' = [
        'modeb(1, hd(+))'
    ]
    if harder:
        lbb.append('modeb(1, v0(+,+))')
        lbb.append('modeb(1, v1(+,+))')

    return bg, pe, ne, lbh, lbb

def n_4queens():
    '''
    % from http://www.hakank.org/answer_set_programming/nqueens.lp
    #const n = 4.

    % domain
    number(1..n).

    % alldifferent
    1 { q(X,Y) : number(Y) } 1 :- number(X).
    1 { q(X,Y) : number(X) } 1 :- number(Y).

    % remove conflicting answers: these rules should be learned
    % two rules should suffice
    '''
    bg : 'list[str]' = [
        "#const n = 4.", 
        "number(1..n).", 
        "1 { q(X,Y) : number(Y) } 1 :- number(X).", 
        "1 { q(X,Y) : number(X) } 1 :- number(Y)."
    ]
    
    # all the existing solutions
    pe : 'list[list[str]]' = [
        ["q(1,3) q(2,1) q(3,4) q(4,2)", ""],
        ["q(1,2) q(2,4) q(3,1) q(4,3)", ""]
    ]
    
    # all the possible placements - all existing solutions
    ne : 'list[list[str]]' = [
        ["q(4,1) q(3,2) q(2,3) q(1,4)",""],
        ["q(3,1) q(4,2) q(2,3) q(1,4)",""],
        ["q(4,1) q(2,2) q(3,3) q(1,4)",""],
        ["q(2,1) q(4,2) q(3,3) q(1,4)",""],
        ["q(3,1) q(2,2) q(4,3) q(1,4)",""],
        ["q(2,1) q(3,2) q(4,3) q(1,4)",""],
        # ["q(3,1) q(1,2) q(4,3) q(2,4)",""],
        ["q(4,1) q(1,2) q(3,3) q(2,4)",""],
        ["q(3,1) q(4,2) q(1,3) q(2,4)",""],
        ["q(4,1) q(3,2) q(1,3) q(2,4)",""],
        ["q(4,1) q(2,2) q(1,3) q(3,4)",""],
        ["q(2,1) q(1,2) q(4,3) q(3,4)",""],
        ["q(4,1) q(1,2) q(2,3) q(3,4)",""],
        # ["q(2,1) q(4,2) q(1,3) q(3,4)",""],
        ["q(3,1) q(2,2) q(1,3) q(4,4)",""],
        ["q(3,1) q(1,2) q(2,3) q(4,4)",""],
        ["q(2,1) q(3,2) q(1,3) q(4,4)",""],
        ["q(2,1) q(1,2) q(3,3) q(4,4)",""],
        ["q(1,1) q(2,2) q(4,3) q(3,4)",""],
        ["q(1,1) q(3,2) q(4,3) q(2,4)",""],
        ["q(1,1) q(2,2) q(3,3) q(4,4)",""],
        ["q(1,1) q(4,2) q(3,3) q(2,4)",""],
        ["q(1,1) q(4,2) q(2,3) q(3,4)",""],
        ["q(1,1) q(3,2) q(2,3) q(4,4)",""]
    ]
    
    lbh : 'list[str]' = []
    
    lbb : 'list[str]' = ['modeb(2, q(+,+))']
    
    return bg, pe, ne, lbh, lbb


def n_5queens():
    '''
    % from http://www.hakank.org/answer_set_programming/nqueens.lp
    #const n = 5.

    % domain
    number(1..n).

    % alldifferent
    1 { q(X,Y) : number(Y) } 1 :- number(X).
    1 { q(X,Y) : number(X) } 1 :- number(Y).

    % remove conflicting answers: these rules should be learned
    :- q(X1,Y), q(X2,Y), X1 < X2.
    :- q(X1,Y1), q(X2,Y2), X1 < X2, Y1 + X1 = Z, Z = Y2 + X2.
    :- q(X1,Y1), q(X2,Y2), X1 < X2, Y1 - X1 = Z, Z = Y2 - X2.
    '''
    bg : 'list[str]' = [
        "#const n = 5.", 
        "number(1..n).", 
        "1 { q(X,Y) : number(Y) } 1 :- number(X).", 
        "1 { q(X,Y) : number(X) } 1 :- number(Y)."
    ]
    
    # all existing solutions (10)
    pe : 'list[list[str]]' = [
        ["q(1,3) q(2,1) q(3,4) q(4,2) q(5,5)",""],
        ["q(1,1) q(2,3) q(3,5) q(4,2) q(5,4)",""],
        ["q(2,3) q(3,1) q(4,4) q(5,2) q(1,5)",""],
        ["q(1,2) q(2,4) q(3,1) q(4,3) q(5,5)",""],
        ["q(1,1) q(2,4) q(3,2) q(4,5) q(5,3)",""],
        ["q(1,3) q(2,5) q(3,2) q(4,4) q(5,1)",""],
        ["q(2,2) q(1,4) q(3,5) q(4,3) q(5,1)",""],
        ["q(2,2) q(3,4) q(4,1) q(5,3) q(1,5)",""],
        ["q(1,4) q(2,1) q(3,3) q(4,5) q(5,2)",""],
        ["q(1,2) q(2,5) q(3,3) q(4,1) q(5,4)",""]
    ]
    
    # some random examples (35) among all the solutions - valid
    ne : 'list[list[str]]' = [
        ["q(1,1) q(2,5) q(3,4) q(4,3) q(5,2)",""],
        ["q(1,1) q(2,2) q(3,5) q(4,4) q(5,3)",""],
        ["q(1,1) q(2,4) q(3,5) q(4,2) q(5,3)",""],
        ["q(1,1) q(2,3) q(3,5) q(4,4) q(5,2)",""],
        ["q(1,1) q(2,3) q(3,4) q(4,5) q(5,2)",""],
        ["q(1,1) q(2,4) q(3,3) q(4,2) q(5,5)",""],
        ["q(1,1) q(2,3) q(3,4) q(4,2) q(5,5)",""],
        ["q(1,1) q(2,4) q(3,2) q(4,3) q(5,5)",""],
        ["q(1,1) q(2,2) q(3,4) q(4,3) q(5,5)",""],
        ["q(1,1) q(2,3) q(3,2) q(4,4) q(5,5)",""],
        ["q(1,1) q(2,2) q(3,3) q(4,4) q(5,5)",""],
        ["q(1,3) q(2,4) q(3,1) q(4,5) q(5,2)",""],
        ["q(1,3) q(2,4) q(3,2) q(4,5) q(5,1)",""],
        ["q(1,2) q(2,3) q(3,1) q(4,5) q(5,4)",""],
        ["q(1,4) q(2,3) q(3,1) q(4,5) q(5,2)",""],
        ["q(1,4) q(2,3) q(3,2) q(4,5) q(5,1)",""],
        ["q(1,2) q(2,3) q(3,4) q(4,5) q(5,1)",""],
        ["q(1,3) q(2,2) q(3,4) q(4,1) q(5,5)",""],
        ["q(1,3) q(2,4) q(3,5) q(4,1) q(5,2)",""],
        ["q(1,2) q(2,1) q(3,5) q(4,3) q(5,4)",""],
        ["q(1,2) q(2,4) q(3,5) q(4,3) q(5,1)",""],
        ["q(1,2) q(2,4) q(3,5) q(4,1) q(5,3)",""],
        ["q(1,3) q(2,1) q(3,5) q(4,2) q(5,4)",""],
        ["q(1,3) q(2,4) q(3,5) q(4,2) q(5,1)",""],
        ["q(1,3) q(2,2) q(3,5) q(4,4) q(5,1)",""],
        ["q(1,5) q(2,3) q(3,2) q(4,4) q(5,1)",""],
        ["q(1,5) q(2,2) q(3,3) q(4,4) q(5,1)",""],
        ["q(1,5) q(2,1) q(3,3) q(4,4) q(5,2)",""],
        ["q(1,5) q(2,2) q(3,1) q(4,4) q(5,3)",""],
        ["q(1,5) q(2,1) q(3,2) q(4,4) q(5,3)",""],
        ["q(1,5) q(2,2) q(3,1) q(4,3) q(5,4)",""],
        ["q(1,5) q(2,3) q(3,1) q(4,2) q(5,4)",""],
        ["q(1,5) q(2,4) q(3,3) q(4,2) q(5,1)",""],
        ["q(1,5) q(2,4) q(3,3) q(4,1) q(5,2)",""],
        ["q(1,5) q(2,4) q(3,2) q(4,3) q(5,1)",""]
    ]
    
    lbh : 'list[str]' = []
    
    lbb : 'list[str]' = ['modeb(2, q(+,+))']
    
    return bg, pe, ne, lbh, lbb


def clique():
    '''
    Clique ok size 3.
    Given:
    3 {in(X) : v(X)} 3.
    v(X) :- e(X,Y).
    v(Y) :- e(X,Y).
    Learn:
    :- in(X), in(Y), v(X), v(Y), X!=Y, not e(X,Y), not e(Y,X).
    Only 2 solutions:
    in(1) in(2) in(5)
    in(1) in(9) in(5)
    '''
    bg : 'list[str]' = [
        "v(1..9).",
        "e(1,2).",
        "e(1,5).",
        "e(1,9).",
        "e(3,1).",
        "e(3,4).",
        "e(3,8).",
        "e(5,4).",
        "e(6,3).",
        "e(6,7).",
        "e(2,5).",
        "e(4,7).",
        "e(7,1).",
        "e(8,2).",
        "e(9,5).",
        "e(9,6).",
        "3 {in(X) : v(X)} 3.",
        "v(X) :- e(X,Y).",
        "v(Y) :- e(X,Y)."
    ]

    pe : 'list[list[str]]' = [
        ["in(1) in(2) in(5)", ""],
        ["in(1) in(9) in(5)", ""]
    ]

    ne : 'list[list[str]]' = [
        ["in(3)", ""],
        ["in(4)", ""]
    ]

    lbh : 'list[str]' = [
        # 'modeh(1, v(+))'
    ]

    lbb : 'list[str]' = [
        'modeb(2, v(+))',
        # 'modeb(2, e(+,+))',
        'modeb(2, not e(+,+))',
        'modeb(2, in(+))'
    ]

    return bg, pe, ne, lbh, lbb


def magic_square_no_diag():
    '''
    With aggregates: limited to the sum of columns and row.
    Constraint: the sum of the elements in the rows and columns
    should be the same.
    To learn:
    sum_row(R,S):- S = #sum{V : x(R,C,V), size(C)}, size(R).
    sum_col(C,S):- S = #sum{V : x(R,C,V), size(R)}, size(C).
    :- sum_col(C0,SC0), sum_col(C1,SC1), C0 != C1, SC0 != SC1.
    :- sum_row(R0,SR0), sum_row(R1,SR1), R0 != R1, SR0 != SR1.
    '''
    # https://en.wikipedia.org/wiki/Magic_square
    bg : 'list[str]' = [
        "#const n = 3.",
        "#const s = n*(n*n + 1) / 2.",
        "size(1..n).",
        "val(1..n*n).",
        "1 { x(Row, Col, N) : val(N) } 1 :- size(Row), size(Col).",
        "1 { x(Row, Col, N) : size(Row), size(Col) } 1 :- val(N)."
    ]
    
    # all the 72 solutions
    pe : 'list[list[str]]' = [
        ["x(1,1,4) x(1,2,2) x(1,3,9) x(2,1,8) x(2,2,6) x(2,3,1) x(3,1,3) x(3,2,7) x(3,3,5)",""],
        ["x(1,1,3) x(1,2,7) x(1,3,5) x(2,1,8) x(2,2,6) x(2,3,1) x(3,1,4) x(3,2,2) x(3,3,9)",""],
        ["x(1,1,7) x(1,2,3) x(1,3,5) x(2,1,6) x(2,2,8) x(2,3,1) x(3,1,2) x(3,2,4) x(3,3,9)",""],
        ["x(1,1,2) x(1,2,4) x(1,3,9) x(2,1,6) x(2,2,8) x(2,3,1) x(3,1,7) x(3,2,3) x(3,3,5)",""],
        ["x(1,1,4) x(1,2,3) x(1,3,8) x(2,1,9) x(2,2,5) x(2,3,1) x(3,1,2) x(3,2,7) x(3,3,6)",""],
        ["x(1,1,2) x(1,2,7) x(1,3,6) x(2,1,9) x(2,2,5) x(2,3,1) x(3,1,4) x(3,2,3) x(3,3,8)",""],
        ["x(1,1,3) x(1,2,4) x(1,3,8) x(2,1,5) x(2,2,9) x(2,3,1) x(3,1,7) x(3,2,2) x(3,3,6)",""],
        ["x(1,1,7) x(1,2,2) x(1,3,6) x(2,1,5) x(2,2,9) x(2,3,1) x(3,1,3) x(3,2,4) x(3,3,8)",""],
        ["x(1,1,7) x(1,2,5) x(1,3,3) x(2,1,6) x(2,2,1) x(2,3,8) x(3,1,2) x(3,2,9) x(3,3,4)",""],
        ["x(1,1,7) x(1,2,6) x(1,3,2) x(2,1,5) x(2,2,1) x(2,3,9) x(3,1,3) x(3,2,8) x(3,3,4)",""],
        ["x(1,1,3) x(1,2,5) x(1,3,7) x(2,1,8) x(2,2,1) x(2,3,6) x(3,1,4) x(3,2,9) x(3,3,2)",""],
        ["x(1,1,2) x(1,2,6) x(1,3,7) x(2,1,9) x(2,2,1) x(2,3,5) x(3,1,4) x(3,2,8) x(3,3,3)",""],
        ["x(1,1,2) x(1,2,9) x(1,3,4) x(2,1,6) x(2,2,1) x(2,3,8) x(3,1,7) x(3,2,5) x(3,3,3)",""],
        ["x(1,1,4) x(1,2,9) x(1,3,2) x(2,1,8) x(2,2,1) x(2,3,6) x(3,1,3) x(3,2,5) x(3,3,7)",""],
        ["x(1,1,3) x(1,2,8) x(1,3,4) x(2,1,5) x(2,2,1) x(2,3,9) x(3,1,7) x(3,2,6) x(3,3,2)",""],
        ["x(1,1,4) x(1,2,8) x(1,3,3) x(2,1,9) x(2,2,1) x(2,3,5) x(3,1,2) x(3,2,6) x(3,3,7)",""],
        ["x(1,1,5) x(1,2,1) x(1,3,9) x(2,1,3) x(2,2,8) x(2,3,4) x(3,1,7) x(3,2,6) x(3,3,2)",""],
        ["x(1,1,7) x(1,2,6) x(1,3,2) x(2,1,3) x(2,2,8) x(2,3,4) x(3,1,5) x(3,2,1) x(3,3,9)",""],
        ["x(1,1,3) x(1,2,8) x(1,3,4) x(2,1,7) x(2,2,6) x(2,3,2) x(3,1,5) x(3,2,1) x(3,3,9)",""],
        ["x(1,1,5) x(1,2,1) x(1,3,9) x(2,1,7) x(2,2,6) x(2,3,2) x(3,1,3) x(3,2,8) x(3,3,4)",""],
        ["x(1,1,7) x(1,2,3) x(1,3,5) x(2,1,2) x(2,2,4) x(2,3,9) x(3,1,6) x(3,2,8) x(3,3,1)",""],
        ["x(1,1,2) x(1,2,4) x(1,3,9) x(2,1,7) x(2,2,3) x(2,3,5) x(3,1,6) x(3,2,8) x(3,3,1)",""],
        ["x(1,1,6) x(1,2,8) x(1,3,1) x(2,1,7) x(2,2,3) x(2,3,5) x(3,1,2) x(3,2,4) x(3,3,9)",""],
        ["x(1,1,6) x(1,2,8) x(1,3,1) x(2,1,2) x(2,2,4) x(2,3,9) x(3,1,7) x(3,2,3) x(3,3,5)",""],
        ["x(1,1,9) x(1,2,1) x(1,3,5) x(2,1,2) x(2,2,6) x(2,3,7) x(3,1,4) x(3,2,8) x(3,3,3)",""],
        ["x(1,1,4) x(1,2,8) x(1,3,3) x(2,1,2) x(2,2,6) x(2,3,7) x(3,1,9) x(3,2,1) x(3,3,5)",""],
        ["x(1,1,2) x(1,2,6) x(1,3,7) x(2,1,4) x(2,2,8) x(2,3,3) x(3,1,9) x(3,2,1) x(3,3,5)",""],
        ["x(1,1,9) x(1,2,1) x(1,3,5) x(2,1,4) x(2,2,8) x(2,3,3) x(3,1,2) x(3,2,6) x(3,3,7)",""],
        ["x(1,1,9) x(1,2,4) x(1,3,2) x(2,1,5) x(2,2,3) x(2,3,7) x(3,1,1) x(3,2,8) x(3,3,6)",""],
        ["x(1,1,1) x(1,2,8) x(1,3,6) x(2,1,5) x(2,2,3) x(2,3,7) x(3,1,9) x(3,2,4) x(3,3,2)",""],
        ["x(1,1,5) x(1,2,3) x(1,3,7) x(2,1,9) x(2,2,4) x(2,3,2) x(3,1,1) x(3,2,8) x(3,3,6)",""],
        ["x(1,1,1) x(1,2,8) x(1,3,6) x(2,1,9) x(2,2,4) x(2,3,2) x(3,1,5) x(3,2,3) x(3,3,7)",""],
        ["x(1,1,5) x(1,2,3) x(1,3,7) x(2,1,1) x(2,2,8) x(2,3,6) x(3,1,9) x(3,2,4) x(3,3,2)",""],
        ["x(1,1,9) x(1,2,4) x(1,3,2) x(2,1,1) x(2,2,8) x(2,3,6) x(3,1,5) x(3,2,3) x(3,3,7)",""],
        ["x(1,1,8) x(1,2,1) x(1,3,6) x(2,1,3) x(2,2,5) x(2,3,7) x(3,1,4) x(3,2,9) x(3,3,2)",""],
        ["x(1,1,4) x(1,2,9) x(1,3,2) x(2,1,3) x(2,2,5) x(2,3,7) x(3,1,8) x(3,2,1) x(3,3,6)",""],
        ["x(1,1,3) x(1,2,5) x(1,3,7) x(2,1,4) x(2,2,9) x(2,3,2) x(3,1,8) x(3,2,1) x(3,3,6)",""],
        ["x(1,1,8) x(1,2,1) x(1,3,6) x(2,1,4) x(2,2,9) x(2,3,2) x(3,1,3) x(3,2,5) x(3,3,7)",""],
        ["x(1,1,1) x(1,2,9) x(1,3,5) x(2,1,8) x(2,2,4) x(2,3,3) x(3,1,6) x(3,2,2) x(3,3,7)",""],
        ["x(1,1,1) x(1,2,9) x(1,3,5) x(2,1,6) x(2,2,2) x(2,3,7) x(3,1,8) x(3,2,4) x(3,3,3)",""],
        ["x(1,1,6) x(1,2,2) x(1,3,7) x(2,1,1) x(2,2,9) x(2,3,5) x(3,1,8) x(3,2,4) x(3,3,3)",""],
        ["x(1,1,8) x(1,2,4) x(1,3,3) x(2,1,6) x(2,2,2) x(2,3,7) x(3,1,1) x(3,2,9) x(3,3,5)",""],
        ["x(1,1,6) x(1,2,2) x(1,3,7) x(2,1,8) x(2,2,4) x(2,3,3) x(3,1,1) x(3,2,9) x(3,3,5)",""],
        ["x(1,1,8) x(1,2,4) x(1,3,3) x(2,1,1) x(2,2,9) x(2,3,5) x(3,1,6) x(3,2,2) x(3,3,7)",""],
        ["x(1,1,3) x(1,2,7) x(1,3,5) x(2,1,4) x(2,2,2) x(2,3,9) x(3,1,8) x(3,2,6) x(3,3,1)",""],
        ["x(1,1,8) x(1,2,6) x(1,3,1) x(2,1,4) x(2,2,2) x(2,3,9) x(3,1,3) x(3,2,7) x(3,3,5)",""],
        ["x(1,1,8) x(1,2,6) x(1,3,1) x(2,1,3) x(2,2,7) x(2,3,5) x(3,1,4) x(3,2,2) x(3,3,9)",""],
        ["x(1,1,4) x(1,2,2) x(1,3,9) x(2,1,3) x(2,2,7) x(2,3,5) x(3,1,8) x(3,2,6) x(3,3,1)",""],
        ["x(1,1,5) x(1,2,7) x(1,3,3) x(2,1,1) x(2,2,6) x(2,3,8) x(3,1,9) x(3,2,2) x(3,3,4)",""],
        ["x(1,1,5) x(1,2,7) x(1,3,3) x(2,1,9) x(2,2,2) x(2,3,4) x(3,1,1) x(3,2,6) x(3,3,8)",""],
        ["x(1,1,9) x(1,2,2) x(1,3,4) x(2,1,1) x(2,2,6) x(2,3,8) x(3,1,5) x(3,2,7) x(3,3,3)",""],
        ["x(1,1,1) x(1,2,6) x(1,3,8) x(2,1,9) x(2,2,2) x(2,3,4) x(3,1,5) x(3,2,7) x(3,3,3)",""],
        ["x(1,1,1) x(1,2,6) x(1,3,8) x(2,1,5) x(2,2,7) x(2,3,3) x(3,1,9) x(3,2,2) x(3,3,4)",""],
        ["x(1,1,9) x(1,2,2) x(1,3,4) x(2,1,5) x(2,2,7) x(2,3,3) x(3,1,1) x(3,2,6) x(3,3,8)",""],
        ["x(1,1,4) x(1,2,3) x(1,3,8) x(2,1,2) x(2,2,7) x(2,3,6) x(3,1,9) x(3,2,5) x(3,3,1)",""],
        ["x(1,1,9) x(1,2,5) x(1,3,1) x(2,1,2) x(2,2,7) x(2,3,6) x(3,1,4) x(3,2,3) x(3,3,8)",""],
        ["x(1,1,2) x(1,2,7) x(1,3,6) x(2,1,4) x(2,2,3) x(2,3,8) x(3,1,9) x(3,2,5) x(3,3,1)",""],
        ["x(1,1,9) x(1,2,5) x(1,3,1) x(2,1,4) x(2,2,3) x(2,3,8) x(3,1,2) x(3,2,7) x(3,3,6)",""],
        ["x(1,1,1) x(1,2,5) x(1,3,9) x(2,1,8) x(2,2,3) x(2,3,4) x(3,1,6) x(3,2,7) x(3,3,2)",""],
        ["x(1,1,6) x(1,2,7) x(1,3,2) x(2,1,8) x(2,2,3) x(2,3,4) x(3,1,1) x(3,2,5) x(3,3,9)",""],
        ["x(1,1,8) x(1,2,3) x(1,3,4) x(2,1,1) x(2,2,5) x(2,3,9) x(3,1,6) x(3,2,7) x(3,3,2)",""],
        ["x(1,1,1) x(1,2,5) x(1,3,9) x(2,1,6) x(2,2,7) x(2,3,2) x(3,1,8) x(3,2,3) x(3,3,4)",""],
        ["x(1,1,8) x(1,2,3) x(1,3,4) x(2,1,6) x(2,2,7) x(2,3,2) x(3,1,1) x(3,2,5) x(3,3,9)",""],
        ["x(1,1,6) x(1,2,7) x(1,3,2) x(2,1,1) x(2,2,5) x(2,3,9) x(3,1,8) x(3,2,3) x(3,3,4)",""],
        ["x(1,1,5) x(1,2,9) x(1,3,1) x(2,1,7) x(2,2,2) x(2,3,6) x(3,1,3) x(3,2,4) x(3,3,8)",""],
        ["x(1,1,5) x(1,2,9) x(1,3,1) x(2,1,3) x(2,2,4) x(2,3,8) x(3,1,7) x(3,2,2) x(3,3,6)",""],
        ["x(1,1,7) x(1,2,2) x(1,3,6) x(2,1,3) x(2,2,4) x(2,3,8) x(3,1,5) x(3,2,9) x(3,3,1)",""],
        ["x(1,1,3) x(1,2,4) x(1,3,8) x(2,1,7) x(2,2,2) x(2,3,6) x(3,1,5) x(3,2,9) x(3,3,1)",""],
        ["x(1,1,6) x(1,2,1) x(1,3,8) x(2,1,7) x(2,2,5) x(2,3,3) x(3,1,2) x(3,2,9) x(3,3,4)",""],
        ["x(1,1,2) x(1,2,9) x(1,3,4) x(2,1,7) x(2,2,5) x(2,3,3) x(3,1,6) x(3,2,1) x(3,3,8)",""],
        ["x(1,1,7) x(1,2,5) x(1,3,3) x(2,1,2) x(2,2,9) x(2,3,4) x(3,1,6) x(3,2,1) x(3,3,8)",""],
        ["x(1,1,6) x(1,2,1) x(1,3,8) x(2,1,2) x(2,2,9) x(2,3,4) x(3,1,7) x(3,2,5) x(3,3,3)",""]
    ]
    
    # 200 not valid solutions
    ne : 'list[list[str]]' = [
        ["x(1,1,6) x(1,2,4) x(1,3,8) x(2,1,5) x(2,2,3) x(2,3,9) x(3,1,7) x(3,2,2) x(3,3,1)",""],
        ["x(1,1,7) x(1,2,4) x(1,3,8) x(2,1,5) x(2,2,3) x(2,3,9) x(3,1,6) x(3,2,2) x(3,3,1)",""],
        ["x(1,1,5) x(1,2,4) x(1,3,8) x(2,1,6) x(2,2,3) x(2,3,9) x(3,1,7) x(3,2,2) x(3,3,1)",""],
        ["x(1,1,5) x(1,2,4) x(1,3,8) x(2,1,7) x(2,2,3) x(2,3,9) x(3,1,6) x(3,2,2) x(3,3,1)",""],
        ["x(1,1,7) x(1,2,4) x(1,3,8) x(2,1,6) x(2,2,3) x(2,3,9) x(3,1,5) x(3,2,2) x(3,3,1)",""],
        ["x(1,1,6) x(1,2,4) x(1,3,8) x(2,1,7) x(2,2,3) x(2,3,9) x(3,1,5) x(3,2,2) x(3,3,1)",""],
        ["x(1,1,5) x(1,2,7) x(1,3,8) x(2,1,6) x(2,2,3) x(2,3,9) x(3,1,4) x(3,2,2) x(3,3,1)",""],
        ["x(1,1,4) x(1,2,7) x(1,3,8) x(2,1,6) x(2,2,3) x(2,3,9) x(3,1,5) x(3,2,2) x(3,3,1)",""],
        ["x(1,1,4) x(1,2,7) x(1,3,8) x(2,1,5) x(2,2,3) x(2,3,9) x(3,1,6) x(3,2,2) x(3,3,1)",""],
        ["x(1,1,5) x(1,2,7) x(1,3,8) x(2,1,4) x(2,2,3) x(2,3,9) x(3,1,6) x(3,2,2) x(3,3,1)",""],
        ["x(1,1,6) x(1,2,7) x(1,3,8) x(2,1,4) x(2,2,3) x(2,3,9) x(3,1,5) x(3,2,2) x(3,3,1)",""],
        ["x(1,1,6) x(1,2,7) x(1,3,8) x(2,1,5) x(2,2,3) x(2,3,9) x(3,1,4) x(3,2,2) x(3,3,1)",""],
        ["x(1,1,7) x(1,2,5) x(1,3,8) x(2,1,6) x(2,2,3) x(2,3,9) x(3,1,4) x(3,2,2) x(3,3,1)",""],
        ["x(1,1,4) x(1,2,5) x(1,3,8) x(2,1,6) x(2,2,3) x(2,3,9) x(3,1,7) x(3,2,2) x(3,3,1)",""],
        ["x(1,1,7) x(1,2,5) x(1,3,8) x(2,1,4) x(2,2,3) x(2,3,9) x(3,1,6) x(3,2,2) x(3,3,1)",""],
        ["x(1,1,4) x(1,2,5) x(1,3,8) x(2,1,7) x(2,2,3) x(2,3,9) x(3,1,6) x(3,2,2) x(3,3,1)",""],
        ["x(1,1,6) x(1,2,5) x(1,3,8) x(2,1,4) x(2,2,3) x(2,3,9) x(3,1,7) x(3,2,2) x(3,3,1)",""],
        ["x(1,1,6) x(1,2,5) x(1,3,8) x(2,1,7) x(2,2,3) x(2,3,9) x(3,1,4) x(3,2,2) x(3,3,1)",""],
        ["x(1,1,7) x(1,2,6) x(1,3,8) x(2,1,4) x(2,2,3) x(2,3,9) x(3,1,5) x(3,2,2) x(3,3,1)",""],
        ["x(1,1,4) x(1,2,6) x(1,3,8) x(2,1,7) x(2,2,3) x(2,3,9) x(3,1,5) x(3,2,2) x(3,3,1)",""],
        ["x(1,1,7) x(1,2,6) x(1,3,8) x(2,1,5) x(2,2,3) x(2,3,9) x(3,1,4) x(3,2,2) x(3,3,1)",""],
        ["x(1,1,4) x(1,2,6) x(1,3,8) x(2,1,5) x(2,2,3) x(2,3,9) x(3,1,7) x(3,2,2) x(3,3,1)",""],
        ["x(1,1,5) x(1,2,6) x(1,3,8) x(2,1,4) x(2,2,3) x(2,3,9) x(3,1,7) x(3,2,2) x(3,3,1)",""],
        ["x(1,1,5) x(1,2,6) x(1,3,8) x(2,1,7) x(2,2,3) x(2,3,9) x(3,1,4) x(3,2,2) x(3,3,1)",""],
        ["x(1,1,5) x(1,2,3) x(1,3,8) x(2,1,6) x(2,2,4) x(2,3,9) x(3,1,7) x(3,2,2) x(3,3,1)",""],
        ["x(1,1,5) x(1,2,3) x(1,3,8) x(2,1,6) x(2,2,7) x(2,3,9) x(3,1,4) x(3,2,2) x(3,3,1)",""],
        ["x(1,1,7) x(1,2,3) x(1,3,8) x(2,1,6) x(2,2,4) x(2,3,9) x(3,1,5) x(3,2,2) x(3,3,1)",""],
        ["x(1,1,4) x(1,2,3) x(1,3,8) x(2,1,6) x(2,2,7) x(2,3,9) x(3,1,5) x(3,2,2) x(3,3,1)",""],
        ["x(1,1,7) x(1,2,3) x(1,3,8) x(2,1,6) x(2,2,5) x(2,3,9) x(3,1,4) x(3,2,2) x(3,3,1)",""],
        ["x(1,1,4) x(1,2,3) x(1,3,8) x(2,1,6) x(2,2,5) x(2,3,9) x(3,1,7) x(3,2,2) x(3,3,1)",""],
        ["x(1,1,6) x(1,2,3) x(1,3,8) x(2,1,4) x(2,2,5) x(2,3,9) x(3,1,7) x(3,2,2) x(3,3,1)",""],
        ["x(1,1,6) x(1,2,3) x(1,3,8) x(2,1,7) x(2,2,5) x(2,3,9) x(3,1,4) x(3,2,2) x(3,3,1)",""],
        ["x(1,1,6) x(1,2,3) x(1,3,8) x(2,1,5) x(2,2,7) x(2,3,9) x(3,1,4) x(3,2,2) x(3,3,1)",""],
        ["x(1,1,6) x(1,2,3) x(1,3,8) x(2,1,4) x(2,2,7) x(2,3,9) x(3,1,5) x(3,2,2) x(3,3,1)",""],
        ["x(1,1,6) x(1,2,3) x(1,3,8) x(2,1,5) x(2,2,4) x(2,3,9) x(3,1,7) x(3,2,2) x(3,3,1)",""],
        ["x(1,1,6) x(1,2,3) x(1,3,8) x(2,1,7) x(2,2,4) x(2,3,9) x(3,1,5) x(3,2,2) x(3,3,1)",""],
        ["x(1,1,7) x(1,2,3) x(1,3,8) x(2,1,4) x(2,2,5) x(2,3,9) x(3,1,6) x(3,2,2) x(3,3,1)",""],
        ["x(1,1,4) x(1,2,3) x(1,3,8) x(2,1,7) x(2,2,5) x(2,3,9) x(3,1,6) x(3,2,2) x(3,3,1)",""],
        ["x(1,1,4) x(1,2,3) x(1,3,8) x(2,1,5) x(2,2,7) x(2,3,9) x(3,1,6) x(3,2,2) x(3,3,1)",""],
        ["x(1,1,5) x(1,2,3) x(1,3,8) x(2,1,4) x(2,2,7) x(2,3,9) x(3,1,6) x(3,2,2) x(3,3,1)",""],
        ["x(1,1,7) x(1,2,3) x(1,3,8) x(2,1,5) x(2,2,4) x(2,3,9) x(3,1,6) x(3,2,2) x(3,3,1)",""],
        ["x(1,1,5) x(1,2,3) x(1,3,8) x(2,1,7) x(2,2,4) x(2,3,9) x(3,1,6) x(3,2,2) x(3,3,1)",""],
        ["x(1,1,7) x(1,2,3) x(1,3,8) x(2,1,5) x(2,2,6) x(2,3,9) x(3,1,4) x(3,2,2) x(3,3,1)",""],
        ["x(1,1,4) x(1,2,3) x(1,3,8) x(2,1,5) x(2,2,6) x(2,3,9) x(3,1,7) x(3,2,2) x(3,3,1)",""],
        ["x(1,1,7) x(1,2,3) x(1,3,8) x(2,1,4) x(2,2,6) x(2,3,9) x(3,1,5) x(3,2,2) x(3,3,1)",""],
        ["x(1,1,4) x(1,2,3) x(1,3,8) x(2,1,7) x(2,2,6) x(2,3,9) x(3,1,5) x(3,2,2) x(3,3,1)",""],
        ["x(1,1,5) x(1,2,3) x(1,3,8) x(2,1,4) x(2,2,6) x(2,3,9) x(3,1,7) x(3,2,2) x(3,3,1)",""],
        ["x(1,1,5) x(1,2,3) x(1,3,8) x(2,1,7) x(2,2,6) x(2,3,9) x(3,1,4) x(3,2,2) x(3,3,1)",""],
        ["x(1,1,7) x(1,2,5) x(1,3,8) x(2,1,4) x(2,2,6) x(2,3,9) x(3,1,3) x(3,2,2) x(3,3,1)",""],
        ["x(1,1,3) x(1,2,5) x(1,3,8) x(2,1,4) x(2,2,6) x(2,3,9) x(3,1,7) x(3,2,2) x(3,3,1)",""],
        ["x(1,1,7) x(1,2,5) x(1,3,8) x(2,1,3) x(2,2,6) x(2,3,9) x(3,1,4) x(3,2,2) x(3,3,1)",""],
        ["x(1,1,3) x(1,2,5) x(1,3,8) x(2,1,7) x(2,2,6) x(2,3,9) x(3,1,4) x(3,2,2) x(3,3,1)",""],
        ["x(1,1,4) x(1,2,5) x(1,3,8) x(2,1,7) x(2,2,6) x(2,3,9) x(3,1,3) x(3,2,2) x(3,3,1)",""],
        ["x(1,1,4) x(1,2,5) x(1,3,8) x(2,1,3) x(2,2,6) x(2,3,9) x(3,1,7) x(3,2,2) x(3,3,1)",""],
        ["x(1,1,3) x(1,2,6) x(1,3,8) x(2,1,4) x(2,2,5) x(2,3,9) x(3,1,7) x(3,2,2) x(3,3,1)",""],
        ["x(1,1,7) x(1,2,6) x(1,3,8) x(2,1,4) x(2,2,5) x(2,3,9) x(3,1,3) x(3,2,2) x(3,3,1)",""],
        ["x(1,1,3) x(1,2,6) x(1,3,8) x(2,1,7) x(2,2,5) x(2,3,9) x(3,1,4) x(3,2,2) x(3,3,1)",""],
        ["x(1,1,7) x(1,2,6) x(1,3,8) x(2,1,3) x(2,2,5) x(2,3,9) x(3,1,4) x(3,2,2) x(3,3,1)",""],
        ["x(1,1,4) x(1,2,6) x(1,3,8) x(2,1,7) x(2,2,5) x(2,3,9) x(3,1,3) x(3,2,2) x(3,3,1)",""],
        ["x(1,1,4) x(1,2,6) x(1,3,8) x(2,1,3) x(2,2,5) x(2,3,9) x(3,1,7) x(3,2,2) x(3,3,1)",""],
        ["x(1,1,6) x(1,2,7) x(1,3,8) x(2,1,4) x(2,2,5) x(2,3,9) x(3,1,3) x(3,2,2) x(3,3,1)",""],
        ["x(1,1,6) x(1,2,5) x(1,3,8) x(2,1,4) x(2,2,7) x(2,3,9) x(3,1,3) x(3,2,2) x(3,3,1)",""],
        ["x(1,1,3) x(1,2,7) x(1,3,8) x(2,1,4) x(2,2,5) x(2,3,9) x(3,1,6) x(3,2,2) x(3,3,1)",""],
        ["x(1,1,3) x(1,2,5) x(1,3,8) x(2,1,4) x(2,2,7) x(2,3,9) x(3,1,6) x(3,2,2) x(3,3,1)",""],
        ["x(1,1,4) x(1,2,7) x(1,3,8) x(2,1,6) x(2,2,5) x(2,3,9) x(3,1,3) x(3,2,2) x(3,3,1)",""],
        ["x(1,1,4) x(1,2,5) x(1,3,8) x(2,1,6) x(2,2,7) x(2,3,9) x(3,1,3) x(3,2,2) x(3,3,1)",""],
        ["x(1,1,4) x(1,2,7) x(1,3,8) x(2,1,3) x(2,2,5) x(2,3,9) x(3,1,6) x(3,2,2) x(3,3,1)",""],
        ["x(1,1,4) x(1,2,5) x(1,3,8) x(2,1,3) x(2,2,7) x(2,3,9) x(3,1,6) x(3,2,2) x(3,3,1)",""],
        ["x(1,1,3) x(1,2,7) x(1,3,8) x(2,1,6) x(2,2,5) x(2,3,9) x(3,1,4) x(3,2,2) x(3,3,1)",""],
        ["x(1,1,3) x(1,2,5) x(1,3,8) x(2,1,6) x(2,2,7) x(2,3,9) x(3,1,4) x(3,2,2) x(3,3,1)",""],
        ["x(1,1,6) x(1,2,7) x(1,3,8) x(2,1,3) x(2,2,5) x(2,3,9) x(3,1,4) x(3,2,2) x(3,3,1)",""],
        ["x(1,1,6) x(1,2,5) x(1,3,8) x(2,1,3) x(2,2,7) x(2,3,9) x(3,1,4) x(3,2,2) x(3,3,1)",""],
        ["x(1,1,3) x(1,2,4) x(1,3,8) x(2,1,6) x(2,2,5) x(2,3,9) x(3,1,7) x(3,2,2) x(3,3,1)",""],
        ["x(1,1,7) x(1,2,4) x(1,3,8) x(2,1,6) x(2,2,5) x(2,3,9) x(3,1,3) x(3,2,2) x(3,3,1)",""],
        ["x(1,1,7) x(1,2,4) x(1,3,8) x(2,1,3) x(2,2,5) x(2,3,9) x(3,1,6) x(3,2,2) x(3,3,1)",""],
        ["x(1,1,3) x(1,2,4) x(1,3,8) x(2,1,7) x(2,2,5) x(2,3,9) x(3,1,6) x(3,2,2) x(3,3,1)",""],
        ["x(1,1,6) x(1,2,4) x(1,3,8) x(2,1,7) x(2,2,5) x(2,3,9) x(3,1,3) x(3,2,2) x(3,3,1)",""],
        ["x(1,1,6) x(1,2,4) x(1,3,8) x(2,1,3) x(2,2,5) x(2,3,9) x(3,1,7) x(3,2,2) x(3,3,1)",""],
        ["x(1,1,3) x(1,2,5) x(1,3,8) x(2,1,6) x(2,2,4) x(2,3,9) x(3,1,7) x(3,2,2) x(3,3,1)",""],
        ["x(1,1,7) x(1,2,5) x(1,3,8) x(2,1,6) x(2,2,4) x(2,3,9) x(3,1,3) x(3,2,2) x(3,3,1)",""],
        ["x(1,1,3) x(1,2,5) x(1,3,8) x(2,1,7) x(2,2,4) x(2,3,9) x(3,1,6) x(3,2,2) x(3,3,1)",""],
        ["x(1,1,7) x(1,2,5) x(1,3,8) x(2,1,3) x(2,2,4) x(2,3,9) x(3,1,6) x(3,2,2) x(3,3,1)",""],
        ["x(1,1,6) x(1,2,5) x(1,3,8) x(2,1,7) x(2,2,4) x(2,3,9) x(3,1,3) x(3,2,2) x(3,3,1)",""],
        ["x(1,1,6) x(1,2,5) x(1,3,8) x(2,1,3) x(2,2,4) x(2,3,9) x(3,1,7) x(3,2,2) x(3,3,1)",""],
        ["x(1,1,3) x(1,2,7) x(1,3,8) x(2,1,4) x(2,2,6) x(2,3,9) x(3,1,5) x(3,2,2) x(3,3,1)",""],
        ["x(1,1,5) x(1,2,7) x(1,3,8) x(2,1,4) x(2,2,6) x(2,3,9) x(3,1,3) x(3,2,2) x(3,3,1)",""],
        ["x(1,1,3) x(1,2,7) x(1,3,8) x(2,1,5) x(2,2,6) x(2,3,9) x(3,1,4) x(3,2,2) x(3,3,1)",""],
        ["x(1,1,5) x(1,2,7) x(1,3,8) x(2,1,3) x(2,2,6) x(2,3,9) x(3,1,4) x(3,2,2) x(3,3,1)",""],
        ["x(1,1,4) x(1,2,7) x(1,3,8) x(2,1,5) x(2,2,6) x(2,3,9) x(3,1,3) x(3,2,2) x(3,3,1)",""],
        ["x(1,1,4) x(1,2,7) x(1,3,8) x(2,1,3) x(2,2,6) x(2,3,9) x(3,1,5) x(3,2,2) x(3,3,1)",""],
        ["x(1,1,5) x(1,2,6) x(1,3,8) x(2,1,4) x(2,2,7) x(2,3,9) x(3,1,3) x(3,2,2) x(3,3,1)",""],
        ["x(1,1,3) x(1,2,6) x(1,3,8) x(2,1,4) x(2,2,7) x(2,3,9) x(3,1,5) x(3,2,2) x(3,3,1)",""],
        ["x(1,1,3) x(1,2,6) x(1,3,8) x(2,1,5) x(2,2,7) x(2,3,9) x(3,1,4) x(3,2,2) x(3,3,1)",""],
        ["x(1,1,5) x(1,2,6) x(1,3,8) x(2,1,3) x(2,2,7) x(2,3,9) x(3,1,4) x(3,2,2) x(3,3,1)",""],
        ["x(1,1,4) x(1,2,6) x(1,3,8) x(2,1,5) x(2,2,7) x(2,3,9) x(3,1,3) x(3,2,2) x(3,3,1)",""],
        ["x(1,1,4) x(1,2,6) x(1,3,8) x(2,1,3) x(2,2,7) x(2,3,9) x(3,1,5) x(3,2,2) x(3,3,1)",""],
        ["x(1,1,3) x(1,2,4) x(1,3,8) x(2,1,5) x(2,2,6) x(2,3,9) x(3,1,7) x(3,2,2) x(3,3,1)",""],
        ["x(1,1,7) x(1,2,4) x(1,3,8) x(2,1,5) x(2,2,6) x(2,3,9) x(3,1,3) x(3,2,2) x(3,3,1)",""],
        ["x(1,1,5) x(1,2,4) x(1,3,8) x(2,1,3) x(2,2,6) x(2,3,9) x(3,1,7) x(3,2,2) x(3,3,1)",""],
        ["x(1,1,5) x(1,2,4) x(1,3,8) x(2,1,7) x(2,2,6) x(2,3,9) x(3,1,3) x(3,2,2) x(3,3,1)",""],
        ["x(1,1,7) x(1,2,4) x(1,3,8) x(2,1,3) x(2,2,6) x(2,3,9) x(3,1,5) x(3,2,2) x(3,3,1)",""],
        ["x(1,1,3) x(1,2,4) x(1,3,8) x(2,1,7) x(2,2,6) x(2,3,9) x(3,1,5) x(3,2,2) x(3,3,1)",""],
        ["x(1,1,7) x(1,2,6) x(1,3,8) x(2,1,5) x(2,2,4) x(2,3,9) x(3,1,3) x(3,2,2) x(3,3,1)",""],
        ["x(1,1,3) x(1,2,6) x(1,3,8) x(2,1,5) x(2,2,4) x(2,3,9) x(3,1,7) x(3,2,2) x(3,3,1)",""],
        ["x(1,1,5) x(1,2,6) x(1,3,8) x(2,1,7) x(2,2,4) x(2,3,9) x(3,1,3) x(3,2,2) x(3,3,1)",""],
        ["x(1,1,5) x(1,2,6) x(1,3,8) x(2,1,3) x(2,2,4) x(2,3,9) x(3,1,7) x(3,2,2) x(3,3,1)",""],
        ["x(1,1,3) x(1,2,6) x(1,3,8) x(2,1,7) x(2,2,4) x(2,3,9) x(3,1,5) x(3,2,2) x(3,3,1)",""],
        ["x(1,1,7) x(1,2,6) x(1,3,8) x(2,1,3) x(2,2,4) x(2,3,9) x(3,1,5) x(3,2,2) x(3,3,1)",""],
        ["x(1,1,6) x(1,2,4) x(1,3,8) x(2,1,5) x(2,2,7) x(2,3,9) x(3,1,3) x(3,2,2) x(3,3,1)",""],
        ["x(1,1,6) x(1,2,7) x(1,3,8) x(2,1,5) x(2,2,4) x(2,3,9) x(3,1,3) x(3,2,2) x(3,3,1)",""],
        ["x(1,1,5) x(1,2,4) x(1,3,8) x(2,1,3) x(2,2,7) x(2,3,9) x(3,1,6) x(3,2,2) x(3,3,1)",""],
        ["x(1,1,5) x(1,2,7) x(1,3,8) x(2,1,3) x(2,2,4) x(2,3,9) x(3,1,6) x(3,2,2) x(3,3,1)",""],
        ["x(1,1,5) x(1,2,4) x(1,3,8) x(2,1,6) x(2,2,7) x(2,3,9) x(3,1,3) x(3,2,2) x(3,3,1)",""],
        ["x(1,1,5) x(1,2,7) x(1,3,8) x(2,1,6) x(2,2,4) x(2,3,9) x(3,1,3) x(3,2,2) x(3,3,1)",""],
        ["x(1,1,6) x(1,2,4) x(1,3,8) x(2,1,3) x(2,2,7) x(2,3,9) x(3,1,5) x(3,2,2) x(3,3,1)",""],
        ["x(1,1,6) x(1,2,7) x(1,3,8) x(2,1,3) x(2,2,4) x(2,3,9) x(3,1,5) x(3,2,2) x(3,3,1)",""],
        ["x(1,1,3) x(1,2,4) x(1,3,8) x(2,1,5) x(2,2,7) x(2,3,9) x(3,1,6) x(3,2,2) x(3,3,1)",""],
        ["x(1,1,3) x(1,2,7) x(1,3,8) x(2,1,5) x(2,2,4) x(2,3,9) x(3,1,6) x(3,2,2) x(3,3,1)",""],
        ["x(1,1,3) x(1,2,4) x(1,3,8) x(2,1,6) x(2,2,7) x(2,3,9) x(3,1,5) x(3,2,2) x(3,3,1)",""],
        ["x(1,1,3) x(1,2,7) x(1,3,8) x(2,1,6) x(2,2,4) x(2,3,9) x(3,1,5) x(3,2,2) x(3,3,1)",""],
        ["x(1,1,7) x(1,2,3) x(1,3,8) x(2,1,5) x(2,2,2) x(2,3,9) x(3,1,6) x(3,2,4) x(3,3,1)",""],
        ["x(1,1,7) x(1,2,4) x(1,3,8) x(2,1,5) x(2,2,2) x(2,3,9) x(3,1,6) x(3,2,3) x(3,3,1)",""],
        ["x(1,1,6) x(1,2,3) x(1,3,8) x(2,1,5) x(2,2,2) x(2,3,9) x(3,1,7) x(3,2,4) x(3,3,1)",""],
        ["x(1,1,6) x(1,2,4) x(1,3,8) x(2,1,5) x(2,2,2) x(2,3,9) x(3,1,7) x(3,2,3) x(3,3,1)",""],
        ["x(1,1,7) x(1,2,4) x(1,3,8) x(2,1,5) x(2,2,2) x(2,3,9) x(3,1,3) x(3,2,6) x(3,3,1)",""],
        ["x(1,1,7) x(1,2,6) x(1,3,8) x(2,1,5) x(2,2,2) x(2,3,9) x(3,1,3) x(3,2,4) x(3,3,1)",""],
        ["x(1,1,6) x(1,2,7) x(1,3,8) x(2,1,5) x(2,2,2) x(2,3,9) x(3,1,3) x(3,2,4) x(3,3,1)",""],
        ["x(1,1,6) x(1,2,4) x(1,3,8) x(2,1,5) x(2,2,2) x(2,3,9) x(3,1,3) x(3,2,7) x(3,3,1)",""],
        ["x(1,1,5) x(1,2,4) x(1,3,8) x(2,1,6) x(2,2,2) x(2,3,9) x(3,1,7) x(3,2,3) x(3,3,1)",""],
        ["x(1,1,5) x(1,2,3) x(1,3,8) x(2,1,6) x(2,2,2) x(2,3,9) x(3,1,7) x(3,2,4) x(3,3,1)",""],
        ["x(1,1,5) x(1,2,4) x(1,3,8) x(2,1,7) x(2,2,2) x(2,3,9) x(3,1,6) x(3,2,3) x(3,3,1)",""],
        ["x(1,1,5) x(1,2,3) x(1,3,8) x(2,1,7) x(2,2,2) x(2,3,9) x(3,1,6) x(3,2,4) x(3,3,1)",""],
        ["x(1,1,5) x(1,2,4) x(1,3,8) x(2,1,3) x(2,2,2) x(2,3,9) x(3,1,7) x(3,2,6) x(3,3,1)",""],
        ["x(1,1,5) x(1,2,6) x(1,3,8) x(2,1,3) x(2,2,2) x(2,3,9) x(3,1,7) x(3,2,4) x(3,3,1)",""],
        ["x(1,1,5) x(1,2,4) x(1,3,8) x(2,1,3) x(2,2,2) x(2,3,9) x(3,1,6) x(3,2,7) x(3,3,1)",""],
        ["x(1,1,5) x(1,2,7) x(1,3,8) x(2,1,3) x(2,2,2) x(2,3,9) x(3,1,6) x(3,2,4) x(3,3,1)",""],
        ["x(1,1,7) x(1,2,5) x(1,3,8) x(2,1,3) x(2,2,2) x(2,3,9) x(3,1,6) x(3,2,4) x(3,3,1)",""],
        ["x(1,1,7) x(1,2,4) x(1,3,8) x(2,1,3) x(2,2,2) x(2,3,9) x(3,1,6) x(3,2,5) x(3,3,1)",""],
        ["x(1,1,6) x(1,2,5) x(1,3,8) x(2,1,3) x(2,2,2) x(2,3,9) x(3,1,7) x(3,2,4) x(3,3,1)",""],
        ["x(1,1,6) x(1,2,4) x(1,3,8) x(2,1,3) x(2,2,2) x(2,3,9) x(3,1,7) x(3,2,5) x(3,3,1)",""],
        ["x(1,1,5) x(1,2,7) x(1,3,8) x(2,1,6) x(2,2,2) x(2,3,9) x(3,1,3) x(3,2,4) x(3,3,1)",""],
        ["x(1,1,5) x(1,2,4) x(1,3,8) x(2,1,6) x(2,2,2) x(2,3,9) x(3,1,3) x(3,2,7) x(3,3,1)",""],
        ["x(1,1,5) x(1,2,4) x(1,3,8) x(2,1,7) x(2,2,2) x(2,3,9) x(3,1,3) x(3,2,6) x(3,3,1)",""],
        ["x(1,1,5) x(1,2,6) x(1,3,8) x(2,1,7) x(2,2,2) x(2,3,9) x(3,1,3) x(3,2,4) x(3,3,1)",""],
        ["x(1,1,7) x(1,2,4) x(1,3,8) x(2,1,6) x(2,2,2) x(2,3,9) x(3,1,3) x(3,2,5) x(3,3,1)",""],
        ["x(1,1,7) x(1,2,5) x(1,3,8) x(2,1,6) x(2,2,2) x(2,3,9) x(3,1,3) x(3,2,4) x(3,3,1)",""],
        ["x(1,1,6) x(1,2,4) x(1,3,8) x(2,1,7) x(2,2,2) x(2,3,9) x(3,1,3) x(3,2,5) x(3,3,1)",""],
        ["x(1,1,6) x(1,2,5) x(1,3,8) x(2,1,7) x(2,2,2) x(2,3,9) x(3,1,3) x(3,2,4) x(3,3,1)",""],
        ["x(1,1,7) x(1,2,4) x(1,3,8) x(2,1,3) x(2,2,2) x(2,3,9) x(3,1,5) x(3,2,6) x(3,3,1)",""],
        ["x(1,1,7) x(1,2,6) x(1,3,8) x(2,1,3) x(2,2,2) x(2,3,9) x(3,1,5) x(3,2,4) x(3,3,1)",""],
        ["x(1,1,6) x(1,2,4) x(1,3,8) x(2,1,3) x(2,2,2) x(2,3,9) x(3,1,5) x(3,2,7) x(3,3,1)",""],
        ["x(1,1,6) x(1,2,7) x(1,3,8) x(2,1,3) x(2,2,2) x(2,3,9) x(3,1,5) x(3,2,4) x(3,3,1)",""],
        ["x(1,1,7) x(1,2,4) x(1,3,8) x(2,1,6) x(2,2,2) x(2,3,9) x(3,1,5) x(3,2,3) x(3,3,1)",""],
        ["x(1,1,7) x(1,2,3) x(1,3,8) x(2,1,6) x(2,2,2) x(2,3,9) x(3,1,5) x(3,2,4) x(3,3,1)",""],
        ["x(1,1,6) x(1,2,4) x(1,3,8) x(2,1,7) x(2,2,2) x(2,3,9) x(3,1,5) x(3,2,3) x(3,3,1)",""],
        ["x(1,1,6) x(1,2,3) x(1,3,8) x(2,1,7) x(2,2,2) x(2,3,9) x(3,1,5) x(3,2,4) x(3,3,1)",""],
        ["x(1,1,3) x(1,2,4) x(1,3,8) x(2,1,5) x(2,2,2) x(2,3,9) x(3,1,7) x(3,2,6) x(3,3,1)",""],
        ["x(1,1,3) x(1,2,6) x(1,3,8) x(2,1,5) x(2,2,2) x(2,3,9) x(3,1,7) x(3,2,4) x(3,3,1)",""],
        ["x(1,1,3) x(1,2,4) x(1,3,8) x(2,1,5) x(2,2,2) x(2,3,9) x(3,1,6) x(3,2,7) x(3,3,1)",""],
        ["x(1,1,3) x(1,2,7) x(1,3,8) x(2,1,5) x(2,2,2) x(2,3,9) x(3,1,6) x(3,2,4) x(3,3,1)",""],
        ["x(1,1,3) x(1,2,4) x(1,3,8) x(2,1,6) x(2,2,2) x(2,3,9) x(3,1,7) x(3,2,5) x(3,3,1)",""],
        ["x(1,1,3) x(1,2,5) x(1,3,8) x(2,1,6) x(2,2,2) x(2,3,9) x(3,1,7) x(3,2,4) x(3,3,1)",""],
        ["x(1,1,3) x(1,2,4) x(1,3,8) x(2,1,7) x(2,2,2) x(2,3,9) x(3,1,6) x(3,2,5) x(3,3,1)",""],
        ["x(1,1,3) x(1,2,5) x(1,3,8) x(2,1,7) x(2,2,2) x(2,3,9) x(3,1,6) x(3,2,4) x(3,3,1)",""],
        ["x(1,1,3) x(1,2,4) x(1,3,8) x(2,1,6) x(2,2,2) x(2,3,9) x(3,1,5) x(3,2,7) x(3,3,1)",""],
        ["x(1,1,3) x(1,2,7) x(1,3,8) x(2,1,6) x(2,2,2) x(2,3,9) x(3,1,5) x(3,2,4) x(3,3,1)",""],
        ["x(1,1,3) x(1,2,4) x(1,3,8) x(2,1,7) x(2,2,2) x(2,3,9) x(3,1,5) x(3,2,6) x(3,3,1)",""],
        ["x(1,1,3) x(1,2,6) x(1,3,8) x(2,1,7) x(2,2,2) x(2,3,9) x(3,1,5) x(3,2,4) x(3,3,1)",""],
        ["x(1,1,4) x(1,2,7) x(1,3,8) x(2,1,5) x(2,2,2) x(2,3,9) x(3,1,3) x(3,2,6) x(3,3,1)",""],
        ["x(1,1,4) x(1,2,6) x(1,3,8) x(2,1,5) x(2,2,2) x(2,3,9) x(3,1,3) x(3,2,7) x(3,3,1)",""],
        ["x(1,1,4) x(1,2,3) x(1,3,8) x(2,1,5) x(2,2,2) x(2,3,9) x(3,1,7) x(3,2,6) x(3,3,1)",""],
        ["x(1,1,4) x(1,2,6) x(1,3,8) x(2,1,5) x(2,2,2) x(2,3,9) x(3,1,7) x(3,2,3) x(3,3,1)",""],
        ["x(1,1,4) x(1,2,7) x(1,3,8) x(2,1,5) x(2,2,2) x(2,3,9) x(3,1,6) x(3,2,3) x(3,3,1)",""],
        ["x(1,1,4) x(1,2,3) x(1,3,8) x(2,1,5) x(2,2,2) x(2,3,9) x(3,1,6) x(3,2,7) x(3,3,1)",""],
        ["x(1,1,4) x(1,2,5) x(1,3,8) x(2,1,3) x(2,2,2) x(2,3,9) x(3,1,7) x(3,2,6) x(3,3,1)",""],
        ["x(1,1,4) x(1,2,6) x(1,3,8) x(2,1,3) x(2,2,2) x(2,3,9) x(3,1,7) x(3,2,5) x(3,3,1)",""],
        ["x(1,1,4) x(1,2,7) x(1,3,8) x(2,1,3) x(2,2,2) x(2,3,9) x(3,1,6) x(3,2,5) x(3,3,1)",""],
        ["x(1,1,4) x(1,2,5) x(1,3,8) x(2,1,3) x(2,2,2) x(2,3,9) x(3,1,6) x(3,2,7) x(3,3,1)",""],
        ["x(1,1,4) x(1,2,7) x(1,3,8) x(2,1,3) x(2,2,2) x(2,3,9) x(3,1,5) x(3,2,6) x(3,3,1)",""],
        ["x(1,1,4) x(1,2,6) x(1,3,8) x(2,1,3) x(2,2,2) x(2,3,9) x(3,1,5) x(3,2,7) x(3,3,1)",""],
        ["x(1,1,4) x(1,2,7) x(1,3,8) x(2,1,6) x(2,2,2) x(2,3,9) x(3,1,3) x(3,2,5) x(3,3,1)",""],
        ["x(1,1,4) x(1,2,5) x(1,3,8) x(2,1,6) x(2,2,2) x(2,3,9) x(3,1,3) x(3,2,7) x(3,3,1)",""],
        ["x(1,1,4) x(1,2,3) x(1,3,8) x(2,1,6) x(2,2,2) x(2,3,9) x(3,1,7) x(3,2,5) x(3,3,1)",""],
        ["x(1,1,4) x(1,2,5) x(1,3,8) x(2,1,6) x(2,2,2) x(2,3,9) x(3,1,7) x(3,2,3) x(3,3,1)",""],
        ["x(1,1,4) x(1,2,5) x(1,3,8) x(2,1,7) x(2,2,2) x(2,3,9) x(3,1,3) x(3,2,6) x(3,3,1)",""],
        ["x(1,1,4) x(1,2,6) x(1,3,8) x(2,1,7) x(2,2,2) x(2,3,9) x(3,1,3) x(3,2,5) x(3,3,1)",""],
        ["x(1,1,4) x(1,2,3) x(1,3,8) x(2,1,7) x(2,2,2) x(2,3,9) x(3,1,6) x(3,2,5) x(3,3,1)",""],
        ["x(1,1,4) x(1,2,5) x(1,3,8) x(2,1,7) x(2,2,2) x(2,3,9) x(3,1,6) x(3,2,3) x(3,3,1)",""],
        ["x(1,1,4) x(1,2,3) x(1,3,8) x(2,1,6) x(2,2,2) x(2,3,9) x(3,1,5) x(3,2,7) x(3,3,1)",""],
        ["x(1,1,4) x(1,2,7) x(1,3,8) x(2,1,6) x(2,2,2) x(2,3,9) x(3,1,5) x(3,2,3) x(3,3,1)",""],
        ["x(1,1,4) x(1,2,3) x(1,3,8) x(2,1,7) x(2,2,2) x(2,3,9) x(3,1,5) x(3,2,6) x(3,3,1)",""],
        ["x(1,1,4) x(1,2,6) x(1,3,8) x(2,1,7) x(2,2,2) x(2,3,9) x(3,1,5) x(3,2,3) x(3,3,1)",""],
        ["x(1,1,3) x(1,2,7) x(1,3,8) x(2,1,5) x(2,2,2) x(2,3,9) x(3,1,4) x(3,2,6) x(3,3,1)",""],
        ["x(1,1,3) x(1,2,6) x(1,3,8) x(2,1,5) x(2,2,2) x(2,3,9) x(3,1,4) x(3,2,7) x(3,3,1)",""],
        ["x(1,1,3) x(1,2,7) x(1,3,8) x(2,1,6) x(2,2,2) x(2,3,9) x(3,1,4) x(3,2,5) x(3,3,1)",""],
        ["x(1,1,3) x(1,2,5) x(1,3,8) x(2,1,6) x(2,2,2) x(2,3,9) x(3,1,4) x(3,2,7) x(3,3,1)",""],
        ["x(1,1,3) x(1,2,5) x(1,3,8) x(2,1,4) x(2,2,2) x(2,3,9) x(3,1,7) x(3,2,6) x(3,3,1)",""],
        ["x(1,1,3) x(1,2,6) x(1,3,8) x(2,1,4) x(2,2,2) x(2,3,9) x(3,1,7) x(3,2,5) x(3,3,1)",""],
        ["x(1,1,3) x(1,2,7) x(1,3,8) x(2,1,4) x(2,2,2) x(2,3,9) x(3,1,6) x(3,2,5) x(3,3,1)",""],
        ["x(1,1,3) x(1,2,5) x(1,3,8) x(2,1,4) x(2,2,2) x(2,3,9) x(3,1,6) x(3,2,7) x(3,3,1)",""]
    ]
    
    lbh : 'list[str]' = [
        "modeh(2, sum_row(+,+)",
        "modeh(2, sum_col(+,+)"
    ]
    
    lbb : 'list[str]' = [
        "modeb(2, sum_row(+,+)",
        "modeb(2, sum_col(+,+)",
        "modeb(1, size(+))"
    ]
    
    return bg, pe, ne, lbh, lbb


def latin_square():
    '''
    With aggregates: the same element cannot repeat in the same 
    row or column.
    Given:
    cell(1..3).
    val(1..3).
    size(3).
    1{x(R,C,N) : val(N)}1:- cell(R), cell(C).
    Learn:
    count_row(R,S):- S = #count{V : x(R,C,V), cell(C)}, cell(R).
    count_col(C,S):- S = #count{V : x(R,C,V), cell(R)}, cell(C).
    :- count_col(Col,C), size(S), C != S.
    :- count_row(Row,C), size(S), C != S.
    '''
    # https://en.wikipedia.org/wiki/Latin_square
    bg : 'list[str]' = [
        "cell(1..3).",
        "val(1..3).",
        "size(3).",
        "1{x(R,C,N) : val(N)}1:- cell(R), cell(C)."
    ]
    
    # all the existing solutions (12)
    pe : 'list[list[str]]' = [
        ["x(1,3,1) x(1,2,2) x(1,1,3) x(2,2,1) x(2,1,2) x(2,3,3) x(3,1,1) x(3,3,2) x(3,2,3)",""],
        ["x(1,3,1) x(1,1,2) x(1,2,3) x(2,1,1) x(2,2,2) x(2,3,3) x(3,2,1) x(3,3,2) x(3,1,3)",""],
        ["x(1,3,1) x(1,2,2) x(1,1,3) x(2,1,1) x(2,3,2) x(2,2,3) x(3,2,1) x(3,1,2) x(3,3,3)",""],
        ["x(1,3,1) x(1,1,2) x(1,2,3) x(2,2,1) x(2,3,2) x(2,1,3) x(3,1,1) x(3,2,2) x(3,3,3)",""],
        ["x(1,1,1) x(1,3,2) x(1,2,3) x(2,3,1) x(2,2,2) x(2,1,3) x(3,2,1) x(3,1,2) x(3,3,3)",""],
        ["x(1,2,1) x(1,3,2) x(1,1,3) x(2,3,1) x(2,1,2) x(2,2,3) x(3,1,1) x(3,2,2) x(3,3,3)",""],
        ["x(1,2,1) x(1,3,2) x(1,1,3) x(2,1,1) x(2,2,2) x(2,3,3) x(3,3,1) x(3,1,2) x(3,2,3)",""],
        ["x(1,1,1) x(1,3,2) x(1,2,3) x(2,2,1) x(2,1,2) x(2,3,3) x(3,3,1) x(3,2,2) x(3,1,3)",""],
        ["x(1,1,1) x(1,2,2) x(1,3,3) x(2,3,1) x(2,1,2) x(2,2,3) x(3,2,1) x(3,3,2) x(3,1,3)",""],
        ["x(1,1,1) x(1,2,2) x(1,3,3) x(2,2,1) x(2,3,2) x(2,1,3) x(3,3,1) x(3,1,2) x(3,2,3)",""],
        ["x(1,2,1) x(1,1,2) x(1,3,3) x(2,3,1) x(2,2,2) x(2,1,3) x(3,1,1) x(3,3,2) x(3,2,3)",""],
        ["x(1,2,1) x(1,1,2) x(1,3,3) x(2,1,1) x(2,3,2) x(2,2,3) x(3,3,1) x(3,2,2) x(3,1,3)",""]
    ]
    
    ne : 'list[list[str]]' = [
        ["x(2,1,1) x(3,1,2) x(1,1,3) x(2,2,1) x(3,2,2) x(1,2,3) x(2,3,1) x(3,3,2) x(1,3,3)",""],
        ["x(3,1,1) x(2,1,2) x(1,1,3) x(3,2,1) x(2,2,2) x(1,2,3) x(3,3,1) x(2,3,2) x(1,3,3)",""],
        ["x(3,1,1) x(2,1,2) x(1,1,3) x(2,2,1) x(3,2,2) x(1,2,3) x(3,3,1) x(2,3,2) x(1,3,3)",""],
        ["x(3,1,1) x(2,1,2) x(1,1,3) x(2,2,1) x(3,2,2) x(1,2,3) x(2,3,1) x(3,3,2) x(1,3,3)",""],
        ["x(3,1,1) x(2,1,2) x(1,1,3) x(3,2,1) x(2,2,2) x(1,2,3) x(2,3,1) x(3,3,2) x(1,3,3)",""],
        ["x(2,1,1) x(3,1,2) x(1,1,3) x(2,2,1) x(3,2,2) x(1,2,3) x(3,3,1) x(2,3,2) x(1,3,3)",""],
        ["x(2,1,1) x(3,1,2) x(1,1,3) x(3,2,1) x(2,2,2) x(1,2,3) x(3,3,1) x(2,3,2) x(1,3,3)",""],
        ["x(2,1,1) x(3,1,2) x(1,1,3) x(3,2,1) x(2,2,2) x(1,2,3) x(2,3,1) x(3,3,2) x(1,3,3)",""],
        ["x(2,1,1) x(3,1,2) x(1,1,3) x(2,2,1) x(3,2,2) x(1,2,3) x(3,3,1) x(1,3,2) x(2,3,3)",""],
        ["x(2,1,1) x(3,1,2) x(1,1,3) x(2,2,1) x(3,2,2) x(1,2,3) x(2,3,1) x(1,3,2) x(3,3,3)",""],
        ["x(1,2,1) x(1,1,2) x(1,3,3) x(2,3,1) x(2,1,2) x(2,2,3) x(3,2,1) x(3,1,2) x(3,3,3)",""],
        ["x(1,2,1) x(1,1,2) x(1,3,3) x(2,3,1) x(2,1,2) x(2,2,3) x(3,2,1) x(3,3,2) x(3,1,3)",""],
        ["x(1,3,1) x(1,1,2) x(1,2,3) x(2,3,1) x(2,1,2) x(2,2,3) x(3,3,1) x(3,1,2) x(3,2,3)",""],
        ["x(1,3,1) x(1,1,2) x(1,2,3) x(2,3,1) x(2,1,2) x(2,2,3) x(3,3,1) x(3,2,2) x(3,1,3)",""],
        ["x(1,3,1) x(1,1,2) x(1,2,3) x(2,3,1) x(2,1,2) x(2,2,3) x(3,2,1) x(3,1,2) x(3,3,3)",""],
        ["x(1,3,1) x(1,2,2) x(1,1,3) x(2,3,1) x(2,1,2) x(2,2,3) x(3,3,1) x(3,1,2) x(3,2,3)",""],
        ["x(1,3,1) x(1,2,2) x(1,1,3) x(2,3,1) x(2,1,2) x(2,2,3) x(3,3,1) x(3,2,2) x(3,1,3)",""],
        ["x(1,3,1) x(1,2,2) x(1,1,3) x(2,3,1) x(2,1,2) x(2,2,3) x(3,2,1) x(3,1,2) x(3,3,3)",""],
        ["x(1,3,1) x(1,1,2) x(1,2,3) x(2,3,1) x(2,1,2) x(2,2,3) x(3,2,1) x(3,3,2) x(3,1,3)",""],
        ["x(1,3,1) x(1,2,2) x(1,1,3) x(2,3,1) x(2,1,2) x(2,2,3) x(3,2,1) x(3,3,2) x(3,1,3)",""],
        ["x(1,1,3) x(2,1,3) x(3,1,3) x(2,2,1) x(1,2,3) x(3,2,3) x(2,3,1) x(1,3,3) x(3,3,3)",""],
        ["x(1,1,3) x(2,1,3) x(3,1,3) x(1,2,1) x(2,2,3) x(3,2,3) x(2,3,1) x(1,3,3) x(3,3,3)",""],
        ["x(1,1,3) x(2,1,3) x(3,1,3) x(1,2,1) x(2,2,1) x(3,2,3) x(2,3,1) x(1,3,3) x(3,3,3)",""],
        ["x(1,1,3) x(2,1,3) x(3,1,3) x(1,2,1) x(2,2,3) x(3,2,3) x(1,3,1) x(2,3,1) x(3,3,3)",""],
        ["x(1,1,3) x(2,1,3) x(3,1,3) x(2,2,1) x(1,2,3) x(3,2,3) x(1,3,1) x(2,3,1) x(3,3,3)",""]
    ]
    
    lbh : 'list[str]' = [
        "modeh(1, count_row(+,+)",
        "modeh(1, count_col(+,+)"
    ]
    
    lbb : 'list[str]' = [
        "modeb(1, count_row(+,+)",
        "modeb(1, count_row(+,+)",
        "modeb(1, size(+))",
        "modeb(1, cell(+))"
    ]
    
    return bg, pe, ne, lbh, lbb
    

def set_partition_sum():
    '''
    Inspired by: http://www.hakank.org/answer_set_programming/set_partition.lp
    Set partition problem: given the set S = {1, 2, ..., n}, 
    find two sets A and B such that:
    - A U B = S
    - sum(A) = sum(B)
    -------------
    Given:
    #const n = 12. 
    val(1..n).
    partition(1..2).
    % split the numbers in two partitions
    1 { p(P, I) : partition(P) } 1 :- val(I).
    % symmetry breaking
    p(1,1).
    Learn:
    sum_partition(Sum,Partition):-
        partition(Partition),
        Sum = #sum{I : p(Partition,I)}.
    :- sum_partition(P0, S1), sum_partition(P1, S2), P0 != P1, S1 != S2.
    '''

    bg : 'list[str]' = [
        "#const n = 12.",
        "val(1..n).",
        "partition(1..2).",
        "1 { p(P, I) : partition(P) } 1 :- val(I).",
        "p(1,1)."
    ]
    
    # 10 of the 62 existing solutions
    pe : 'list[list[str]]' = [
        ["p(1,1) p(1,5) p(1,10) p(1,11) p(1,12) p(2,2) p(2,3) p(2,4) p(2,6) p(2,7) p(2,8) p(2,9)",""],
        ["p(1,1) p(1,4) p(1,5) p(1,8) p(1,10) p(1,11) p(2,2) p(2,3) p(2,6) p(2,7) p(2,9) p(2,12)",""],
        ["p(1,1) p(1,3) p(1,5) p(1,8) p(1,10) p(1,12) p(2,2) p(2,4) p(2,6) p(2,7) p(2,9) p(2,11)",""],
        ["p(1,1) p(1,3) p(1,4) p(1,8) p(1,11) p(1,12) p(2,2) p(2,5) p(2,6) p(2,7) p(2,9) p(2,10)",""],
        ["p(1,1) p(1,3) p(1,5) p(1,9) p(1,10) p(1,11) p(2,2) p(2,4) p(2,6) p(2,7) p(2,8) p(2,12)",""],
        ["p(1,1) p(1,3) p(1,4) p(1,9) p(1,10) p(1,12) p(2,2) p(2,5) p(2,6) p(2,7) p(2,8) p(2,11)",""],
        ["p(1,1) p(1,8) p(1,9) p(1,10) p(1,11) p(2,2) p(2,3) p(2,4) p(2,5) p(2,6) p(2,7) p(2,12)",""],
        ["p(1,1) p(1,4) p(1,5) p(1,8) p(1,9) p(1,12) p(2,2) p(2,3) p(2,6) p(2,7) p(2,10) p(2,11)",""],
        ["p(1,1) p(1,4) p(1,5) p(1,7) p(1,10) p(1,12) p(2,2) p(2,3) p(2,6) p(2,8) p(2,9) p(2,11)",""],
        ["p(1,1) p(1,7) p(1,9) p(1,10) p(1,12) p(2,2) p(2,3) p(2,4) p(2,5) p(2,6) p(2,8) p(2,11)",""]
    ]
    
    # some of the 2048 possible placements
    ne : 'list[list[str]]' = [
        ["p(1,1) p(1,4) p(1,6) p(1,7) p(1,8) p(1,9) p(1,11) p(1,12) p(2,2) p(2,3) p(2,5) p(2,10)",""],
        ["p(1,1) p(1,2) p(1,4) p(1,5) p(1,6) p(1,7) p(1,8) p(1,9) p(1,11) p(2,3) p(2,10) p(2,12)",""],
        ["p(1,1) p(1,4) p(1,5) p(1,6) p(1,7) p(1,8) p(1,9) p(1,11) p(2,2) p(2,3) p(2,10) p(2,12)",""],
        ["p(1,1) p(1,2) p(1,4) p(1,6) p(1,7) p(1,8) p(1,9) p(1,11) p(2,3) p(2,5) p(2,10) p(2,12)",""],
        ["p(1,1) p(1,4) p(1,6) p(1,7) p(1,8) p(1,9) p(1,11) p(2,2) p(2,3) p(2,5) p(2,10) p(2,12)",""],
        ["p(1,1) p(1,2) p(1,3) p(1,5) p(1,6) p(1,7) p(1,8) p(1,9) p(1,11) p(1,12) p(2,4) p(2,10)",""],
        ["p(1,1) p(1,2) p(1,5) p(1,6) p(1,7) p(1,8) p(1,9) p(1,11) p(1,12) p(2,3) p(2,4) p(2,10)",""],
        ["p(1,1) p(1,2) p(1,3) p(1,6) p(1,7) p(1,8) p(1,9) p(1,11) p(1,12) p(2,4) p(2,5) p(2,10)",""],
        ["p(1,1) p(1,2) p(1,6) p(1,7) p(1,8) p(1,9) p(1,11) p(1,12) p(2,3) p(2,4) p(2,5) p(2,10)",""],
        ["p(1,1) p(1,2) p(1,3) p(1,5) p(1,6) p(1,7) p(1,8) p(1,9) p(1,11) p(2,4) p(2,10) p(2,12)",""],
        ["p(1,1) p(1,2) p(1,3) p(1,6) p(1,7) p(1,8) p(1,9) p(1,11) p(2,4) p(2,5) p(2,10) p(2,12)",""],
        ["p(1,1) p(2,2) p(2,3) p(2,4) p(2,5) p(2,6) p(2,7) p(2,8) p(2,9) p(2,10) p(2,11) p(2,12)",""],
        ["p(1,1) p(1,3) p(1,4) p(1,5) p(1,6) p(1,7) p(1,8) p(1,9) p(1,10) p(1,11) p(1,12) p(2,2)",""]
    ]
    
    lbh : 'list[str]' = [
        "modeh(1, sum_partition(+,+)"
    ]
    
    lbb : 'list[str]' = [
        "modeb(1, partition(+)",
        "modeb(2, sum_partition(+,+)"
    ]
    
    return bg, pe, ne, lbh, lbb

def set_partition_sum_and_cardinality():
    '''
    Inspired by: http://www.hakank.org/answer_set_programming/set_partition.lp
    Set partition problem: given the set S = {1, 2, ..., n}, 
    find two sets A and B such that:
    - A U B = S
    - sum(A) = sum(B)
    - |A| = |B|
    -------------
    Given:
    #const n = 12. 
    val(1..n).
    partition(1..2).
    % split the numbers in two partitions
    1 { p(P, I) : partition(P) } 1 :- val(I).
    % symmetry breaking
    p(1,1).
    Learn:
    sum_partition(Sum,Partition):-
        partition(Partition),
        Sum = #sum{I : p(Partition,I)}.
    :- sum_partition(P0, S1), sum_partition(P1, S2), P0 != P1, S1 != S2.
    count_partition(Count,Partition):-
        partition(Partition),
        Count = #count{I : p(Partition,I)}.
    :- count_partition(P0, S1), count_partition(P1, S2), P0 != P1, S1 != S2.
    '''

    bg : 'list[str]' = [
        "#const n = 12.",
        "val(1..n).",
        "partition(1..2).",
        "1 { p(P, I) : partition(P) } 1 :- val(I).",
        "p(1,1)."
    ]
    
    # all the 29 existing solutions
    pe : 'list[list[str]]' = [
        ["p(1,1) p(1,4) p(1,5) p(1,8) p(1,9) p(1,12) p(2,2) p(2,3) p(2,6) p(2,7) p(2,10) p(2,11)",""],
        ["p(1,1) p(1,4) p(1,5) p(1,8) p(1,10) p(1,11) p(2,2) p(2,3) p(2,6) p(2,7) p(2,9) p(2,12)",""],
        ["p(1,1) p(1,3) p(1,4) p(1,9) p(1,10) p(1,12) p(2,2) p(2,5) p(2,6) p(2,7) p(2,8) p(2,11)",""],
        ["p(1,1) p(1,3) p(1,5) p(1,9) p(1,10) p(1,11) p(2,2) p(2,4) p(2,6) p(2,7) p(2,8) p(2,12)",""],
        ["p(1,1) p(1,3) p(1,5) p(1,8) p(1,10) p(1,12) p(2,2) p(2,4) p(2,6) p(2,7) p(2,9) p(2,11)",""],
        ["p(1,1) p(1,3) p(1,4) p(1,8) p(1,11) p(1,12) p(2,2) p(2,5) p(2,6) p(2,7) p(2,9) p(2,10)",""],
        ["p(1,1) p(1,4) p(1,5) p(1,7) p(1,10) p(1,12) p(2,2) p(2,3) p(2,6) p(2,8) p(2,9) p(2,11)",""],
        ["p(1,1) p(1,3) p(1,5) p(1,7) p(1,11) p(1,12) p(2,2) p(2,4) p(2,6) p(2,8) p(2,9) p(2,10)",""],
        ["p(1,1) p(1,3) p(1,7) p(1,8) p(1,9) p(1,11) p(2,2) p(2,4) p(2,5) p(2,6) p(2,10) p(2,12)",""],
        ["p(1,1) p(1,4) p(1,7) p(1,8) p(1,9) p(1,10) p(2,2) p(2,3) p(2,5) p(2,6) p(2,11) p(2,12)",""],
        ["p(1,1) p(1,5) p(1,6) p(1,7) p(1,8) p(1,12) p(2,2) p(2,3) p(2,4) p(2,9) p(2,10) p(2,11)",""],
        ["p(1,1) p(1,5) p(1,6) p(1,7) p(1,9) p(1,11) p(2,2) p(2,3) p(2,4) p(2,8) p(2,10) p(2,12)",""],
        ["p(1,1) p(1,5) p(1,6) p(1,8) p(1,9) p(1,10) p(2,2) p(2,3) p(2,4) p(2,7) p(2,11) p(2,12)",""],
        ["p(1,1) p(1,3) p(1,6) p(1,7) p(1,10) p(1,12) p(2,2) p(2,4) p(2,5) p(2,8) p(2,9) p(2,11)",""],
        ["p(1,1) p(1,3) p(1,6) p(1,8) p(1,9) p(1,12) p(2,2) p(2,4) p(2,5) p(2,7) p(2,10) p(2,11)",""],
        ["p(1,1) p(1,3) p(1,6) p(1,8) p(1,10) p(1,11) p(2,2) p(2,4) p(2,5) p(2,7) p(2,9) p(2,12)",""],
        ["p(1,1) p(1,4) p(1,6) p(1,8) p(1,9) p(1,11) p(2,2) p(2,3) p(2,5) p(2,7) p(2,10) p(2,12)",""],
        ["p(1,1) p(1,4) p(1,5) p(1,6) p(1,11) p(1,12) p(2,2) p(2,3) p(2,7) p(2,8) p(2,9) p(2,10)",""],
        ["p(1,1) p(1,4) p(1,6) p(1,7) p(1,10) p(1,11) p(2,2) p(2,3) p(2,5) p(2,8) p(2,9) p(2,12)",""],
        ["p(1,1) p(1,4) p(1,6) p(1,7) p(1,9) p(1,12) p(2,2) p(2,3) p(2,5) p(2,8) p(2,10) p(2,11)",""],
        ["p(1,1) p(1,2) p(1,3) p(1,10) p(1,11) p(1,12) p(2,4) p(2,5) p(2,6) p(2,7) p(2,8) p(2,9)",""],
        ["p(1,1) p(1,2) p(1,5) p(1,9) p(1,10) p(1,12) p(2,3) p(2,4) p(2,6) p(2,7) p(2,8) p(2,11)",""],
        ["p(1,1) p(1,2) p(1,4) p(1,9) p(1,11) p(1,12) p(2,3) p(2,5) p(2,6) p(2,7) p(2,8) p(2,10)",""],
        ["p(1,1) p(1,2) p(1,6) p(1,7) p(1,11) p(1,12) p(2,3) p(2,4) p(2,5) p(2,8) p(2,9) p(2,10)",""],
        ["p(1,1) p(1,2) p(1,6) p(1,8) p(1,10) p(1,12) p(2,3) p(2,4) p(2,5) p(2,7) p(2,9) p(2,11)",""],
        ["p(1,1) p(1,2) p(1,5) p(1,8) p(1,11) p(1,12) p(2,3) p(2,4) p(2,6) p(2,7) p(2,9) p(2,10)",""],
        ["p(1,1) p(1,2) p(1,7) p(1,8) p(1,9) p(1,12) p(2,3) p(2,4) p(2,5) p(2,6) p(2,10) p(2,11)",""],
        ["p(1,1) p(1,2) p(1,7) p(1,8) p(1,10) p(1,11) p(2,3) p(2,4) p(2,5) p(2,6) p(2,9) p(2,12)",""],
        ["p(1,1) p(1,2) p(1,6) p(1,9) p(1,10) p(1,11) p(2,3) p(2,4) p(2,5) p(2,7) p(2,8) p(2,12)",""]
    ]
    
    # some of the 2048 possible placements
    ne : 'list[list[str]]' = [
        ["p(1,1) p(1,2) p(1,6) p(1,7) p(1,11) p(1,12) p(2,3) p(2,4) p(2,5) p(2,8) p(2,9) p(2,10)",""],
        ["p(1,1) p(1,2) p(1,3) p(1,6) p(1,7) p(1,8) p(1,12) p(2,4) p(2,5) p(2,9) p(2,10) p(2,11)",""], 
        ["p(1,1) p(1,2) p(1,6) p(1,7) p(1,8) p(1,9) p(2,3) p(2,4) p(2,5) p(2,10) p(2,11) p(2,12)",""],
        ["p(1,1) p(1,2) p(1,4) p(1,6) p(1,7) p(1,8) p(2,3) p(2,5) p(2,9) p(2,10) p(2,11) p(2,12)",""],
        ["p(1,1) p(1,2) p(1,3) p(1,4) p(1,6) p(1,7) p(1,8) p(1,9) p(1,10) p(2,5) p(2,11) p(2,12)",""],
        ["p(1,1) p(1,2) p(1,3) p(1,5) p(1,6) p(1,7) p(1,8) p(1,9) p(1,10) p(1,12) p(2,4) p(2,11)",""]
    ]
    
    lbh : 'list[str]' = [
        "modeh(1, sum_partition(+,+)",
        "modeh(1, count_partition(+,+)"
    ]
    
    lbb : 'list[str]' = [
        "modeb(1, partition(+)",
        "modeb(2, sum_partition(+,+)",
        "modeb(2, count_partition(+,+)"
    ]
    
    return bg, pe, ne, lbh, lbb


def set_partition_sum_cardinality_and_square():
    '''
    Inspired by: http://www.hakank.org/answer_set_programming/set_partition.lp
    Set partition problem: given the set S = {1, 2, ..., n}, 
    find two sets A and B such that:
    - A U B = S
    - sum(A) = sum(B)
    - |A| = |B|
    - sum of squares of A = sum of squares of B 
    -------------
    Given:
    #const n = 12. 
    val(1..n).
    partition(1..2).
    % split the numbers in two partitions
    1 { p(P, I) : partition(P) } 1 :- val(I).
    % symmetry breaking
    p(1,1).
    % sum of squares
    sq(Partition,Val):- p(Partition,V), Val = V*V.
    Learn (6 rules):
    % NOTE: the aggregation on p/2 can be avoided when the one on sq/2 is used (for this setting)
    count_partition(Count,Partition):-
        partition(Partition),
        Count = #count{I : p(Partition,I)}.
    :- count_partition(P0, S1), count_partition(P1, S2), P0 != P1, S1 != S2.
    sum_partition_sq(Sum,Partition):-
        partition(Partition),
        Sum = #sum{I : sq(Partition,I)}.
    :- sum_partition_sq(P0, S1), sum_partition_sq(P1, S2), P0 != P1, S1 != S2.
    '''

    bg : 'list[str]' = [
        "#const n = 12.",
        "val(1..n).",
        "partition(1..2).",
        "1 { p(P, I) : partition(P) } 1 :- val(I).",
        "p(1,1).",
        "sq(Partition,Val):- p(Partition,V), Val = V*V."
    ]
    
    # only one solution
    pe : 'list[list[str]]' = [
        ["p(1,1) p(2,2) p(1,3) p(2,4) p(2,5) p(2,6) p(1,7) p(1,8) p(1,9) p(2,10) p(1,11) p(2,12)", ""]
    ]
    
    # some of the 2048 possible placements
    ne : 'list[list[str]]' = [
        ["p(1,1) p(1,2) p(2,3) p(2,4) p(2,5) p(1,6) p(2,7) p(1,8) p(2,9) p(1,10) p(2,11) p(1,12)",""],
        ["p(1,1) p(1,2) p(1,3) p(1,4) p(1,5) p(1,6) p(1,7) p(1,8) p(2,9) p(2,10) p(1,11) p(2,12)",""],
        ["p(1,1) p(1,2) p(1,3) p(1,4) p(1,5) p(2,6) p(1,7) p(2,8) p(2,9) p(1,10) p(1,11) p(2,12)",""],
        ["p(1,1) p(2,2) p(1,3) p(1,4) p(1,5) p(2,6) p(1,7) p(2,8) p(1,9) p(2,10) p(2,11) p(1,12)",""],
        ["p(1,1) p(2,2) p(2,3) p(1,4) p(2,5) p(2,6) p(2,7) p(1,8) p(2,9) p(1,10) p(2,11) p(1,12)",""]
    ]
    
    lbh : 'list[str]' = [
        # "modeh(1, sum_partition(+,+)",
        "modeh(1, count_partition(+,+)",
        "modeh(1, sum_partition_sq(+,+)"
    ]
    
    lbb : 'list[str]' = [
        "modeb(1, partition(+)",
        # "modeb(2, sum_partition(+,+)",
        "modeb(2, count_partition(+,+)",
        "modeb(2, sum_partition_sq(+,+)"
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