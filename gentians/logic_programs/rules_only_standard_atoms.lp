% no aggregates, arithmetic, and comparison
v_in_head(V):- last_index_var_in_head(I), var_pos(V,P), P <= I.
v_in_body(V):- last_index_var_in_head(I), var_pos(V,P), P > I.
:- v_in_head(V), not v_in_body(V).
