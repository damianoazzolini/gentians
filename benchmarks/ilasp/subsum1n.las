0{el(1)}1.
0{el(2)}1.
0{el(3)}1.
0{el(4)}1.
0{el(5)}1.

% 1 ~ s(V0):- V0#sum{V1:el(V1)}V0, v(V0).
% 2 ~ :- V1#sum{V0:el(V0)}V1, s(V1).
% 3 ~ :- V1#sum{V0:el(V0)}V1, v(V1), V1!=V2,s(V2).
% 3 ~ :- V1#sum{V0:el(V0)}V1, v(V1), V2!=V1,s(V2).

2 ~ s(V0):- V0#sum{V1:el(V1)}V0, v(V0).
2 ~ :- V1#sum{V0:el(V0)}V1,s(V1).
2 ~ s(V0):- v(V0), V0#count{V1:el(V1)}V0.
2 ~ :- V1#count{V0:el(V0)}V1,s(V1).
2 ~ :- V1#sum{V0:el(V0)}V1, v(V1), V1!=V2,s(V2).
2 ~ :- V1#sum{V0:el(V0)}V1, v(V1), V2!=V1,s(V2).
2 ~ :- V1#count{V0:el(V0)}V1, v(V1), V1!=V2,s(V2).
2 ~ :- V1#count{V0:el(V0)}V1, v(V1), V2!=V1,s(V2).
2 ~ :- V1#count{V0:el(V0)}V1, v(V1), V1#sum{V0:el(V0)}V1.
2 ~ :- V1#count{V0:el(V0)}V1, v(V1), V1#sum{V2:el(V2)}V1.
2 ~ s(V0):- V0#count{V1:el(V1)}V0, v(V0), V0#sum{V1:el(V1)}V0.
2 ~ s(V0):- V0#count{V1:el(V1)}V0, v(V0), V0#sum{V2:el(V2)}V0.
2 ~ :- V1#count{V0:el(V0)}V1, v(V1), V1#sum{V0:el(V0)}V1,s(V1).
2 ~ :- V1#count{V0:el(V0)}V1, V1#sum{V2:el(V2)}V1,s(V1).
2 ~ :- V1#count{V0:el(V0)}V1, v(V1), v(V2), V2#sum{V0:el(V0)}V2,V1!=V2.
2 ~ :- V1#count{V0:el(V0)}V1, v(V1), v(V2), V2#sum{V0:el(V0)}V2,V2!=V1.


#pos({s(6)},{}).
#neg({s(5)},{}).

% #modeh(1, s(var(t)), (positive)).

v(6).

% #modeh(1, v(const(k)), (positive)).
% #constant(k, 0).
% #constant(k, 1).
% #constant(k, 2).
% #constant(k, 3).
% #constant(k, 4).
% #constant(k, 5).
% #constant(k, 6).
% #constant(k, 7).
% #constant(k, 8).
% #constant(k, 9).
% #constant(k, 10).
% #constant(k, 11).
% #constant(k, 12).
% #constant(k, 13).
% #constant(k, 14).
% #constant(k, 15).