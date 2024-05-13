diff(A,B):- v(A), v(B), A != B.

v(1..9).
e(1,2).
e(1,5).
e(1,9).
e(3,1).
e(3,4).
e(3,8).
e(5,4).
e(6,3).
e(6,7).
e(2,5).
e(4,7).
e(7,1).
e(8,2).
e(9,5).
e(9,6).
3 {in(X) : v(X)} 3.
v(X) :- e(X,Y).
v(Y) :- e(X,Y).

ne(X,Y):- not e(X,Y), v(X), v(Y).

#pos({in(1), in(2), in(5)}, {} ).
#pos({in(1), in(9), in(5)}, {} ).

#neg({in(3)}, {}).
#neg({in(4)}, {}).

#modeb(2, n(var(t)), (positive)). 
#modeb(2, ne(var(t),var(t)), (positive,anti_reflexive)).
#modeb(1, diff(var(t),var(t)), (positive,anti_reflexive)).
#modeb(2, in(var(t)), (positive)).

% #bias("saturate.").
