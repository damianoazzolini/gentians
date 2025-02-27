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


cv_head(Var, C):- C = #count{Pos : var_pos(Var,Pos), Pos <= VHI}, var(Var), last_index_var_in_head(VHI).
:- cv_head(Var,CH), cv_body(Var,0), CH > 0.
