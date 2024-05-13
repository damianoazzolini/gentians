0{el(1,2)}1.
0{el(2,3)}1.
0{el(3,5)}1.
0{el(4,1)}1.
0{el(5,9)}1.

#pos({ok(0)},{}).
#pos({ok(8)},{}).
#pos({ok(9)},{}).


#neg({ok(1)},{}). 
#neg({ok(2)},{}).
#neg({ok(10)},{}).

% hv(8).
% hv(9).

#modeh(1, hv(const(k)), (positive)).
#constant(k, 0).
#constant(k, 1).
#constant(k, 2).
#constant(k, 3).
#constant(k, 4).
#constant(k, 5).
#constant(k, 6).
#constant(k, 7).
#constant(k, 8).
#constant(k, 9).
#constant(k, 10).


1 ~ ok(V0):- s0(V0).
1 ~ ok(V0):- s1(V0).
1 ~ s0(V0):- s1(V0).
1 ~ s1(V0):- s0(V0).
1 ~ :- s0(V0),s1(V0).
1 ~ ok(V0):- s0(V0),s1(V0).
1 ~ ok(V0):- V1+V1=V0,s0(V1).
1 ~ ok(V0):- V1+V1=V0,s1(V1).
1 ~ s0(V0):- V1+V1=V0,s1(V1).
1 ~ s1(V0):- V1+V1=V0,s0(V1).
1 ~ :- V0+V0=V1,s0(V0),s1(V1).
1 ~ :- V0+V0=V1,s0(V1),s1(V0).
1 ~ ok(V0):- V0+V0=V1,s0(V0),s1(V1).
1 ~ ok(V0):- V0+V0=V1,s0(V1),s1(V0).
1 ~ ok(V0):- V1+V1=V0,s0(V0),s1(V1).
1 ~ ok(V0):- V1+V1=V0,s0(V1),s1(V0).
1 ~ ok(V0):- V1+V1=V0,s0(V1),s1(V1).
1 ~ ok(V0):- V1+V2=V0,s0(V1),s1(V2).
1 ~ ok(V0):- V1+V2=V0,s0(V2),s1(V1).
1 ~ ok(V0):- V0#sum{V1,V2:el(V1,V2)}V0,hv(V0).
1 ~ ok(V0):- V0#sum{V1,V2:el(V2,V1)}V0,hv(V0).
1 ~ s0(V0):- V0#sum{V1,V2:el(V1,V2)}V0,hv(V0).
1 ~ s0(V0):- V0#sum{V1,V2:el(V2,V1)}V0,hv(V0).
1 ~ s1(V0):- V0#sum{V1,V2:el(V1,V2)}V0,hv(V0).
1 ~ s1(V0):- V0#sum{V1,V2:el(V2,V1)}V0,hv(V0).
1 ~ :- V2#sum{V0,V1:el(V0,V1)}V2,s0(V2),hv(V2).
1 ~ :- V2#sum{V0,V1:el(V1,V0)}V2,s0(V2),hv(V2).
1 ~ :- V2#sum{V0,V1:el(V0,V1)}V2,s1(V2),hv(V2).
1 ~ :- V2#sum{V0,V1:el(V1,V0)}V2,s1(V2),hv(V2).
1 ~ ok(V0):- V0#sum{V1,V2:el(V1,V2)}V0,s0(V0),hv(V0).
1 ~ ok(V0):- V0#sum{V1,V2:el(V2,V1)}V0,s0(V0),hv(V0).
1 ~ ok(V0):- V0#sum{V1,V2:el(V1,V2)}V0,s1(V0),hv(V0).
1 ~ ok(V0):- V0#sum{V1,V2:el(V2,V1)}V0,s1(V0),hv(V0).
1 ~ s0(V0):- V0#sum{V1,V2:el(V1,V2)}V0,s1(V0),hv(V0).
1 ~ s0(V0):- V0#sum{V1,V2:el(V2,V1)}V0,s1(V0),hv(V0).
1 ~ s1(V0):- V0#sum{V1,V2:el(V1,V2)}V0,s0(V0),hv(V0).
1 ~ s1(V0):- V0#sum{V1,V2:el(V2,V1)}V0,s0(V0),hv(V0).
1 ~ :- V2#sum{V0,V1:el(V0,V1)}V2,s0(V2),s1(V2),hv(V2).
1 ~ :- V2#sum{V0,V1:el(V1,V0)}V2,s0(V2),s1(V2),hv(V2).
1 ~ ok(V0):- V0#sum{V1,V2:el(V1,V2)}V0,s0(V0),s1(V0),hv(V0).
1 ~ ok(V0):- V0#sum{V1,V2:el(V2,V1)}V0,s0(V0),s1(V0),hv(V0).
2 ~ :- V2#sum{V0,V1:el(V0,V1)}V2,V2#sum{V0,V1:el(V1,V0)}V2,hv(V2).
2 ~ :- V2#sum{V0,V1:el(V0,V1)}V2,V2#sum{V1,V0:el(V0,V1)}V2,hv(V2).
2 ~ :- V2#sum{V0,V1:el(V0,V1)}V2,V2#sum{V1,V0:el(V1,V0)}V2,hv(V2).
2 ~ :- V2#sum{V0,V1:el(V1,V0)}V2,V2#sum{V0,V1:el(V0,V1)}V2,hv(V2).
2 ~ :- V2#sum{V0,V1:el(V1,V0)}V2,V2#sum{V1,V0:el(V0,V1)}V2,hv(V2).
2 ~ :- V2#sum{V0,V1:el(V1,V0)}V2,V2#sum{V1,V0:el(V1,V0)}V2,hv(V2).
2 ~ ok(V0):- V0#sum{V1,V2:el(V1,V2)}V0,V0#sum{V1,V2:el(V2,V1)}V0,hv(V0).
2 ~ ok(V0):- V0#sum{V1,V2:el(V1,V2)}V0,V0#sum{V2,V1:el(V1,V2)}V0,hv(V0).
2 ~ ok(V0):- V0#sum{V1,V2:el(V1,V2)}V0,V0#sum{V2,V1:el(V2,V1)}V0,hv(V0).
2 ~ ok(V0):- V0#sum{V1,V2:el(V2,V1)}V0,V0#sum{V1,V2:el(V1,V2)}V0,hv(V0).
2 ~ ok(V0):- V0#sum{V1,V2:el(V2,V1)}V0,V0#sum{V2,V1:el(V1,V2)}V0,hv(V0).
2 ~ ok(V0):- V0#sum{V1,V2:el(V2,V1)}V0,V0#sum{V2,V1:el(V2,V1)}V0,hv(V0).
2 ~ s0(V0):- V0#sum{V1,V2:el(V1,V2)}V0,V0#sum{V1,V2:el(V2,V1)}V0,hv(V0).
2 ~ s0(V0):- V0#sum{V1,V2:el(V1,V2)}V0,V0#sum{V2,V1:el(V1,V2)}V0,hv(V0).
2 ~ s0(V0):- V0#sum{V1,V2:el(V1,V2)}V0,V0#sum{V2,V1:el(V2,V1)}V0,hv(V0).
2 ~ s0(V0):- V0#sum{V1,V2:el(V2,V1)}V0,V0#sum{V1,V2:el(V1,V2)}V0,hv(V0).
2 ~ s0(V0):- V0#sum{V1,V2:el(V2,V1)}V0,V0#sum{V2,V1:el(V1,V2)}V0,hv(V0).
2 ~ s0(V0):- V0#sum{V1,V2:el(V2,V1)}V0,V0#sum{V2,V1:el(V2,V1)}V0,hv(V0).
2 ~ s1(V0):- V0#sum{V1,V2:el(V1,V2)}V0,V0#sum{V1,V2:el(V2,V1)}V0,hv(V0).
2 ~ s1(V0):- V0#sum{V1,V2:el(V1,V2)}V0,V0#sum{V2,V1:el(V1,V2)}V0,hv(V0).
2 ~ s1(V0):- V0#sum{V1,V2:el(V1,V2)}V0,V0#sum{V2,V1:el(V2,V1)}V0,hv(V0).
2 ~ s1(V0):- V0#sum{V1,V2:el(V2,V1)}V0,V0#sum{V1,V2:el(V1,V2)}V0,hv(V0).
2 ~ s1(V0):- V0#sum{V1,V2:el(V2,V1)}V0,V0#sum{V2,V1:el(V1,V2)}V0,hv(V0).
2 ~ s1(V0):- V0#sum{V1,V2:el(V2,V1)}V0,V0#sum{V2,V1:el(V2,V1)}V0,hv(V0).
2 ~ :- V2#sum{V0,V1:el(V0,V1)}V2,V2#sum{V0,V1:el(V1,V0)}V2,s0(V2),hv(V2).
2 ~ :- V2#sum{V0,V1:el(V0,V1)}V2,V2#sum{V1,V0:el(V0,V1)}V2,s0(V2),hv(V2).
2 ~ :- V2#sum{V0,V1:el(V0,V1)}V2,V2#sum{V1,V0:el(V1,V0)}V2,s0(V2),hv(V2).
2 ~ :- V2#sum{V0,V1:el(V1,V0)}V2,V2#sum{V0,V1:el(V0,V1)}V2,s0(V2),hv(V2).
2 ~ :- V2#sum{V0,V1:el(V1,V0)}V2,V2#sum{V1,V0:el(V0,V1)}V2,s0(V2),hv(V2).
2 ~ :- V2#sum{V0,V1:el(V1,V0)}V2,V2#sum{V1,V0:el(V1,V0)}V2,s0(V2),hv(V2).
2 ~ :- V2#sum{V0,V1:el(V0,V1)}V2,V2#sum{V0,V1:el(V1,V0)}V2,s1(V2),hv(V2).
2 ~ :- V2#sum{V0,V1:el(V0,V1)}V2,V2#sum{V1,V0:el(V0,V1)}V2,s1(V2),hv(V2).
2 ~ :- V2#sum{V0,V1:el(V0,V1)}V2,V2#sum{V1,V0:el(V1,V0)}V2,s1(V2),hv(V2).
2 ~ :- V2#sum{V0,V1:el(V1,V0)}V2,V2#sum{V0,V1:el(V0,V1)}V2,s1(V2),hv(V2).
2 ~ :- V2#sum{V0,V1:el(V1,V0)}V2,V2#sum{V1,V0:el(V0,V1)}V2,s1(V2),hv(V2).
2 ~ :- V2#sum{V0,V1:el(V1,V0)}V2,V2#sum{V1,V0:el(V1,V0)}V2,s1(V2),hv(V2).
2 ~ ok(V0):- V0#sum{V1,V2:el(V1,V2)}V0,V0#sum{V1,V2:el(V2,V1)}V0,s0(V0),hv(V0).
2 ~ ok(V0):- V0#sum{V1,V2:el(V1,V2)}V0,V0#sum{V2,V1:el(V1,V2)}V0,s0(V0),hv(V0).
2 ~ ok(V0):- V0#sum{V1,V2:el(V1,V2)}V0,V0#sum{V2,V1:el(V2,V1)}V0,s0(V0),hv(V0).
2 ~ ok(V0):- V0#sum{V1,V2:el(V2,V1)}V0,V0#sum{V1,V2:el(V1,V2)}V0,s0(V0),hv(V0).
2 ~ ok(V0):- V0#sum{V1,V2:el(V2,V1)}V0,V0#sum{V2,V1:el(V1,V2)}V0,s0(V0),hv(V0).
2 ~ ok(V0):- V0#sum{V1,V2:el(V2,V1)}V0,V0#sum{V2,V1:el(V2,V1)}V0,s0(V0),hv(V0).
2 ~ ok(V0):- V0#sum{V1,V2:el(V1,V2)}V0,V0#sum{V1,V2:el(V2,V1)}V0,s1(V0),hv(V0).
2 ~ ok(V0):- V0#sum{V1,V2:el(V1,V2)}V0,V0#sum{V2,V1:el(V1,V2)}V0,s1(V0),hv(V0).
2 ~ ok(V0):- V0#sum{V1,V2:el(V1,V2)}V0,V0#sum{V2,V1:el(V2,V1)}V0,s1(V0),hv(V0).
2 ~ ok(V0):- V0#sum{V1,V2:el(V2,V1)}V0,V0#sum{V1,V2:el(V1,V2)}V0,s1(V0),hv(V0).
2 ~ ok(V0):- V0#sum{V1,V2:el(V2,V1)}V0,V0#sum{V2,V1:el(V1,V2)}V0,s1(V0),hv(V0).
2 ~ ok(V0):- V0#sum{V1,V2:el(V2,V1)}V0,V0#sum{V2,V1:el(V2,V1)}V0,s1(V0),hv(V0).
2 ~ s0(V0):- V0#sum{V1,V2:el(V1,V2)}V0,V0#sum{V1,V2:el(V2,V1)}V0,s1(V0),hv(V0).
2 ~ s0(V0):- V0#sum{V1,V2:el(V1,V2)}V0,V0#sum{V2,V1:el(V1,V2)}V0,s1(V0),hv(V0).
2 ~ s0(V0):- V0#sum{V1,V2:el(V1,V2)}V0,V0#sum{V2,V1:el(V2,V1)}V0,s1(V0),hv(V0).
2 ~ s0(V0):- V0#sum{V1,V2:el(V2,V1)}V0,V0#sum{V1,V2:el(V1,V2)}V0,s1(V0),hv(V0).
2 ~ s0(V0):- V0#sum{V1,V2:el(V2,V1)}V0,V0#sum{V2,V1:el(V1,V2)}V0,s1(V0),hv(V0).
2 ~ s0(V0):- V0#sum{V1,V2:el(V2,V1)}V0,V0#sum{V2,V1:el(V2,V1)}V0,s1(V0),hv(V0).
2 ~ s1(V0):- V0#sum{V1,V2:el(V1,V2)}V0,V0#sum{V1,V2:el(V2,V1)}V0,s0(V0),hv(V0).
2 ~ s1(V0):- V0#sum{V1,V2:el(V1,V2)}V0,V0#sum{V2,V1:el(V1,V2)}V0,s0(V0),hv(V0).
2 ~ s1(V0):- V0#sum{V1,V2:el(V1,V2)}V0,V0#sum{V2,V1:el(V2,V1)}V0,s0(V0),hv(V0).
2 ~ s1(V0):- V0#sum{V1,V2:el(V2,V1)}V0,V0#sum{V1,V2:el(V1,V2)}V0,s0(V0),hv(V0).
2 ~ s1(V0):- V0#sum{V1,V2:el(V2,V1)}V0,V0#sum{V2,V1:el(V1,V2)}V0,s0(V0),hv(V0).
2 ~ s1(V0):- V0#sum{V1,V2:el(V2,V1)}V0,V0#sum{V2,V1:el(V2,V1)}V0,s0(V0),hv(V0).
2 ~ :- V2#sum{V0,V1:el(V0,V1)}V2,V2#sum{V0,V1:el(V1,V0)}V2,s0(V2),s1(V2),hv(V2).
2 ~ :- V2#sum{V0,V1:el(V0,V1)}V2,V2#sum{V1,V0:el(V0,V1)}V2,s0(V2),s1(V2),hv(V2).
2 ~ :- V2#sum{V0,V1:el(V0,V1)}V2,V2#sum{V1,V0:el(V1,V0)}V2,s0(V2),s1(V2),hv(V2).
2 ~ :- V2#sum{V0,V1:el(V1,V0)}V2,V2#sum{V0,V1:el(V0,V1)}V2,s0(V2),s1(V2),hv(V2).
2 ~ :- V2#sum{V0,V1:el(V1,V0)}V2,V2#sum{V1,V0:el(V0,V1)}V2,s0(V2),s1(V2),hv(V2).
2 ~ :- V2#sum{V0,V1:el(V1,V0)}V2,V2#sum{V1,V0:el(V1,V0)}V2,s0(V2),s1(V2),hv(V2).
