% variables in comparison should appear elsewhere and not only in comparison
var_not_in_comparison(Var):-
    var_pos(Var,Pos),
    not comparison_term_position(_,Pos).

:- var_pos(Var,Pos), comparison_term_position(_,Pos), not var_not_in_comparison(Var).

% impose that comparison operators must have different variables
:- comparison_term_position(C,P0),
    comparison_term_position(C,P1),
    P0 != P1,
    var_pos(Var0,P0),
    var_pos(Var1,P1),
    Var0 == Var1.
