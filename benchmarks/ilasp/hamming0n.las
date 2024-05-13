pos(0).
pos(1).
pos(2).
num(0).
num(1).
hd(0).
1{v0(Val,Pos) : num(Val)}1 :- pos(Pos).
1{v1(Val,Pos) : num(Val)}1 :- pos(Pos).

d(Pos,X):- v0(V0,Pos), v1(V1,Pos), X = |V0 - V1|.

#pos({v0(1,0), v1(1,0), v1(0,1), v0(0,1), v0(1,2), v1(1,2)},{}).
#pos({v0(1,0), v1(1,0), v1(0,1), v0(0,1), v1(0,2), v0(0,2)},{}).
#pos({v0(1,0), v1(1,0), v0(1,1), v1(1,1), v0(1,2), v1(1,2)},{}).
#pos({v0(1,0), v1(1,0), v0(1,1), v1(1,1), v1(0,2), v0(0,2)},{}).
#pos({v1(0,0), v0(0,0), v1(0,1), v0(0,1), v0(1,2), v1(1,2)},{}).
#pos({v1(0,0), v0(0,0), v0(1,1), v1(1,1), v0(1,2), v1(1,2)},{}).
#pos({v1(0,0), v0(0,0), v1(0,1), v0(0,1), v1(0,2), v0(0,2)},{}).
#pos({v1(0,0), v0(0,0), v0(1,1), v1(1,1), v1(0,2), v0(0,2)},{}).


#neg({v0(1,0), v0(1,1), v0(1,2), v1(0,1), v1(1,0), v1(1,2)},{}).
#neg({v0(0,2), v0(1,0), v0(1,1), v1(0,1), v1(1,0), v1(1,2)},{}).
#neg({v0(0,1), v0(0,2), v0(1,0), v1(0,1), v1(1,0), v1(1,2)},{}).
#neg({v0(1,0), v0(1,1), v0(1,2), v1(0,1), v1(0,2), v1(1,0)},{}).
#neg({v0(0,2), v0(1,0), v0(1,1), v1(0,1), v1(0,2), v1(1,0)},{}).
#neg({v0(0,1), v0(1,0), v0(1,2), v1(0,1), v1(0,2), v1(1,0)},{}).
#neg({v0(1,0), v0(1,1), v0(1,2), v1(0,2), v1(1,0), v1(1,1)},{}).
#neg({v0(0,1), v0(1,0), v0(1,2), v1(0,2), v1(1,0), v1(1,1)},{}).
#neg({v0(0,1), v0(1,0), v0(1,2), v1(1,0), v1(1,1), v1(1,2)},{}).
#neg({v0(0,2), v0(1,0), v0(1,1), v1(1,0), v1(1,1), v1(1,2)},{}).
#neg({v0(0,1), v0(0,2), v0(1,0), v1(0,2), v1(1,0), v1(1,1)},{}).
#neg({v0(0,1), v0(0,2), v0(1,0), v1(1,0), v1(1,1), v1(1,2)},{}).
#neg({v0(0,0), v0(1,1), v0(1,2), v1(0,2), v1(1,0), v1(1,1)},{}).
#neg({v0(0,0), v0(0,1), v0(1,2), v1(0,2), v1(1,0), v1(1,1)},{}).
#neg({v0(0,0), v0(0,2), v0(1,1), v1(0,2), v1(1,0), v1(1,1)},{}).
#neg({v0(0,0), v0(0,1), v0(0,2), v1(0,2), v1(1,0), v1(1,1)},{}).
#neg({v0(0,0), v0(1,1), v0(1,2), v1(0,1), v1(0,2), v1(1,0)},{}).
#neg({v0(0,0), v0(0,2), v0(1,1), v1(0,1), v1(0,2), v1(1,0)},{}).
#neg({v0(0,0), v0(0,1), v0(1,2), v1(0,1), v1(0,2), v1(1,0)},{}).
#neg({v0(0,0), v0(0,1), v0(0,2), v1(0,1), v1(0,2), v1(1,0)},{}).
#neg({v0(0,0), v0(1,1), v0(1,2), v1(1,0), v1(1,1), v1(1,2)},{}).
#neg({v0(0,0), v0(0,1), v0(1,2), v1(1,0), v1(1,1), v1(1,2)},{}).
#neg({v0(0,0), v0(1,1), v0(1,2), v1(0,1), v1(1,0), v1(1,2)},{}).
#neg({v0(0,0), v0(0,1), v0(1,2), v1(0,1), v1(1,0), v1(1,2)},{}).
#neg({v0(0,0), v0(0,2), v0(1,1), v1(1,0), v1(1,1), v1(1,2)},{}).
#neg({v0(0,0), v0(0,2), v0(1,1), v1(0,1), v1(1,0), v1(1,2)},{}).
#neg({v0(0,0), v0(0,1), v0(0,2), v1(1,0), v1(1,1), v1(1,2)},{}).
#neg({v0(0,0), v0(0,1), v0(0,2), v1(0,1), v1(1,0), v1(1,2)},{}).
#neg({v0(1,0), v0(1,1), v0(1,2), v1(0,0), v1(0,2), v1(1,1)},{}).
#neg({v0(0,2), v0(1,0), v0(1,1), v1(0,0), v1(0,2), v1(1,1)},{}).
#neg({v0(1,0), v0(1,1), v0(1,2), v1(0,0), v1(1,1), v1(1,2)},{}).
#neg({v0(0,2), v0(1,0), v0(1,1), v1(0,0), v1(1,1), v1(1,2)},{}).
#neg({v0(0,1), v0(1,0), v0(1,2), v1(0,0), v1(0,2), v1(1,1)},{}).
#neg({v0(0,1), v0(1,0), v0(1,2), v1(0,0), v1(1,1), v1(1,2)},{}).
#neg({v0(0,1), v0(0,2), v0(1,0), v1(0,0), v1(0,2), v1(1,1)},{}).
#neg({v0(0,1), v0(0,2), v0(1,0), v1(0,0), v1(1,1), v1(1,2)},{}).
#neg({v0(0,0), v0(1,1), v0(1,2), v1(0,0), v1(0,2), v1(1,1)},{}).
#neg({v0(0,0), v0(0,1), v0(1,2), v1(0,0), v1(0,2), v1(1,1)},{}).
#neg({v0(0,0), v0(0,1), v0(0,2), v1(0,0), v1(0,2), v1(1,1)},{}).
#neg({v0(0,0), v0(0,2), v0(1,1), v1(0,0), v1(1,1), v1(1,2)},{}).
#neg({v0(0,0), v0(0,1), v0(1,2), v1(0,0), v1(1,1), v1(1,2)},{}).
#neg({v0(0,0), v0(0,1), v0(0,2), v1(0,0), v1(1,1), v1(1,2)},{}).
#neg({v0(1,0), v0(1,1), v0(1,2), v1(0,0), v1(0,1), v1(0,2)},{}).
#neg({v0(0,0), v0(1,1), v0(1,2), v1(0,0), v1(0,1), v1(0,2)},{}).
#neg({v0(0,1), v0(1,0), v0(1,2), v1(0,0), v1(0,1), v1(0,2)},{}).
#neg({v0(0,0), v0(0,1), v0(1,2), v1(0,0), v1(0,1), v1(0,2)},{}).
#neg({v0(1,0), v0(1,1), v0(1,2), v1(0,0), v1(0,1), v1(1,2)},{}).
#neg({v0(0,1), v0(1,0), v0(1,2), v1(0,0), v1(0,1), v1(1,2)},{}).
#neg({v0(0,0), v0(1,1), v0(1,2), v1(0,0), v1(0,1), v1(1,2)},{}).
#neg({v0(0,2), v0(1,0), v0(1,1), v1(0,0), v1(0,1), v1(0,2)},{}).
#neg({v0(0,0), v0(0,2), v0(1,1), v1(0,0), v1(0,1), v1(0,2)},{}).
#neg({v0(0,2), v0(1,0), v0(1,1), v1(0,0), v1(0,1), v1(1,2)},{}).
#neg({v0(0,0), v0(0,2), v0(1,1), v1(0,0), v1(0,1), v1(1,2)},{}).
#neg({v0(0,1), v0(0,2), v0(1,0), v1(0,0), v1(0,1), v1(0,2)},{}).
#neg({v0(0,1), v0(0,2), v0(1,0), v1(0,0), v1(0,1), v1(1,2)},{}).
#neg({v0(0,0), v0(0,1), v0(0,2), v1(0,0), v1(0,1), v1(1,2)},{}).

% #modeb(1, hd(var(t))).
% hv(1).
#modeh(1, hv(const(k)), (positive)).
#constant(k, 0).
#constant(k, 1).
#constant(k, 2).

