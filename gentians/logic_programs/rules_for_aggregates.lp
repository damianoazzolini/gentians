% i) all the terms must be different
:- var_pos(V0,P0), 
    var_pos(V1,P1), 
    P0 != P1, 
    aggregate_term_position(A,P0), 
    aggregate_term_position(A,P1),
    V0 = V1.


% ii) all the terms must appear in literals, i.e., remove #count{X:a(Y)}

% ii) all the terms must appear in literals
var_in_term_agg(A,V):- aggregate_term_position(A,VPos), var_pos(V,VPos).
var_in_atom_agg(A,V):- aggregate_atom_position(A,VPos), var_pos(V,VPos).
:- var_in_term_agg(A,V), not var_in_atom_agg(A,V).


% iii) no global variables in tuple of aggregate elements
aggregate_in_position(Pos):-
    aggregate_term_position(_,Pos).
aggregate_in_position(Pos):-
    aggregate_atom_position(_,Pos).
global_var_tuple(Var):- 
    var_pos(Var,Pos0),
    aggregate_term_position(_,Pos0),
    var_pos(Var,Pos1),
    not aggregate_in_position(Pos1),
    Pos0 != Pos1.

:- global_var_tuple(_).
