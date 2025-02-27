% variables in arithm should appear elsewhere and not only in arithm
var_not_in_arithm(Var):-
    var_pos(Var,Pos),
    not all_arithm_term_position(_,Pos).

:- var_pos(Var,Pos), all_arithm_term_position(_,Pos), not var_not_in_arithm(Var).

% impose that arithm operators must have different variables 

:-  arithm_term_position(C,P0),
    result_term_position(C,P1),
    P0 != P1,
    var_pos(Var0,P0),
    var_pos(Var1,P1),
    Var0 == Var1.