1 ~ :- V1#sum{V0:d(V0,V0)}V1,hd(V1),hv(V1).
1 ~ :- V1#sum{V0:d(V0,V1)}V1,hd(V1),hv(V1).
1 ~ :- V1#sum{V0:d(V1,V0)}V1,hd(V1),hv(V1).
1 ~ :- V1#count{V0:d(V0,V0)}V1,hd(V1),hv(V1).
1 ~ :- V1#count{V0:d(V0,V1)}V1,hd(V1),hv(V1).
1 ~ :- V1#count{V0:d(V1,V0)}V1,hd(V1),hv(V1).
1 ~ :- V2#sum{V0,V1:d(V0,V1)}V2,hd(V2),hv(V2).
1 ~ :- V2#sum{V0,V1:d(V1,V0)}V2,hd(V2),hv(V2).
1 ~ :- V2#count{V0,V1:d(V0,V1)}V2,hd(V2),hv(V2).
1 ~ :- V2#count{V0,V1:d(V1,V0)}V2,hd(V2),hv(V2).
1 ~ :- V1#sum{V0:d(V0,V0)}V1,V1!=V2,hd(V2),hv(V1).
1 ~ :- V1#sum{V0:d(V0,V0)}V1,V2!=V1,hd(V2),hv(V1).
1 ~ :- V2#sum{V0:d(V0,V1)}V2,V1!=V2,hd(V1),hv(V2).
1 ~ :- V2#sum{V0:d(V0,V1)}V2,V2!=V1,hd(V1),hv(V2).
1 ~ :- V2#sum{V0:d(V1,V0)}V2,V1!=V2,hd(V1),hv(V2).
1 ~ :- V2#sum{V0:d(V1,V0)}V2,V2!=V1,hd(V1),hv(V2).
1 ~ :- V1#count{V0:d(V0,V0)}V1,V1!=V2,hd(V2),hv(V1).
1 ~ :- V1#count{V0:d(V0,V0)}V1,V2!=V1,hd(V2),hv(V1).
1 ~ :- V2#count{V0:d(V0,V1)}V2,V1!=V2,hd(V1),hv(V2).
1 ~ :- V2#count{V0:d(V0,V1)}V2,V2!=V1,hd(V1),hv(V2).
1 ~ :- V2#count{V0:d(V1,V0)}V2,V1!=V2,hd(V1),hv(V2).
1 ~ :- V2#count{V0:d(V1,V0)}V2,V2!=V1,hd(V1),hv(V2).
1 ~ :- V2#sum{V0,V1:d(V0,V1)}V2,V2!=V3,hd(V3),hv(V2).
1 ~ :- V2#sum{V0,V1:d(V0,V1)}V2,V3!=V2,hd(V3),hv(V2).
1 ~ :- V2#sum{V0,V1:d(V1,V0)}V2,V2!=V3,hd(V3),hv(V2).
1 ~ :- V2#sum{V0,V1:d(V1,V0)}V2,V3!=V2,hd(V3),hv(V2).
1 ~ :- V2#count{V0,V1:d(V0,V1)}V2,V2!=V3,hd(V3),hv(V2).
1 ~ :- V2#count{V0,V1:d(V0,V1)}V2,V3!=V2,hd(V3),hv(V2).
1 ~ :- V2#count{V0,V1:d(V1,V0)}V2,V2!=V3,hd(V3),hv(V2).
1 ~ :- V2#count{V0,V1:d(V1,V0)}V2,V3!=V2,hd(V3),hv(V2).
2 ~ :- V1#count{V0:d(V0,V0)}V1,V1#sum{V0:d(V0,V0)}V1,hv(V1).
2 ~ :- V1#count{V0:d(V0,V0)}V1,V1#sum{V0:d(V0,V1)}V1,hv(V1).
2 ~ :- V1#count{V0:d(V0,V0)}V1,V1#sum{V0:d(V1,V0)}V1,hv(V1).
2 ~ :- V1#count{V0:d(V0,V0)}V1,V1#sum{V2:d(V0,V2)}V1,hv(V1).
2 ~ :- V1#count{V0:d(V0,V0)}V1,V1#sum{V2:d(V1,V2)}V1,hv(V1).
2 ~ :- V1#count{V0:d(V0,V0)}V1,V1#sum{V2:d(V2,V0)}V1,hv(V1).
2 ~ :- V1#count{V0:d(V0,V0)}V1,V1#sum{V2:d(V2,V1)}V1,hv(V1).
2 ~ :- V1#count{V0:d(V0,V0)}V1,V1#sum{V2:d(V2,V2)}V1,hv(V1).
2 ~ :- V1#count{V0:d(V0,V1)}V1,V1#sum{V0:d(V0,V0)}V1,hv(V1).
2 ~ :- V1#count{V0:d(V0,V1)}V1,V1#sum{V2:d(V0,V2)}V1,hv(V1).
2 ~ :- V1#count{V0:d(V0,V1)}V1,V1#sum{V2:d(V2,V0)}V1,hv(V1).
2 ~ :- V1#count{V0:d(V0,V1)}V1,V1#sum{V2:d(V2,V2)}V1,hv(V1).
2 ~ :- V2#count{V0:d(V0,V1)}V2,V2#sum{V0:d(V0,V1)}V2,hv(V2).
2 ~ :- V2#count{V0:d(V0,V1)}V2,V2#sum{V0:d(V1,V0)}V2,hv(V2).
2 ~ :- V2#count{V0:d(V0,V1)}V2,V2#sum{V1:d(V0,V1)}V2,hv(V2).
2 ~ :- V2#count{V0:d(V0,V1)}V2,V2#sum{V1:d(V1,V0)}V2,hv(V2).
2 ~ :- V2#count{V0:d(V0,V1)}V2,V2#sum{V1:d(V1,V1)}V2,hv(V2).
2 ~ :- V2#count{V0:d(V0,V1)}V2,V2#sum{V1:d(V1,V2)}V2,hv(V2).
2 ~ :- V2#count{V0:d(V0,V1)}V2,V2#sum{V1:d(V2,V1)}V2,hv(V2).
2 ~ :- V2#count{V0:d(V0,V1)}V2,V2#sum{V3:d(V1,V3)}V2,hv(V2).
2 ~ :- V2#count{V0:d(V0,V1)}V2,V2#sum{V3:d(V3,V1)}V2,hv(V2).
2 ~ :- V1#count{V0:d(V1,V0)}V1,V1#sum{V0:d(V0,V0)}V1,hv(V1).
2 ~ :- V1#count{V0:d(V1,V0)}V1,V1#sum{V2:d(V0,V2)}V1,hv(V1).
2 ~ :- V1#count{V0:d(V1,V0)}V1,V1#sum{V2:d(V2,V0)}V1,hv(V1).
2 ~ :- V1#count{V0:d(V1,V0)}V1,V1#sum{V2:d(V2,V2)}V1,hv(V1).
2 ~ :- V2#count{V0:d(V1,V0)}V2,V2#sum{V0:d(V0,V1)}V2,hv(V2).
2 ~ :- V2#count{V0:d(V1,V0)}V2,V2#sum{V0:d(V1,V0)}V2,hv(V2).
2 ~ :- V2#count{V0:d(V1,V0)}V2,V2#sum{V1:d(V0,V1)}V2,hv(V2).
2 ~ :- V2#count{V0:d(V1,V0)}V2,V2#sum{V1:d(V1,V0)}V2,hv(V2).
2 ~ :- V2#count{V0:d(V1,V0)}V2,V2#sum{V1:d(V1,V1)}V2,hv(V2).
2 ~ :- V2#count{V0:d(V1,V0)}V2,V2#sum{V1:d(V1,V2)}V2,hv(V2).
2 ~ :- V2#count{V0:d(V1,V0)}V2,V2#sum{V1:d(V2,V1)}V2,hv(V2).
2 ~ :- V2#count{V0:d(V1,V0)}V2,V2#sum{V3:d(V1,V3)}V2,hv(V2).
2 ~ :- V2#count{V0:d(V1,V0)}V2,V2#sum{V3:d(V3,V1)}V2,hv(V2).
2 ~ :- V2#count{V0,V1:d(V0,V1)}V2,V2#sum{V0:d(V0,V0)}V2,hv(V2).
2 ~ :- V2#count{V0,V1:d(V0,V1)}V2,V2#sum{V0:d(V0,V1)}V2,hv(V2).
2 ~ :- V2#count{V0,V1:d(V0,V1)}V2,V2#sum{V0:d(V0,V2)}V2,hv(V2).
2 ~ :- V2#count{V0,V1:d(V0,V1)}V2,V2#sum{V0:d(V1,V0)}V2,hv(V2).
2 ~ :- V2#count{V0,V1:d(V0,V1)}V2,V2#sum{V0:d(V2,V0)}V2,hv(V2).
2 ~ :- V2#count{V0,V1:d(V0,V1)}V2,V2#sum{V1:d(V0,V1)}V2,hv(V2).
2 ~ :- V2#count{V0,V1:d(V0,V1)}V2,V2#sum{V1:d(V1,V0)}V2,hv(V2).
2 ~ :- V2#count{V0,V1:d(V0,V1)}V2,V2#sum{V1:d(V1,V1)}V2,hv(V2).
2 ~ :- V2#count{V0,V1:d(V0,V1)}V2,V2#sum{V1:d(V1,V2)}V2,hv(V2).
2 ~ :- V2#count{V0,V1:d(V0,V1)}V2,V2#sum{V1:d(V2,V1)}V2,hv(V2).
2 ~ :- V2#count{V0,V1:d(V0,V1)}V2,V2#sum{V3:d(V0,V3)}V2,hv(V2).
2 ~ :- V2#count{V0,V1:d(V0,V1)}V2,V2#sum{V3:d(V1,V3)}V2,hv(V2).
2 ~ :- V2#count{V0,V1:d(V0,V1)}V2,V2#sum{V3:d(V2,V3)}V2,hv(V2).
2 ~ :- V2#count{V0,V1:d(V0,V1)}V2,V2#sum{V3:d(V3,V0)}V2,hv(V2).
2 ~ :- V2#count{V0,V1:d(V0,V1)}V2,V2#sum{V3:d(V3,V1)}V2,hv(V2).
2 ~ :- V2#count{V0,V1:d(V0,V1)}V2,V2#sum{V3:d(V3,V2)}V2,hv(V2).
2 ~ :- V2#count{V0,V1:d(V0,V1)}V2,V2#sum{V3:d(V3,V3)}V2,hv(V2).
2 ~ :- V2#count{V0,V1:d(V1,V0)}V2,V2#sum{V0:d(V0,V0)}V2,hv(V2).
2 ~ :- V2#count{V0,V1:d(V1,V0)}V2,V2#sum{V0:d(V0,V1)}V2,hv(V2).
2 ~ :- V2#count{V0,V1:d(V1,V0)}V2,V2#sum{V0:d(V0,V2)}V2,hv(V2).
2 ~ :- V2#count{V0,V1:d(V1,V0)}V2,V2#sum{V0:d(V1,V0)}V2,hv(V2).
2 ~ :- V2#count{V0,V1:d(V1,V0)}V2,V2#sum{V0:d(V2,V0)}V2,hv(V2).
2 ~ :- V2#count{V0,V1:d(V1,V0)}V2,V2#sum{V1:d(V0,V1)}V2,hv(V2).
2 ~ :- V2#count{V0,V1:d(V1,V0)}V2,V2#sum{V1:d(V1,V0)}V2,hv(V2).
2 ~ :- V2#count{V0,V1:d(V1,V0)}V2,V2#sum{V1:d(V1,V1)}V2,hv(V2).
2 ~ :- V2#count{V0,V1:d(V1,V0)}V2,V2#sum{V1:d(V1,V2)}V2,hv(V2).
2 ~ :- V2#count{V0,V1:d(V1,V0)}V2,V2#sum{V1:d(V2,V1)}V2,hv(V2).
2 ~ :- V2#count{V0,V1:d(V1,V0)}V2,V2#sum{V3:d(V0,V3)}V2,hv(V2).
2 ~ :- V2#count{V0,V1:d(V1,V0)}V2,V2#sum{V3:d(V1,V3)}V2,hv(V2).
2 ~ :- V2#count{V0,V1:d(V1,V0)}V2,V2#sum{V3:d(V2,V3)}V2,hv(V2).
2 ~ :- V2#count{V0,V1:d(V1,V0)}V2,V2#sum{V3:d(V3,V0)}V2,hv(V2).
2 ~ :- V2#count{V0,V1:d(V1,V0)}V2,V2#sum{V3:d(V3,V1)}V2,hv(V2).
2 ~ :- V2#count{V0,V1:d(V1,V0)}V2,V2#sum{V3:d(V3,V2)}V2,hv(V2).
2 ~ :- V2#count{V0,V1:d(V1,V0)}V2,V2#sum{V3:d(V3,V3)}V2,hv(V2).
2 ~ :- V1#count{V0:d(V0,V0)}V1,V1#sum{V0,V2:d(V0,V2)}V1,hv(V1).
2 ~ :- V1#count{V0:d(V0,V0)}V1,V1#sum{V0,V2:d(V2,V0)}V1,hv(V1).
2 ~ :- V1#count{V0:d(V0,V0)}V1,V1#sum{V2,V0:d(V0,V2)}V1,hv(V1).
2 ~ :- V1#count{V0:d(V0,V0)}V1,V1#sum{V2,V0:d(V2,V0)}V1,hv(V1).
2 ~ :- V1#count{V0:d(V0,V0)}V1,V1#sum{V2,V3:d(V2,V3)}V1,hv(V1).
2 ~ :- V1#count{V0:d(V0,V0)}V1,V1#sum{V2,V3:d(V3,V2)}V1,hv(V1).
2 ~ :- V1#count{V0:d(V0,V1)}V1,V1#sum{V0,V2:d(V0,V2)}V1,hv(V1).
2 ~ :- V1#count{V0:d(V0,V1)}V1,V1#sum{V0,V2:d(V2,V0)}V1,hv(V1).
2 ~ :- V1#count{V0:d(V0,V1)}V1,V1#sum{V2,V0:d(V0,V2)}V1,hv(V1).
2 ~ :- V1#count{V0:d(V0,V1)}V1,V1#sum{V2,V0:d(V2,V0)}V1,hv(V1).
2 ~ :- V1#count{V0:d(V0,V1)}V1,V1#sum{V2,V3:d(V2,V3)}V1,hv(V1).
2 ~ :- V1#count{V0:d(V0,V1)}V1,V1#sum{V2,V3:d(V3,V2)}V1,hv(V1).
2 ~ :- V2#count{V0:d(V0,V1)}V2,V2#sum{V0,V1:d(V0,V1)}V2,hv(V2).
2 ~ :- V2#count{V0:d(V0,V1)}V2,V2#sum{V0,V1:d(V1,V0)}V2,hv(V2).
2 ~ :- V2#count{V0:d(V0,V1)}V2,V2#sum{V1,V0:d(V0,V1)}V2,hv(V2).
2 ~ :- V2#count{V0:d(V0,V1)}V2,V2#sum{V1,V0:d(V1,V0)}V2,hv(V2).
2 ~ :- V2#count{V0:d(V0,V1)}V2,V2#sum{V1,V3:d(V1,V3)}V2,hv(V2).
2 ~ :- V2#count{V0:d(V0,V1)}V2,V2#sum{V1,V3:d(V3,V1)}V2,hv(V2).
2 ~ :- V2#count{V0:d(V0,V1)}V2,V2#sum{V3,V1:d(V1,V3)}V2,hv(V2).
2 ~ :- V2#count{V0:d(V0,V1)}V2,V2#sum{V3,V1:d(V3,V1)}V2,hv(V2).
2 ~ :- V1#count{V0:d(V1,V0)}V1,V1#sum{V0,V2:d(V0,V2)}V1,hv(V1).
2 ~ :- V1#count{V0:d(V1,V0)}V1,V1#sum{V0,V2:d(V2,V0)}V1,hv(V1).
2 ~ :- V1#count{V0:d(V1,V0)}V1,V1#sum{V2,V0:d(V0,V2)}V1,hv(V1).
2 ~ :- V1#count{V0:d(V1,V0)}V1,V1#sum{V2,V0:d(V2,V0)}V1,hv(V1).
2 ~ :- V1#count{V0:d(V1,V0)}V1,V1#sum{V2,V3:d(V2,V3)}V1,hv(V1).
2 ~ :- V1#count{V0:d(V1,V0)}V1,V1#sum{V2,V3:d(V3,V2)}V1,hv(V1).
2 ~ :- V2#count{V0:d(V1,V0)}V2,V2#sum{V0,V1:d(V0,V1)}V2,hv(V2).
2 ~ :- V2#count{V0:d(V1,V0)}V2,V2#sum{V0,V1:d(V1,V0)}V2,hv(V2).
2 ~ :- V2#count{V0:d(V1,V0)}V2,V2#sum{V1,V0:d(V0,V1)}V2,hv(V2).
2 ~ :- V2#count{V0:d(V1,V0)}V2,V2#sum{V1,V0:d(V1,V0)}V2,hv(V2).
2 ~ :- V2#count{V0:d(V1,V0)}V2,V2#sum{V1,V3:d(V1,V3)}V2,hv(V2).
2 ~ :- V2#count{V0:d(V1,V0)}V2,V2#sum{V1,V3:d(V3,V1)}V2,hv(V2).
2 ~ :- V2#count{V0:d(V1,V0)}V2,V2#sum{V3,V1:d(V1,V3)}V2,hv(V2).
2 ~ :- V2#count{V0:d(V1,V0)}V2,V2#sum{V3,V1:d(V3,V1)}V2,hv(V2).
2 ~ :- V1#count{V0:d(V0,V0)}V1,V1#sum{V0:d(V0,V0)}V1,hd(V1),hv(V1).
2 ~ :- V1#count{V0:d(V0,V0)}V1,V1#sum{V0:d(V0,V1)}V1,hd(V1),hv(V1).
2 ~ :- V1#count{V0:d(V0,V0)}V1,V2#sum{V0:d(V0,V1)}V2,hd(V2),hv(V2),hv(V1).
2 ~ :- V1#count{V0:d(V0,V0)}V1,V1#sum{V0:d(V0,V2)}V1,hd(V2),hv(V1).
2 ~ :- V1#count{V0:d(V0,V0)}V1,V1#sum{V0:d(V1,V0)}V1,hd(V1),hv(V1).
2 ~ :- V1#count{V0:d(V0,V0)}V1,V2#sum{V0:d(V1,V0)}V2,hd(V2),hv(V2),hv(V1).
2 ~ :- V1#count{V0:d(V0,V0)}V1,V1#sum{V0:d(V2,V0)}V1,hd(V2),hv(V1).
2 ~ :- V1#count{V0:d(V0,V0)}V1,V1#sum{V2:d(V0,V2)}V1,hd(V1),hv(V1).
2 ~ :- V1#count{V0:d(V0,V0)}V1,V1#sum{V2:d(V1,V2)}V1,hd(V1),hv(V1).
2 ~ :- V1#count{V0:d(V0,V0)}V1,V3#sum{V2:d(V1,V2)}V3,hd(V3),hv(V1),hv(V3).
2 ~ :- V1#count{V0:d(V0,V0)}V1,V1#sum{V2:d(V2,V0)}V1,hd(V1),hv(V1).
2 ~ :- V1#count{V0:d(V0,V0)}V1,V1#sum{V2:d(V2,V1)}V1,hd(V1),hv(V1).
2 ~ :- V1#count{V0:d(V0,V0)}V1,V3#sum{V2:d(V2,V1)}V3,hd(V3),hv(V1),hv(V3).
2 ~ :- V1#count{V0:d(V0,V0)}V1,V1#sum{V2:d(V2,V2)}V1,hd(V1),hv(V1).
2 ~ :- V1#count{V0:d(V0,V0)}V1,V1#sum{V2:d(V2,V3)}V1,hd(V3),hv(V1).
2 ~ :- V1#count{V0:d(V0,V0)}V1,V1#sum{V2:d(V3,V2)}V1,hd(V3),hv(V1).
2 ~ :- V1#count{V0:d(V0,V1)}V1,V1#sum{V0:d(V0,V0)}V1,hd(V1),hv(V1).
2 ~ :- V1#count{V0:d(V0,V1)}V1,V1#sum{V0:d(V0,V1)}V1,hd(V1),hv(V1).
2 ~ :- V1#count{V0:d(V0,V1)}V1,V1#sum{V0:d(V0,V2)}V1,hd(V2),hv(V1).
2 ~ :- V1#count{V0:d(V0,V1)}V1,V1#sum{V0:d(V1,V0)}V1,hd(V1),hv(V1).
2 ~ :- V1#count{V0:d(V0,V1)}V1,V1#sum{V0:d(V2,V0)}V1,hd(V2),hv(V1).
2 ~ :- V1#count{V0:d(V0,V1)}V1,V1#sum{V2:d(V0,V2)}V1,hd(V1),hv(V1).
2 ~ :- V1#count{V0:d(V0,V1)}V1,V1#sum{V2:d(V1,V2)}V1,hd(V1),hv(V1).
2 ~ :- V1#count{V0:d(V0,V1)}V1,V1#sum{V2:d(V2,V0)}V1,hd(V1),hv(V1).
2 ~ :- V1#count{V0:d(V0,V1)}V1,V1#sum{V2:d(V2,V1)}V1,hd(V1),hv(V1).
2 ~ :- V1#count{V0:d(V0,V1)}V1,V1#sum{V2:d(V2,V2)}V1,hd(V1),hv(V1).
2 ~ :- V1#count{V0:d(V0,V1)}V1,V1#sum{V2:d(V2,V3)}V1,hd(V3),hv(V1).
2 ~ :- V1#count{V0:d(V0,V1)}V1,V1#sum{V2:d(V3,V2)}V1,hd(V3),hv(V1).
2 ~ :- V2#count{V0:d(V0,V1)}V2,V1#sum{V0:d(V0,V0)}V1,hd(V2),hv(V2),hv(V1).
2 ~ :- V2#count{V0:d(V0,V1)}V2,V2#sum{V0:d(V0,V0)}V2,hd(V1),hv(V2).
2 ~ :- V2#count{V0:d(V0,V1)}V2,V2#sum{V0:d(V0,V1)}V2,hd(V1),hv(V2).
2 ~ :- V2#count{V0:d(V0,V1)}V2,V2#sum{V0:d(V0,V1)}V2,hd(V2),hv(V2).
2 ~ :- V2#count{V0:d(V0,V1)}V2,V1#sum{V0:d(V0,V2)}V1,hd(V1),hv(V2),hv(V1).
2 ~ :- V2#count{V0:d(V0,V1)}V2,V1#sum{V0:d(V0,V2)}V1,hd(V2),hv(V2),hv(V1).
2 ~ :- V2#count{V0:d(V0,V1)}V2,V2#sum{V0:d(V0,V2)}V2,hd(V1),hv(V2).
2 ~ :- V2#count{V0:d(V0,V1)}V2,V2#sum{V0:d(V1,V0)}V2,hd(V1),hv(V2).
2 ~ :- V2#count{V0:d(V0,V1)}V2,V2#sum{V0:d(V1,V0)}V2,hd(V2),hv(V2).
2 ~ :- V2#count{V0:d(V0,V1)}V2,V1#sum{V0:d(V2,V0)}V1,hd(V1),hv(V2),hv(V1).
2 ~ :- V2#count{V0:d(V0,V1)}V2,V1#sum{V0:d(V2,V0)}V1,hd(V2),hv(V2),hv(V1).
2 ~ :- V2#count{V0:d(V0,V1)}V2,V2#sum{V0:d(V2,V0)}V2,hd(V1),hv(V2).
2 ~ :- V2#count{V0:d(V0,V1)}V2,V2#sum{V1:d(V0,V1)}V2,hd(V2),hv(V2).
2 ~ :- V2#count{V0:d(V0,V1)}V2,V2#sum{V1:d(V1,V0)}V2,hd(V2),hv(V2).
2 ~ :- V2#count{V0:d(V0,V1)}V2,V2#sum{V1:d(V1,V1)}V2,hd(V2),hv(V2).
2 ~ :- V2#count{V0:d(V0,V1)}V2,V2#sum{V1:d(V1,V2)}V2,hd(V2),hv(V2).
2 ~ :- V2#count{V0:d(V0,V1)}V2,V3#sum{V1:d(V1,V2)}V3,hd(V3),hv(V2),hv(V3).
2 ~ :- V2#count{V0:d(V0,V1)}V2,V2#sum{V1:d(V1,V3)}V2,hd(V3),hv(V2).
2 ~ :- V2#count{V0:d(V0,V1)}V2,V2#sum{V1:d(V2,V1)}V2,hd(V2),hv(V2).
2 ~ :- V2#count{V0:d(V0,V1)}V2,V3#sum{V1:d(V2,V1)}V3,hd(V3),hv(V2),hv(V3).
2 ~ :- V2#count{V0:d(V0,V1)}V2,V2#sum{V1:d(V3,V1)}V2,hd(V3),hv(V2).
2 ~ :- V2#count{V0:d(V0,V1)}V2,V1#sum{V3:d(V0,V3)}V1,hd(V2),hv(V2),hv(V1).
2 ~ :- V2#count{V0:d(V0,V1)}V2,V2#sum{V3:d(V0,V3)}V2,hd(V1),hv(V2).
2 ~ :- V2#count{V0:d(V0,V1)}V2,V2#sum{V3:d(V1,V3)}V2,hd(V1),hv(V2).
2 ~ :- V2#count{V0:d(V0,V1)}V2,V2#sum{V3:d(V1,V3)}V2,hd(V2),hv(V2).
2 ~ :- V2#count{V0:d(V0,V1)}V2,V1#sum{V3:d(V2,V3)}V1,hd(V1),hv(V2),hv(V1).
2 ~ :- V2#count{V0:d(V0,V1)}V2,V1#sum{V3:d(V2,V3)}V1,hd(V2),hv(V2),hv(V1).
2 ~ :- V2#count{V0:d(V0,V1)}V2,V2#sum{V3:d(V2,V3)}V2,hd(V1),hv(V2).
2 ~ :- V2#count{V0:d(V0,V1)}V2,V1#sum{V3:d(V3,V0)}V1,hd(V2),hv(V2),hv(V1).
2 ~ :- V2#count{V0:d(V0,V1)}V2,V2#sum{V3:d(V3,V0)}V2,hd(V1),hv(V2).
2 ~ :- V2#count{V0:d(V0,V1)}V2,V2#sum{V3:d(V3,V1)}V2,hd(V1),hv(V2).
2 ~ :- V2#count{V0:d(V0,V1)}V2,V2#sum{V3:d(V3,V1)}V2,hd(V2),hv(V2).
2 ~ :- V2#count{V0:d(V0,V1)}V2,V1#sum{V3:d(V3,V2)}V1,hd(V1),hv(V2),hv(V1).
2 ~ :- V2#count{V0:d(V0,V1)}V2,V1#sum{V3:d(V3,V2)}V1,hd(V2),hv(V2),hv(V1).
2 ~ :- V2#count{V0:d(V0,V1)}V2,V2#sum{V3:d(V3,V2)}V2,hd(V1),hv(V2).
2 ~ :- V2#count{V0:d(V0,V1)}V2,V1#sum{V3:d(V3,V3)}V1,hd(V2),hv(V2),hv(V1).
2 ~ :- V2#count{V0:d(V0,V1)}V2,V2#sum{V3:d(V3,V3)}V2,hd(V1),hv(V2).
2 ~ :- V1#count{V0:d(V1,V0)}V1,V1#sum{V0:d(V0,V0)}V1,hd(V1),hv(V1).
2 ~ :- V1#count{V0:d(V1,V0)}V1,V1#sum{V0:d(V0,V1)}V1,hd(V1),hv(V1).
2 ~ :- V1#count{V0:d(V1,V0)}V1,V1#sum{V0:d(V0,V2)}V1,hd(V2),hv(V1).
2 ~ :- V1#count{V0:d(V1,V0)}V1,V1#sum{V0:d(V1,V0)}V1,hd(V1),hv(V1).
2 ~ :- V1#count{V0:d(V1,V0)}V1,V1#sum{V0:d(V2,V0)}V1,hd(V2),hv(V1).
2 ~ :- V1#count{V0:d(V1,V0)}V1,V1#sum{V2:d(V0,V2)}V1,hd(V1),hv(V1).
2 ~ :- V1#count{V0:d(V1,V0)}V1,V1#sum{V2:d(V1,V2)}V1,hd(V1),hv(V1).
2 ~ :- V1#count{V0:d(V1,V0)}V1,V1#sum{V2:d(V2,V0)}V1,hd(V1),hv(V1).
2 ~ :- V1#count{V0:d(V1,V0)}V1,V1#sum{V2:d(V2,V1)}V1,hd(V1),hv(V1).
2 ~ :- V1#count{V0:d(V1,V0)}V1,V1#sum{V2:d(V2,V2)}V1,hd(V1),hv(V1).
2 ~ :- V1#count{V0:d(V1,V0)}V1,V1#sum{V2:d(V2,V3)}V1,hd(V3),hv(V1).
2 ~ :- V1#count{V0:d(V1,V0)}V1,V1#sum{V2:d(V3,V2)}V1,hd(V3),hv(V1).
2 ~ :- V2#count{V0:d(V1,V0)}V2,V1#sum{V0:d(V0,V0)}V1,hd(V2),hv(V2),hv(V1).
2 ~ :- V2#count{V0:d(V1,V0)}V2,V2#sum{V0:d(V0,V0)}V2,hd(V1),hv(V2).
2 ~ :- V2#count{V0:d(V1,V0)}V2,V2#sum{V0:d(V0,V1)}V2,hd(V1),hv(V2).
2 ~ :- V2#count{V0:d(V1,V0)}V2,V2#sum{V0:d(V0,V1)}V2,hd(V2),hv(V2).
2 ~ :- V2#count{V0:d(V1,V0)}V2,V1#sum{V0:d(V0,V2)}V1,hd(V1),hv(V2),hv(V1).
2 ~ :- V2#count{V0:d(V1,V0)}V2,V1#sum{V0:d(V0,V2)}V1,hd(V2),hv(V2),hv(V1).
2 ~ :- V2#count{V0:d(V1,V0)}V2,V2#sum{V0:d(V0,V2)}V2,hd(V1),hv(V2).
2 ~ :- V2#count{V0:d(V1,V0)}V2,V2#sum{V0:d(V1,V0)}V2,hd(V1),hv(V2).
2 ~ :- V2#count{V0:d(V1,V0)}V2,V2#sum{V0:d(V1,V0)}V2,hd(V2),hv(V2).
2 ~ :- V2#count{V0:d(V1,V0)}V2,V1#sum{V0:d(V2,V0)}V1,hd(V1),hv(V2),hv(V1).
2 ~ :- V2#count{V0:d(V1,V0)}V2,V1#sum{V0:d(V2,V0)}V1,hd(V2),hv(V2),hv(V1).
2 ~ :- V2#count{V0:d(V1,V0)}V2,V2#sum{V0:d(V2,V0)}V2,hd(V1),hv(V2).
2 ~ :- V2#count{V0:d(V1,V0)}V2,V2#sum{V1:d(V0,V1)}V2,hd(V2),hv(V2).
2 ~ :- V2#count{V0:d(V1,V0)}V2,V2#sum{V1:d(V1,V0)}V2,hd(V2),hv(V2).
2 ~ :- V2#count{V0:d(V1,V0)}V2,V2#sum{V1:d(V1,V1)}V2,hd(V2),hv(V2).
2 ~ :- V2#count{V0:d(V1,V0)}V2,V2#sum{V1:d(V1,V2)}V2,hd(V2),hv(V2).
2 ~ :- V2#count{V0:d(V1,V0)}V2,V3#sum{V1:d(V1,V2)}V3,hd(V3),hv(V2),hv(V3).
2 ~ :- V2#count{V0:d(V1,V0)}V2,V2#sum{V1:d(V1,V3)}V2,hd(V3),hv(V2).
2 ~ :- V2#count{V0:d(V1,V0)}V2,V2#sum{V1:d(V2,V1)}V2,hd(V2),hv(V2).
2 ~ :- V2#count{V0:d(V1,V0)}V2,V3#sum{V1:d(V2,V1)}V3,hd(V3),hv(V2),hv(V3).
2 ~ :- V2#count{V0:d(V1,V0)}V2,V2#sum{V1:d(V3,V1)}V2,hd(V3),hv(V2).
2 ~ :- V2#count{V0:d(V1,V0)}V2,V1#sum{V3:d(V0,V3)}V1,hd(V2),hv(V2),hv(V1).
2 ~ :- V2#count{V0:d(V1,V0)}V2,V2#sum{V3:d(V0,V3)}V2,hd(V1),hv(V2).
2 ~ :- V2#count{V0:d(V1,V0)}V2,V2#sum{V3:d(V1,V3)}V2,hd(V1),hv(V2).
2 ~ :- V2#count{V0:d(V1,V0)}V2,V2#sum{V3:d(V1,V3)}V2,hd(V2),hv(V2).
2 ~ :- V2#count{V0:d(V1,V0)}V2,V1#sum{V3:d(V2,V3)}V1,hd(V1),hv(V2),hv(V1).
2 ~ :- V2#count{V0:d(V1,V0)}V2,V1#sum{V3:d(V2,V3)}V1,hd(V2),hv(V2),hv(V1).
2 ~ :- V2#count{V0:d(V1,V0)}V2,V2#sum{V3:d(V2,V3)}V2,hd(V1),hv(V2).
2 ~ :- V2#count{V0:d(V1,V0)}V2,V1#sum{V3:d(V3,V0)}V1,hd(V2),hv(V2),hv(V1).
2 ~ :- V2#count{V0:d(V1,V0)}V2,V2#sum{V3:d(V3,V0)}V2,hd(V1),hv(V2).
2 ~ :- V2#count{V0:d(V1,V0)}V2,V2#sum{V3:d(V3,V1)}V2,hd(V1),hv(V2).
2 ~ :- V2#count{V0:d(V1,V0)}V2,V2#sum{V3:d(V3,V1)}V2,hd(V2),hv(V2).
2 ~ :- V2#count{V0:d(V1,V0)}V2,V1#sum{V3:d(V3,V2)}V1,hd(V1),hv(V2),hv(V1).
2 ~ :- V2#count{V0:d(V1,V0)}V2,V1#sum{V3:d(V3,V2)}V1,hd(V2),hv(V2),hv(V1).
2 ~ :- V2#count{V0:d(V1,V0)}V2,V2#sum{V3:d(V3,V2)}V2,hd(V1),hv(V2).
2 ~ :- V2#count{V0:d(V1,V0)}V2,V1#sum{V3:d(V3,V3)}V1,hd(V2),hv(V2),hv(V1).
2 ~ :- V2#count{V0:d(V1,V0)}V2,V2#sum{V3:d(V3,V3)}V2,hd(V1),hv(V2).
2 ~ :- V2#count{V0,V1:d(V0,V1)}V2,V2#sum{V0,V1:d(V0,V1)}V2,hv(V2).
2 ~ :- V2#count{V0,V1:d(V0,V1)}V2,V2#sum{V0,V1:d(V1,V0)}V2,hv(V2).
2 ~ :- V2#count{V0,V1:d(V0,V1)}V2,V2#sum{V0,V3:d(V0,V3)}V2,hv(V2).
2 ~ :- V2#count{V0,V1:d(V0,V1)}V2,V2#sum{V0,V3:d(V3,V0)}V2,hv(V2).
2 ~ :- V2#count{V0,V1:d(V0,V1)}V2,V2#sum{V1,V0:d(V0,V1)}V2,hv(V2).
2 ~ :- V2#count{V0,V1:d(V0,V1)}V2,V2#sum{V1,V0:d(V1,V0)}V2,hv(V2).
2 ~ :- V2#count{V0,V1:d(V0,V1)}V2,V2#sum{V1,V3:d(V1,V3)}V2,hv(V2).
2 ~ :- V2#count{V0,V1:d(V0,V1)}V2,V2#sum{V1,V3:d(V3,V1)}V2,hv(V2).
2 ~ :- V2#count{V0,V1:d(V0,V1)}V2,V2#sum{V3,V0:d(V0,V3)}V2,hv(V2).
2 ~ :- V2#count{V0,V1:d(V0,V1)}V2,V2#sum{V3,V0:d(V3,V0)}V2,hv(V2).
2 ~ :- V2#count{V0,V1:d(V0,V1)}V2,V2#sum{V3,V1:d(V1,V3)}V2,hv(V2).
2 ~ :- V2#count{V0,V1:d(V0,V1)}V2,V2#sum{V3,V1:d(V3,V1)}V2,hv(V2).
2 ~ :- V2#count{V0,V1:d(V1,V0)}V2,V2#sum{V0,V1:d(V0,V1)}V2,hv(V2).
2 ~ :- V2#count{V0,V1:d(V1,V0)}V2,V2#sum{V0,V1:d(V1,V0)}V2,hv(V2).
2 ~ :- V2#count{V0,V1:d(V1,V0)}V2,V2#sum{V0,V3:d(V0,V3)}V2,hv(V2).
2 ~ :- V2#count{V0,V1:d(V1,V0)}V2,V2#sum{V0,V3:d(V3,V0)}V2,hv(V2).
2 ~ :- V2#count{V0,V1:d(V1,V0)}V2,V2#sum{V1,V0:d(V0,V1)}V2,hv(V2).
2 ~ :- V2#count{V0,V1:d(V1,V0)}V2,V2#sum{V1,V0:d(V1,V0)}V2,hv(V2).
2 ~ :- V2#count{V0,V1:d(V1,V0)}V2,V2#sum{V1,V3:d(V1,V3)}V2,hv(V2).
2 ~ :- V2#count{V0,V1:d(V1,V0)}V2,V2#sum{V1,V3:d(V3,V1)}V2,hv(V2).
2 ~ :- V2#count{V0,V1:d(V1,V0)}V2,V2#sum{V3,V0:d(V0,V3)}V2,hv(V2).
2 ~ :- V2#count{V0,V1:d(V1,V0)}V2,V2#sum{V3,V0:d(V3,V0)}V2,hv(V2).
2 ~ :- V2#count{V0,V1:d(V1,V0)}V2,V2#sum{V3,V1:d(V1,V3)}V2,hv(V2).
2 ~ :- V2#count{V0,V1:d(V1,V0)}V2,V2#sum{V3,V1:d(V3,V1)}V2,hv(V2).
2 ~ :- V1#count{V0:d(V0,V0)}V1,V2#sum{V0:d(V0,V0)}V2,V1!=V2,hv(V2),hv(V1).
2 ~ :- V1#count{V0:d(V0,V0)}V1,V2#sum{V0:d(V0,V0)}V2,V2!=V1,hv(V2),hv(V1).
2 ~ :- V1#count{V0:d(V0,V0)}V1,V2#sum{V0:d(V0,V1)}V2,V1!=V2,hv(V2),hv(V1).
2 ~ :- V1#count{V0:d(V0,V0)}V1,V2#sum{V0:d(V0,V1)}V2,V2!=V1,hv(V2),hv(V1).
2 ~ :- V1#count{V0:d(V0,V0)}V1,V2#sum{V0:d(V1,V0)}V2,V1!=V2,hv(V2),hv(V1).
2 ~ :- V1#count{V0:d(V0,V0)}V1,V2#sum{V0:d(V1,V0)}V2,V2!=V1,hv(V2),hv(V1).
2 ~ :- V1#count{V0:d(V0,V0)}V1,V3#sum{V2:d(V0,V2)}V3,V1!=V3,hv(V1),hv(V3).
2 ~ :- V1#count{V0:d(V0,V0)}V1,V3#sum{V2:d(V0,V2)}V3,V3!=V1,hv(V1),hv(V3).
2 ~ :- V1#count{V0:d(V0,V0)}V1,V3#sum{V2:d(V1,V2)}V3,V1!=V3,hv(V1),hv(V3).
2 ~ :- V1#count{V0:d(V0,V0)}V1,V3#sum{V2:d(V1,V2)}V3,V3!=V1,hv(V1),hv(V3).
2 ~ :- V1#count{V0:d(V0,V0)}V1,V3#sum{V2:d(V2,V0)}V3,V1!=V3,hv(V1),hv(V3).
2 ~ :- V1#count{V0:d(V0,V0)}V1,V3#sum{V2:d(V2,V0)}V3,V3!=V1,hv(V1),hv(V3).
2 ~ :- V1#count{V0:d(V0,V0)}V1,V3#sum{V2:d(V2,V1)}V3,V1!=V3,hv(V1),hv(V3).
2 ~ :- V1#count{V0:d(V0,V0)}V1,V3#sum{V2:d(V2,V1)}V3,V3!=V1,hv(V1),hv(V3).
2 ~ :- V1#count{V0:d(V0,V0)}V1,V3#sum{V2:d(V2,V2)}V3,V1!=V3,hv(V1),hv(V3).
2 ~ :- V1#count{V0:d(V0,V0)}V1,V3#sum{V2:d(V2,V2)}V3,V3!=V1,hv(V1),hv(V3).
2 ~ :- V2#count{V0:d(V0,V1)}V2,V1#sum{V0:d(V0,V0)}V1,V1!=V2,hv(V2),hv(V1).
2 ~ :- V2#count{V0:d(V0,V1)}V2,V1#sum{V0:d(V0,V0)}V1,V2!=V1,hv(V2),hv(V1).
2 ~ :- V2#count{V0:d(V0,V1)}V2,V3#sum{V0:d(V0,V1)}V3,V2!=V3,hv(V2),hv(V3).
2 ~ :- V2#count{V0:d(V0,V1)}V2,V3#sum{V0:d(V0,V1)}V3,V3!=V2,hv(V2),hv(V3).
2 ~ :- V2#count{V0:d(V0,V1)}V2,V3#sum{V0:d(V1,V0)}V3,V2!=V3,hv(V2),hv(V3).
2 ~ :- V2#count{V0:d(V0,V1)}V2,V3#sum{V0:d(V1,V0)}V3,V3!=V2,hv(V2),hv(V3).
2 ~ :- V2#count{V0:d(V0,V1)}V2,V3#sum{V1:d(V0,V1)}V3,V2!=V3,hv(V2),hv(V3).
2 ~ :- V2#count{V0:d(V0,V1)}V2,V3#sum{V1:d(V0,V1)}V3,V3!=V2,hv(V2),hv(V3).
2 ~ :- V2#count{V0:d(V0,V1)}V2,V3#sum{V1:d(V1,V0)}V3,V2!=V3,hv(V2),hv(V3).
2 ~ :- V2#count{V0:d(V0,V1)}V2,V3#sum{V1:d(V1,V0)}V3,V3!=V2,hv(V2),hv(V3).
2 ~ :- V2#count{V0:d(V0,V1)}V2,V3#sum{V1:d(V1,V1)}V3,V2!=V3,hv(V2),hv(V3).
2 ~ :- V2#count{V0:d(V0,V1)}V2,V3#sum{V1:d(V1,V1)}V3,V3!=V2,hv(V2),hv(V3).
2 ~ :- V2#count{V0:d(V0,V1)}V2,V3#sum{V1:d(V1,V2)}V3,V2!=V3,hv(V2),hv(V3).
2 ~ :- V2#count{V0:d(V0,V1)}V2,V3#sum{V1:d(V1,V2)}V3,V3!=V2,hv(V2),hv(V3).
2 ~ :- V2#count{V0:d(V0,V1)}V2,V3#sum{V1:d(V2,V1)}V3,V2!=V3,hv(V2),hv(V3).
2 ~ :- V2#count{V0:d(V0,V1)}V2,V3#sum{V1:d(V2,V1)}V3,V3!=V2,hv(V2),hv(V3).
2 ~ :- V2#count{V0:d(V0,V1)}V2,V1#sum{V3:d(V0,V3)}V1,V1!=V2,hv(V2),hv(V1).
2 ~ :- V2#count{V0:d(V0,V1)}V2,V1#sum{V3:d(V0,V3)}V1,V2!=V1,hv(V2),hv(V1).
2 ~ :- V2#count{V0:d(V0,V1)}V2,V1#sum{V3:d(V3,V0)}V1,V1!=V2,hv(V2),hv(V1).
2 ~ :- V2#count{V0:d(V0,V1)}V2,V1#sum{V3:d(V3,V0)}V1,V2!=V1,hv(V2),hv(V1).
2 ~ :- V2#count{V0:d(V0,V1)}V2,V1#sum{V3:d(V3,V3)}V1,V1!=V2,hv(V2),hv(V1).
2 ~ :- V2#count{V0:d(V0,V1)}V2,V1#sum{V3:d(V3,V3)}V1,V2!=V1,hv(V2),hv(V1).
2 ~ :- V2#count{V0:d(V1,V0)}V2,V1#sum{V0:d(V0,V0)}V1,V1!=V2,hv(V2),hv(V1).
2 ~ :- V2#count{V0:d(V1,V0)}V2,V1#sum{V0:d(V0,V0)}V1,V2!=V1,hv(V2),hv(V1).
2 ~ :- V2#count{V0:d(V1,V0)}V2,V3#sum{V0:d(V0,V1)}V3,V2!=V3,hv(V2),hv(V3).
2 ~ :- V2#count{V0:d(V1,V0)}V2,V3#sum{V0:d(V0,V1)}V3,V3!=V2,hv(V2),hv(V3).
2 ~ :- V2#count{V0:d(V1,V0)}V2,V3#sum{V0:d(V1,V0)}V3,V2!=V3,hv(V2),hv(V3).
2 ~ :- V2#count{V0:d(V1,V0)}V2,V3#sum{V0:d(V1,V0)}V3,V3!=V2,hv(V2),hv(V3).
2 ~ :- V2#count{V0:d(V1,V0)}V2,V3#sum{V1:d(V0,V1)}V3,V2!=V3,hv(V2),hv(V3).
2 ~ :- V2#count{V0:d(V1,V0)}V2,V3#sum{V1:d(V0,V1)}V3,V3!=V2,hv(V2),hv(V3).
2 ~ :- V2#count{V0:d(V1,V0)}V2,V3#sum{V1:d(V1,V0)}V3,V2!=V3,hv(V2),hv(V3).
2 ~ :- V2#count{V0:d(V1,V0)}V2,V3#sum{V1:d(V1,V0)}V3,V3!=V2,hv(V2),hv(V3).
2 ~ :- V2#count{V0:d(V1,V0)}V2,V3#sum{V1:d(V1,V1)}V3,V2!=V3,hv(V2),hv(V3).
2 ~ :- V2#count{V0:d(V1,V0)}V2,V3#sum{V1:d(V1,V1)}V3,V3!=V2,hv(V2),hv(V3).
2 ~ :- V2#count{V0:d(V1,V0)}V2,V3#sum{V1:d(V1,V2)}V3,V2!=V3,hv(V2),hv(V3).
2 ~ :- V2#count{V0:d(V1,V0)}V2,V3#sum{V1:d(V1,V2)}V3,V3!=V2,hv(V2),hv(V3).
2 ~ :- V2#count{V0:d(V1,V0)}V2,V3#sum{V1:d(V2,V1)}V3,V2!=V3,hv(V2),hv(V3).
2 ~ :- V2#count{V0:d(V1,V0)}V2,V3#sum{V1:d(V2,V1)}V3,V3!=V2,hv(V2),hv(V3).
2 ~ :- V2#count{V0:d(V1,V0)}V2,V1#sum{V3:d(V0,V3)}V1,V1!=V2,hv(V2),hv(V1).
2 ~ :- V2#count{V0:d(V1,V0)}V2,V1#sum{V3:d(V0,V3)}V1,V2!=V1,hv(V2),hv(V1).
2 ~ :- V2#count{V0:d(V1,V0)}V2,V1#sum{V3:d(V3,V0)}V1,V1!=V2,hv(V2),hv(V1).
2 ~ :- V2#count{V0:d(V1,V0)}V2,V1#sum{V3:d(V3,V0)}V1,V2!=V1,hv(V2),hv(V1).
2 ~ :- V2#count{V0:d(V1,V0)}V2,V1#sum{V3:d(V3,V3)}V1,V1!=V2,hv(V2),hv(V1).
2 ~ :- V2#count{V0:d(V1,V0)}V2,V1#sum{V3:d(V3,V3)}V1,V2!=V1,hv(V2),hv(V1).
2 ~ :- V2#count{V0,V1:d(V0,V1)}V2,V2#sum{V0:d(V0,V0)}V2,hd(V2),hv(V2).
2 ~ :- V2#count{V0,V1:d(V0,V1)}V2,V2#sum{V0:d(V0,V1)}V2,hd(V2),hv(V2).
2 ~ :- V2#count{V0,V1:d(V0,V1)}V2,V2#sum{V0:d(V0,V2)}V2,hd(V2),hv(V2).
2 ~ :- V2#count{V0,V1:d(V0,V1)}V2,V3#sum{V0:d(V0,V2)}V3,hd(V3),hv(V2),hv(V3).
2 ~ :- V2#count{V0,V1:d(V0,V1)}V2,V2#sum{V0:d(V0,V3)}V2,hd(V3),hv(V2).
2 ~ :- V2#count{V0,V1:d(V0,V1)}V2,V2#sum{V0:d(V1,V0)}V2,hd(V2),hv(V2).
2 ~ :- V2#count{V0,V1:d(V0,V1)}V2,V2#sum{V0:d(V2,V0)}V2,hd(V2),hv(V2).
2 ~ :- V2#count{V0,V1:d(V0,V1)}V2,V3#sum{V0:d(V2,V0)}V3,hd(V3),hv(V2),hv(V3).
2 ~ :- V2#count{V0,V1:d(V0,V1)}V2,V2#sum{V0:d(V3,V0)}V2,hd(V3),hv(V2).
2 ~ :- V2#count{V0,V1:d(V0,V1)}V2,V2#sum{V1:d(V0,V1)}V2,hd(V2),hv(V2).
2 ~ :- V2#count{V0,V1:d(V0,V1)}V2,V2#sum{V1:d(V1,V0)}V2,hd(V2),hv(V2).
2 ~ :- V2#count{V0,V1:d(V0,V1)}V2,V2#sum{V1:d(V1,V1)}V2,hd(V2),hv(V2).
2 ~ :- V2#count{V0,V1:d(V0,V1)}V2,V2#sum{V1:d(V1,V2)}V2,hd(V2),hv(V2).
2 ~ :- V2#count{V0,V1:d(V0,V1)}V2,V3#sum{V1:d(V1,V2)}V3,hd(V3),hv(V2),hv(V3).
2 ~ :- V2#count{V0,V1:d(V0,V1)}V2,V2#sum{V1:d(V1,V3)}V2,hd(V3),hv(V2).
2 ~ :- V2#count{V0,V1:d(V0,V1)}V2,V2#sum{V1:d(V2,V1)}V2,hd(V2),hv(V2).
2 ~ :- V2#count{V0,V1:d(V0,V1)}V2,V3#sum{V1:d(V2,V1)}V3,hd(V3),hv(V2),hv(V3).
2 ~ :- V2#count{V0,V1:d(V0,V1)}V2,V2#sum{V1:d(V3,V1)}V2,hd(V3),hv(V2).
2 ~ :- V2#count{V0,V1:d(V0,V1)}V2,V2#sum{V3:d(V0,V3)}V2,hd(V2),hv(V2).
2 ~ :- V2#count{V0,V1:d(V0,V1)}V2,V2#sum{V3:d(V1,V3)}V2,hd(V2),hv(V2).
2 ~ :- V2#count{V0,V1:d(V0,V1)}V2,V2#sum{V3:d(V2,V3)}V2,hd(V2),hv(V2).
2 ~ :- V2#count{V0,V1:d(V0,V1)}V2,V2#sum{V3:d(V3,V0)}V2,hd(V2),hv(V2).
2 ~ :- V2#count{V0,V1:d(V0,V1)}V2,V2#sum{V3:d(V3,V1)}V2,hd(V2),hv(V2).
2 ~ :- V2#count{V0,V1:d(V0,V1)}V2,V2#sum{V3:d(V3,V2)}V2,hd(V2),hv(V2).
2 ~ :- V2#count{V0,V1:d(V0,V1)}V2,V2#sum{V3:d(V3,V3)}V2,hd(V2),hv(V2).
2 ~ :- V2#count{V0,V1:d(V1,V0)}V2,V2#sum{V0:d(V0,V0)}V2,hd(V2),hv(V2).
2 ~ :- V2#count{V0,V1:d(V1,V0)}V2,V2#sum{V0:d(V0,V1)}V2,hd(V2),hv(V2).
2 ~ :- V2#count{V0,V1:d(V1,V0)}V2,V2#sum{V0:d(V0,V2)}V2,hd(V2),hv(V2).
2 ~ :- V2#count{V0,V1:d(V1,V0)}V2,V3#sum{V0:d(V0,V2)}V3,hd(V3),hv(V2),hv(V3).
2 ~ :- V2#count{V0,V1:d(V1,V0)}V2,V2#sum{V0:d(V0,V3)}V2,hd(V3),hv(V2).
2 ~ :- V2#count{V0,V1:d(V1,V0)}V2,V2#sum{V0:d(V1,V0)}V2,hd(V2),hv(V2).
2 ~ :- V2#count{V0,V1:d(V1,V0)}V2,V2#sum{V0:d(V2,V0)}V2,hd(V2),hv(V2).
2 ~ :- V2#count{V0,V1:d(V1,V0)}V2,V3#sum{V0:d(V2,V0)}V3,hd(V3),hv(V2),hv(V3).
2 ~ :- V2#count{V0,V1:d(V1,V0)}V2,V2#sum{V0:d(V3,V0)}V2,hd(V3),hv(V2).
2 ~ :- V2#count{V0,V1:d(V1,V0)}V2,V2#sum{V1:d(V0,V1)}V2,hd(V2),hv(V2).
2 ~ :- V2#count{V0,V1:d(V1,V0)}V2,V2#sum{V1:d(V1,V0)}V2,hd(V2),hv(V2).
2 ~ :- V2#count{V0,V1:d(V1,V0)}V2,V2#sum{V1:d(V1,V1)}V2,hd(V2),hv(V2).
2 ~ :- V2#count{V0,V1:d(V1,V0)}V2,V2#sum{V1:d(V1,V2)}V2,hd(V2),hv(V2).
2 ~ :- V2#count{V0,V1:d(V1,V0)}V2,V3#sum{V1:d(V1,V2)}V3,hd(V3),hv(V2),hv(V3).
2 ~ :- V2#count{V0,V1:d(V1,V0)}V2,V2#sum{V1:d(V1,V3)}V2,hd(V3),hv(V2).
2 ~ :- V2#count{V0,V1:d(V1,V0)}V2,V2#sum{V1:d(V2,V1)}V2,hd(V2),hv(V2).
2 ~ :- V2#count{V0,V1:d(V1,V0)}V2,V3#sum{V1:d(V2,V1)}V3,hd(V3),hv(V2),hv(V3).
2 ~ :- V2#count{V0,V1:d(V1,V0)}V2,V2#sum{V1:d(V3,V1)}V2,hd(V3),hv(V2).
2 ~ :- V2#count{V0,V1:d(V1,V0)}V2,V2#sum{V3:d(V0,V3)}V2,hd(V2),hv(V2).
2 ~ :- V2#count{V0,V1:d(V1,V0)}V2,V2#sum{V3:d(V1,V3)}V2,hd(V2),hv(V2).
2 ~ :- V2#count{V0,V1:d(V1,V0)}V2,V2#sum{V3:d(V2,V3)}V2,hd(V2),hv(V2).
2 ~ :- V2#count{V0,V1:d(V1,V0)}V2,V2#sum{V3:d(V3,V0)}V2,hd(V2),hv(V2).
2 ~ :- V2#count{V0,V1:d(V1,V0)}V2,V2#sum{V3:d(V3,V1)}V2,hd(V2),hv(V2).
2 ~ :- V2#count{V0,V1:d(V1,V0)}V2,V2#sum{V3:d(V3,V2)}V2,hd(V2),hv(V2).
2 ~ :- V2#count{V0,V1:d(V1,V0)}V2,V2#sum{V3:d(V3,V3)}V2,hd(V2),hv(V2).
2 ~ :- V1#count{V0:d(V0,V0)}V1,V1#sum{V0,V2:d(V0,V2)}V1,hd(V1),hv(V1).
2 ~ :- V1#count{V0:d(V0,V0)}V1,V1#sum{V0,V2:d(V2,V0)}V1,hd(V1),hv(V1).
2 ~ :- V1#count{V0:d(V0,V0)}V1,V1#sum{V2,V0:d(V0,V2)}V1,hd(V1),hv(V1).
2 ~ :- V1#count{V0:d(V0,V0)}V1,V1#sum{V2,V0:d(V2,V0)}V1,hd(V1),hv(V1).
2 ~ :- V1#count{V0:d(V0,V0)}V1,V1#sum{V2,V3:d(V2,V3)}V1,hd(V1),hv(V1).
2 ~ :- V1#count{V0:d(V0,V0)}V1,V1#sum{V2,V3:d(V3,V2)}V1,hd(V1),hv(V1).
2 ~ :- V1#count{V0:d(V0,V1)}V1,V1#sum{V0,V2:d(V0,V2)}V1,hd(V1),hv(V1).
2 ~ :- V1#count{V0:d(V0,V1)}V1,V1#sum{V0,V2:d(V2,V0)}V1,hd(V1),hv(V1).
2 ~ :- V1#count{V0:d(V0,V1)}V1,V1#sum{V2,V0:d(V0,V2)}V1,hd(V1),hv(V1).
2 ~ :- V1#count{V0:d(V0,V1)}V1,V1#sum{V2,V0:d(V2,V0)}V1,hd(V1),hv(V1).
2 ~ :- V1#count{V0:d(V0,V1)}V1,V1#sum{V2,V3:d(V2,V3)}V1,hd(V1),hv(V1).
2 ~ :- V1#count{V0:d(V0,V1)}V1,V1#sum{V2,V3:d(V3,V2)}V1,hd(V1),hv(V1).
2 ~ :- V2#count{V0:d(V0,V1)}V2,V2#sum{V0,V1:d(V0,V1)}V2,hd(V2),hv(V2).
2 ~ :- V2#count{V0:d(V0,V1)}V2,V2#sum{V0,V1:d(V1,V0)}V2,hd(V2),hv(V2).
2 ~ :- V2#count{V0:d(V0,V1)}V2,V1#sum{V0,V3:d(V0,V3)}V1,hd(V2),hv(V2),hv(V1).
2 ~ :- V2#count{V0:d(V0,V1)}V2,V2#sum{V0,V3:d(V0,V3)}V2,hd(V1),hv(V2).
2 ~ :- V2#count{V0:d(V0,V1)}V2,V1#sum{V0,V3:d(V3,V0)}V1,hd(V2),hv(V2),hv(V1).
2 ~ :- V2#count{V0:d(V0,V1)}V2,V2#sum{V0,V3:d(V3,V0)}V2,hd(V1),hv(V2).
2 ~ :- V2#count{V0:d(V0,V1)}V2,V2#sum{V1,V0:d(V0,V1)}V2,hd(V2),hv(V2).
2 ~ :- V2#count{V0:d(V0,V1)}V2,V2#sum{V1,V0:d(V1,V0)}V2,hd(V2),hv(V2).
2 ~ :- V2#count{V0:d(V0,V1)}V2,V2#sum{V1,V3:d(V1,V3)}V2,hd(V2),hv(V2).
2 ~ :- V2#count{V0:d(V0,V1)}V2,V2#sum{V1,V3:d(V3,V1)}V2,hd(V2),hv(V2).
2 ~ :- V2#count{V0:d(V0,V1)}V2,V1#sum{V3,V0:d(V0,V3)}V1,hd(V2),hv(V2),hv(V1).
2 ~ :- V2#count{V0:d(V0,V1)}V2,V2#sum{V3,V0:d(V0,V3)}V2,hd(V1),hv(V2).
2 ~ :- V2#count{V0:d(V0,V1)}V2,V1#sum{V3,V0:d(V3,V0)}V1,hd(V2),hv(V2),hv(V1).
2 ~ :- V2#count{V0:d(V0,V1)}V2,V2#sum{V3,V0:d(V3,V0)}V2,hd(V1),hv(V2).
2 ~ :- V2#count{V0:d(V0,V1)}V2,V2#sum{V3,V1:d(V1,V3)}V2,hd(V2),hv(V2).
2 ~ :- V2#count{V0:d(V0,V1)}V2,V2#sum{V3,V1:d(V3,V1)}V2,hd(V2),hv(V2).
2 ~ :- V1#count{V0:d(V1,V0)}V1,V1#sum{V0,V2:d(V0,V2)}V1,hd(V1),hv(V1).
2 ~ :- V1#count{V0:d(V1,V0)}V1,V1#sum{V0,V2:d(V2,V0)}V1,hd(V1),hv(V1).
2 ~ :- V1#count{V0:d(V1,V0)}V1,V1#sum{V2,V0:d(V0,V2)}V1,hd(V1),hv(V1).
2 ~ :- V1#count{V0:d(V1,V0)}V1,V1#sum{V2,V0:d(V2,V0)}V1,hd(V1),hv(V1).
2 ~ :- V1#count{V0:d(V1,V0)}V1,V1#sum{V2,V3:d(V2,V3)}V1,hd(V1),hv(V1).
2 ~ :- V1#count{V0:d(V1,V0)}V1,V1#sum{V2,V3:d(V3,V2)}V1,hd(V1),hv(V1).
2 ~ :- V2#count{V0:d(V1,V0)}V2,V2#sum{V0,V1:d(V0,V1)}V2,hd(V2),hv(V2).
2 ~ :- V2#count{V0:d(V1,V0)}V2,V2#sum{V0,V1:d(V1,V0)}V2,hd(V2),hv(V2).
2 ~ :- V2#count{V0:d(V1,V0)}V2,V1#sum{V0,V3:d(V0,V3)}V1,hd(V2),hv(V2),hv(V1).
2 ~ :- V2#count{V0:d(V1,V0)}V2,V2#sum{V0,V3:d(V0,V3)}V2,hd(V1),hv(V2).
2 ~ :- V2#count{V0:d(V1,V0)}V2,V1#sum{V0,V3:d(V3,V0)}V1,hd(V2),hv(V2),hv(V1).
2 ~ :- V2#count{V0:d(V1,V0)}V2,V2#sum{V0,V3:d(V3,V0)}V2,hd(V1),hv(V2).
2 ~ :- V2#count{V0:d(V1,V0)}V2,V2#sum{V1,V0:d(V0,V1)}V2,hd(V2),hv(V2).
2 ~ :- V2#count{V0:d(V1,V0)}V2,V2#sum{V1,V0:d(V1,V0)}V2,hd(V2),hv(V2).
2 ~ :- V2#count{V0:d(V1,V0)}V2,V2#sum{V1,V3:d(V1,V3)}V2,hd(V2),hv(V2).
2 ~ :- V2#count{V0:d(V1,V0)}V2,V2#sum{V1,V3:d(V3,V1)}V2,hd(V2),hv(V2).
2 ~ :- V2#count{V0:d(V1,V0)}V2,V1#sum{V3,V0:d(V0,V3)}V1,hd(V2),hv(V2),hv(V1).
2 ~ :- V2#count{V0:d(V1,V0)}V2,V2#sum{V3,V0:d(V0,V3)}V2,hd(V1),hv(V2).
2 ~ :- V2#count{V0:d(V1,V0)}V2,V1#sum{V3,V0:d(V3,V0)}V1,hd(V2),hv(V2),hv(V1).
2 ~ :- V2#count{V0:d(V1,V0)}V2,V2#sum{V3,V0:d(V3,V0)}V2,hd(V1),hv(V2).
2 ~ :- V2#count{V0:d(V1,V0)}V2,V2#sum{V3,V1:d(V1,V3)}V2,hd(V2),hv(V2).
2 ~ :- V2#count{V0:d(V1,V0)}V2,V2#sum{V3,V1:d(V3,V1)}V2,hd(V2),hv(V2).
2 ~ :- V2#count{V0,V1:d(V0,V1)}V2,V3#sum{V0:d(V0,V0)}V3,V2!=V3,hv(V2),hv(V3).
2 ~ :- V2#count{V0,V1:d(V0,V1)}V2,V3#sum{V0:d(V0,V0)}V3,V3!=V2,hv(V2),hv(V3).
2 ~ :- V2#count{V0,V1:d(V0,V1)}V2,V3#sum{V0:d(V0,V1)}V3,V2!=V3,hv(V2),hv(V3).
2 ~ :- V2#count{V0,V1:d(V0,V1)}V2,V3#sum{V0:d(V0,V1)}V3,V3!=V2,hv(V2),hv(V3).
2 ~ :- V2#count{V0,V1:d(V0,V1)}V2,V3#sum{V0:d(V0,V2)}V3,V2!=V3,hv(V2),hv(V3).
2 ~ :- V2#count{V0,V1:d(V0,V1)}V2,V3#sum{V0:d(V0,V2)}V3,V3!=V2,hv(V2),hv(V3).
2 ~ :- V2#count{V0,V1:d(V0,V1)}V2,V3#sum{V0:d(V1,V0)}V3,V2!=V3,hv(V2),hv(V3).
2 ~ :- V2#count{V0,V1:d(V0,V1)}V2,V3#sum{V0:d(V1,V0)}V3,V3!=V2,hv(V2),hv(V3).
2 ~ :- V2#count{V0,V1:d(V0,V1)}V2,V3#sum{V0:d(V2,V0)}V3,V2!=V3,hv(V2),hv(V3).
2 ~ :- V2#count{V0,V1:d(V0,V1)}V2,V3#sum{V0:d(V2,V0)}V3,V3!=V2,hv(V2),hv(V3).
2 ~ :- V2#count{V0,V1:d(V0,V1)}V2,V3#sum{V1:d(V0,V1)}V3,V2!=V3,hv(V2),hv(V3).
2 ~ :- V2#count{V0,V1:d(V0,V1)}V2,V3#sum{V1:d(V0,V1)}V3,V3!=V2,hv(V2),hv(V3).
2 ~ :- V2#count{V0,V1:d(V0,V1)}V2,V3#sum{V1:d(V1,V0)}V3,V2!=V3,hv(V2),hv(V3).
2 ~ :- V2#count{V0,V1:d(V0,V1)}V2,V3#sum{V1:d(V1,V0)}V3,V3!=V2,hv(V2),hv(V3).
2 ~ :- V2#count{V0,V1:d(V0,V1)}V2,V3#sum{V1:d(V1,V1)}V3,V2!=V3,hv(V2),hv(V3).
2 ~ :- V2#count{V0,V1:d(V0,V1)}V2,V3#sum{V1:d(V1,V1)}V3,V3!=V2,hv(V2),hv(V3).
2 ~ :- V2#count{V0,V1:d(V0,V1)}V2,V3#sum{V1:d(V1,V2)}V3,V2!=V3,hv(V2),hv(V3).
2 ~ :- V2#count{V0,V1:d(V0,V1)}V2,V3#sum{V1:d(V1,V2)}V3,V3!=V2,hv(V2),hv(V3).
2 ~ :- V2#count{V0,V1:d(V0,V1)}V2,V3#sum{V1:d(V2,V1)}V3,V2!=V3,hv(V2),hv(V3).
2 ~ :- V2#count{V0,V1:d(V0,V1)}V2,V3#sum{V1:d(V2,V1)}V3,V3!=V2,hv(V2),hv(V3).
2 ~ :- V2#count{V0,V1:d(V1,V0)}V2,V3#sum{V0:d(V0,V0)}V3,V2!=V3,hv(V2),hv(V3).
2 ~ :- V2#count{V0,V1:d(V1,V0)}V2,V3#sum{V0:d(V0,V0)}V3,V3!=V2,hv(V2),hv(V3).
2 ~ :- V2#count{V0,V1:d(V1,V0)}V2,V3#sum{V0:d(V0,V1)}V3,V2!=V3,hv(V2),hv(V3).
2 ~ :- V2#count{V0,V1:d(V1,V0)}V2,V3#sum{V0:d(V0,V1)}V3,V3!=V2,hv(V2),hv(V3).
2 ~ :- V2#count{V0,V1:d(V1,V0)}V2,V3#sum{V0:d(V0,V2)}V3,V2!=V3,hv(V2),hv(V3).
2 ~ :- V2#count{V0,V1:d(V1,V0)}V2,V3#sum{V0:d(V0,V2)}V3,V3!=V2,hv(V2),hv(V3).
2 ~ :- V2#count{V0,V1:d(V1,V0)}V2,V3#sum{V0:d(V1,V0)}V3,V2!=V3,hv(V2),hv(V3).
2 ~ :- V2#count{V0,V1:d(V1,V0)}V2,V3#sum{V0:d(V1,V0)}V3,V3!=V2,hv(V2),hv(V3).
2 ~ :- V2#count{V0,V1:d(V1,V0)}V2,V3#sum{V0:d(V2,V0)}V3,V2!=V3,hv(V2),hv(V3).
2 ~ :- V2#count{V0,V1:d(V1,V0)}V2,V3#sum{V0:d(V2,V0)}V3,V3!=V2,hv(V2),hv(V3).
2 ~ :- V2#count{V0,V1:d(V1,V0)}V2,V3#sum{V1:d(V0,V1)}V3,V2!=V3,hv(V2),hv(V3).
2 ~ :- V2#count{V0,V1:d(V1,V0)}V2,V3#sum{V1:d(V0,V1)}V3,V3!=V2,hv(V2),hv(V3).
2 ~ :- V2#count{V0,V1:d(V1,V0)}V2,V3#sum{V1:d(V1,V0)}V3,V2!=V3,hv(V2),hv(V3).
2 ~ :- V2#count{V0,V1:d(V1,V0)}V2,V3#sum{V1:d(V1,V0)}V3,V3!=V2,hv(V2),hv(V3).
2 ~ :- V2#count{V0,V1:d(V1,V0)}V2,V3#sum{V1:d(V1,V1)}V3,V2!=V3,hv(V2),hv(V3).
2 ~ :- V2#count{V0,V1:d(V1,V0)}V2,V3#sum{V1:d(V1,V1)}V3,V3!=V2,hv(V2),hv(V3).
2 ~ :- V2#count{V0,V1:d(V1,V0)}V2,V3#sum{V1:d(V1,V2)}V3,V2!=V3,hv(V2),hv(V3).
2 ~ :- V2#count{V0,V1:d(V1,V0)}V2,V3#sum{V1:d(V1,V2)}V3,V3!=V2,hv(V2),hv(V3).
2 ~ :- V2#count{V0,V1:d(V1,V0)}V2,V3#sum{V1:d(V2,V1)}V3,V2!=V3,hv(V2),hv(V3).
2 ~ :- V2#count{V0,V1:d(V1,V0)}V2,V3#sum{V1:d(V2,V1)}V3,V3!=V2,hv(V2),hv(V3).
2 ~ :- V1#count{V0:d(V0,V0)}V1,V3#sum{V0,V2:d(V0,V2)}V3,V1!=V3,hv(V1),hv(V3).
2 ~ :- V1#count{V0:d(V0,V0)}V1,V3#sum{V0,V2:d(V0,V2)}V3,V3!=V1,hv(V1),hv(V3).
2 ~ :- V1#count{V0:d(V0,V0)}V1,V3#sum{V0,V2:d(V2,V0)}V3,V1!=V3,hv(V1),hv(V3).
2 ~ :- V1#count{V0:d(V0,V0)}V1,V3#sum{V0,V2:d(V2,V0)}V3,V3!=V1,hv(V1),hv(V3).
2 ~ :- V1#count{V0:d(V0,V0)}V1,V3#sum{V2,V0:d(V0,V2)}V3,V1!=V3,hv(V1),hv(V3).
2 ~ :- V1#count{V0:d(V0,V0)}V1,V3#sum{V2,V0:d(V0,V2)}V3,V3!=V1,hv(V1),hv(V3).
2 ~ :- V1#count{V0:d(V0,V0)}V1,V3#sum{V2,V0:d(V2,V0)}V3,V1!=V3,hv(V1),hv(V3).
2 ~ :- V1#count{V0:d(V0,V0)}V1,V3#sum{V2,V0:d(V2,V0)}V3,V3!=V1,hv(V1),hv(V3).
2 ~ :- V2#count{V0:d(V0,V1)}V2,V3#sum{V0,V1:d(V0,V1)}V3,V2!=V3,hv(V2),hv(V3).
2 ~ :- V2#count{V0:d(V0,V1)}V2,V3#sum{V0,V1:d(V0,V1)}V3,V3!=V2,hv(V2),hv(V3).
2 ~ :- V2#count{V0:d(V0,V1)}V2,V3#sum{V0,V1:d(V1,V0)}V3,V2!=V3,hv(V2),hv(V3).
2 ~ :- V2#count{V0:d(V0,V1)}V2,V3#sum{V0,V1:d(V1,V0)}V3,V3!=V2,hv(V2),hv(V3).
2 ~ :- V2#count{V0:d(V0,V1)}V2,V1#sum{V0,V3:d(V0,V3)}V1,V1!=V2,hv(V2),hv(V1).
2 ~ :- V2#count{V0:d(V0,V1)}V2,V1#sum{V0,V3:d(V0,V3)}V1,V2!=V1,hv(V2),hv(V1).
2 ~ :- V2#count{V0:d(V0,V1)}V2,V1#sum{V0,V3:d(V3,V0)}V1,V1!=V2,hv(V2),hv(V1).
2 ~ :- V2#count{V0:d(V0,V1)}V2,V1#sum{V0,V3:d(V3,V0)}V1,V2!=V1,hv(V2),hv(V1).
2 ~ :- V2#count{V0:d(V0,V1)}V2,V3#sum{V1,V0:d(V0,V1)}V3,V2!=V3,hv(V2),hv(V3).
2 ~ :- V2#count{V0:d(V0,V1)}V2,V3#sum{V1,V0:d(V0,V1)}V3,V3!=V2,hv(V2),hv(V3).
2 ~ :- V2#count{V0:d(V0,V1)}V2,V3#sum{V1,V0:d(V1,V0)}V3,V2!=V3,hv(V2),hv(V3).
2 ~ :- V2#count{V0:d(V0,V1)}V2,V3#sum{V1,V0:d(V1,V0)}V3,V3!=V2,hv(V2),hv(V3).
2 ~ :- V2#count{V0:d(V0,V1)}V2,V1#sum{V3,V0:d(V0,V3)}V1,V1!=V2,hv(V2),hv(V1).
2 ~ :- V2#count{V0:d(V0,V1)}V2,V1#sum{V3,V0:d(V0,V3)}V1,V2!=V1,hv(V2),hv(V1).
2 ~ :- V2#count{V0:d(V0,V1)}V2,V1#sum{V3,V0:d(V3,V0)}V1,V1!=V2,hv(V2),hv(V1).
2 ~ :- V2#count{V0:d(V0,V1)}V2,V1#sum{V3,V0:d(V3,V0)}V1,V2!=V1,hv(V2),hv(V1).
2 ~ :- V2#count{V0:d(V1,V0)}V2,V3#sum{V0,V1:d(V0,V1)}V3,V2!=V3,hv(V2),hv(V3).
2 ~ :- V2#count{V0:d(V1,V0)}V2,V3#sum{V0,V1:d(V0,V1)}V3,V3!=V2,hv(V2),hv(V3).
2 ~ :- V2#count{V0:d(V1,V0)}V2,V3#sum{V0,V1:d(V1,V0)}V3,V2!=V3,hv(V2),hv(V3).
2 ~ :- V2#count{V0:d(V1,V0)}V2,V3#sum{V0,V1:d(V1,V0)}V3,V3!=V2,hv(V2),hv(V3).
2 ~ :- V2#count{V0:d(V1,V0)}V2,V1#sum{V0,V3:d(V0,V3)}V1,V1!=V2,hv(V2),hv(V1).
2 ~ :- V2#count{V0:d(V1,V0)}V2,V1#sum{V0,V3:d(V0,V3)}V1,V2!=V1,hv(V2),hv(V1).
2 ~ :- V2#count{V0:d(V1,V0)}V2,V1#sum{V0,V3:d(V3,V0)}V1,V1!=V2,hv(V2),hv(V1).
2 ~ :- V2#count{V0:d(V1,V0)}V2,V1#sum{V0,V3:d(V3,V0)}V1,V2!=V1,hv(V2),hv(V1).
2 ~ :- V2#count{V0:d(V1,V0)}V2,V3#sum{V1,V0:d(V0,V1)}V3,V2!=V3,hv(V2),hv(V3).
2 ~ :- V2#count{V0:d(V1,V0)}V2,V3#sum{V1,V0:d(V0,V1)}V3,V3!=V2,hv(V2),hv(V3).
2 ~ :- V2#count{V0:d(V1,V0)}V2,V3#sum{V1,V0:d(V1,V0)}V3,V2!=V3,hv(V2),hv(V3).
2 ~ :- V2#count{V0:d(V1,V0)}V2,V3#sum{V1,V0:d(V1,V0)}V3,V3!=V2,hv(V2),hv(V3).
2 ~ :- V2#count{V0:d(V1,V0)}V2,V1#sum{V3,V0:d(V0,V3)}V1,V1!=V2,hv(V2),hv(V1).
2 ~ :- V2#count{V0:d(V1,V0)}V2,V1#sum{V3,V0:d(V0,V3)}V1,V2!=V1,hv(V2),hv(V1).
2 ~ :- V2#count{V0:d(V1,V0)}V2,V1#sum{V3,V0:d(V3,V0)}V1,V1!=V2,hv(V2),hv(V1).
2 ~ :- V2#count{V0:d(V1,V0)}V2,V1#sum{V3,V0:d(V3,V0)}V1,V2!=V1,hv(V2),hv(V1).
2 ~ :- V2#count{V0,V1:d(V0,V1)}V2,V2#sum{V0,V1:d(V0,V1)}V2,hd(V2),hv(V2).
2 ~ :- V2#count{V0,V1:d(V0,V1)}V2,V2#sum{V0,V1:d(V1,V0)}V2,hd(V2),hv(V2).
2 ~ :- V2#count{V0,V1:d(V0,V1)}V2,V2#sum{V0,V3:d(V0,V3)}V2,hd(V2),hv(V2).
2 ~ :- V2#count{V0,V1:d(V0,V1)}V2,V2#sum{V0,V3:d(V3,V0)}V2,hd(V2),hv(V2).
2 ~ :- V2#count{V0,V1:d(V0,V1)}V2,V2#sum{V1,V0:d(V0,V1)}V2,hd(V2),hv(V2).
2 ~ :- V2#count{V0,V1:d(V0,V1)}V2,V2#sum{V1,V0:d(V1,V0)}V2,hd(V2),hv(V2).
2 ~ :- V2#count{V0,V1:d(V0,V1)}V2,V2#sum{V1,V3:d(V1,V3)}V2,hd(V2),hv(V2).
2 ~ :- V2#count{V0,V1:d(V0,V1)}V2,V2#sum{V1,V3:d(V3,V1)}V2,hd(V2),hv(V2).
2 ~ :- V2#count{V0,V1:d(V0,V1)}V2,V2#sum{V3,V0:d(V0,V3)}V2,hd(V2),hv(V2).
2 ~ :- V2#count{V0,V1:d(V0,V1)}V2,V2#sum{V3,V0:d(V3,V0)}V2,hd(V2),hv(V2).
2 ~ :- V2#count{V0,V1:d(V0,V1)}V2,V2#sum{V3,V1:d(V1,V3)}V2,hd(V2),hv(V2).
2 ~ :- V2#count{V0,V1:d(V0,V1)}V2,V2#sum{V3,V1:d(V3,V1)}V2,hd(V2),hv(V2).
2 ~ :- V2#count{V0,V1:d(V1,V0)}V2,V2#sum{V0,V1:d(V0,V1)}V2,hd(V2),hv(V2).
2 ~ :- V2#count{V0,V1:d(V1,V0)}V2,V2#sum{V0,V1:d(V1,V0)}V2,hd(V2),hv(V2).
2 ~ :- V2#count{V0,V1:d(V1,V0)}V2,V2#sum{V0,V3:d(V0,V3)}V2,hd(V2),hv(V2).
2 ~ :- V2#count{V0,V1:d(V1,V0)}V2,V2#sum{V0,V3:d(V3,V0)}V2,hd(V2),hv(V2).
2 ~ :- V2#count{V0,V1:d(V1,V0)}V2,V2#sum{V1,V0:d(V0,V1)}V2,hd(V2),hv(V2).
2 ~ :- V2#count{V0,V1:d(V1,V0)}V2,V2#sum{V1,V0:d(V1,V0)}V2,hd(V2),hv(V2).
2 ~ :- V2#count{V0,V1:d(V1,V0)}V2,V2#sum{V1,V3:d(V1,V3)}V2,hd(V2),hv(V2).
2 ~ :- V2#count{V0,V1:d(V1,V0)}V2,V2#sum{V1,V3:d(V3,V1)}V2,hd(V2),hv(V2).
2 ~ :- V2#count{V0,V1:d(V1,V0)}V2,V2#sum{V3,V0:d(V0,V3)}V2,hd(V2),hv(V2).
2 ~ :- V2#count{V0,V1:d(V1,V0)}V2,V2#sum{V3,V0:d(V3,V0)}V2,hd(V2),hv(V2).
2 ~ :- V2#count{V0,V1:d(V1,V0)}V2,V2#sum{V3,V1:d(V1,V3)}V2,hd(V2),hv(V2).
2 ~ :- V2#count{V0,V1:d(V1,V0)}V2,V2#sum{V3,V1:d(V3,V1)}V2,hd(V2),hv(V2).
2 ~ :- V2#count{V0,V1:d(V0,V1)}V2,V3#sum{V0,V1:d(V0,V1)}V3,V2!=V3,hv(V2),hv(V3).
2 ~ :- V2#count{V0,V1:d(V0,V1)}V2,V3#sum{V0,V1:d(V0,V1)}V3,V3!=V2,hv(V2),hv(V3).
2 ~ :- V2#count{V0,V1:d(V0,V1)}V2,V3#sum{V0,V1:d(V1,V0)}V3,V2!=V3,hv(V2),hv(V3).
2 ~ :- V2#count{V0,V1:d(V0,V1)}V2,V3#sum{V0,V1:d(V1,V0)}V3,V3!=V2,hv(V2),hv(V3).
2 ~ :- V2#count{V0,V1:d(V0,V1)}V2,V3#sum{V1,V0:d(V0,V1)}V3,V2!=V3,hv(V2),hv(V3).
2 ~ :- V2#count{V0,V1:d(V0,V1)}V2,V3#sum{V1,V0:d(V0,V1)}V3,V3!=V2,hv(V2),hv(V3).
2 ~ :- V2#count{V0,V1:d(V0,V1)}V2,V3#sum{V1,V0:d(V1,V0)}V3,V2!=V3,hv(V2),hv(V3).
2 ~ :- V2#count{V0,V1:d(V0,V1)}V2,V3#sum{V1,V0:d(V1,V0)}V3,V3!=V2,hv(V2),hv(V3).
2 ~ :- V2#count{V0,V1:d(V1,V0)}V2,V3#sum{V0,V1:d(V0,V1)}V3,V2!=V3,hv(V2),hv(V3).
2 ~ :- V2#count{V0,V1:d(V1,V0)}V2,V3#sum{V0,V1:d(V0,V1)}V3,V3!=V2,hv(V2),hv(V3).
2 ~ :- V2#count{V0,V1:d(V1,V0)}V2,V3#sum{V0,V1:d(V1,V0)}V3,V2!=V3,hv(V2),hv(V3).
2 ~ :- V2#count{V0,V1:d(V1,V0)}V2,V3#sum{V0,V1:d(V1,V0)}V3,V3!=V2,hv(V2),hv(V3).
2 ~ :- V2#count{V0,V1:d(V1,V0)}V2,V3#sum{V1,V0:d(V0,V1)}V3,V2!=V3,hv(V2),hv(V3).
2 ~ :- V2#count{V0,V1:d(V1,V0)}V2,V3#sum{V1,V0:d(V0,V1)}V3,V3!=V2,hv(V2),hv(V3).
2 ~ :- V2#count{V0,V1:d(V1,V0)}V2,V3#sum{V1,V0:d(V1,V0)}V3,V2!=V3,hv(V2),hv(V3).
2 ~ :- V2#count{V0,V1:d(V1,V0)}V2,V3#sum{V1,V0:d(V1,V0)}V3,V3!=V2,hv(V2),hv(V3).
