
king(k).
rook(r).
white(w).
black(b).
one(1).
rank(A):-
    cell(_,(A,_),_,_).
file(A):-
    cell(_,(_,A),_,_).

distance((X1,Y1),(X2,Y2),D1) :-
    rank(X1),
    rank(X2),
    file(Y1),
    file(Y2),
    |X1-X2| = D1,
    |Y1-Y2| = D2,
    D1 >= D2.

distance((X1,Y1),(X2,Y2),D2) :-
    rank(X1),
    rank(X2),
    file(Y1),
    file(Y2),
    |X1-X2| = D1,
    |Y1-Y2| = D2,
    D1 <= D2.

cell(0,(5, 3), w, r).
cell(0,(3, 4), b, k).
cell(0,(5, 4), w, k).
cell(1,(3, 3), w, r).
cell(1,(2, 1), b, k).
cell(1,(3, 2), w, k).
cell(2,(1, 3), w, r).
cell(2,(7, 2), b, k).
cell(2,(2, 2), w, k).
cell(3,(8, 2), w, r).
cell(3,(8, 1), b, k).
cell(3,(7, 1), w, k).
cell(4,(1, 5), w, r).
cell(4,(7, 2), b, k).
cell(4,(0, 5), w, k).
cell(5,(7, 6), w, r).
cell(5,(1, 8), b, k).
cell(5,(8, 5), w, k).
cell(6,(1, 6), w, r).
cell(6,(6, 2), b, k).
cell(6,(2, 6), w, k).
cell(7,(5, 6), w, r).
cell(7,(3, 6), b, k).
cell(7,(4, 7), w, k).
cell(8,(5, 6), w, r).
cell(8,(8, 2), b, k).
cell(8,(4, 6), w, k).
cell(9,(8, 7), w, r).
cell(9,(6, 3), b, k).
cell(9,(7, 6), w, k).
cell(10,(8, 8), w, r).
cell(10,(7, 8), b, k).
cell(10,(8, 7), w, k).
cell(11,(5, 7), w, r).
cell(11,(5, 3), b, k).
cell(11,(6, 8), w, k).
cell(12,(8, 6), w, r).
cell(12,(4, 2), b, k).
cell(12,(7, 6), w, k).
cell(13,(5, 5), w, r).
cell(13,(1, 3), b, k).
cell(13,(5, 4), w, k).
cell(14,(2, 3), w, r).
cell(14,(8, 3), b, k).
cell(14,(2, 2), w, k).
cell(15,(8, 5), w, r).
cell(15,(5, 6), b, k).
cell(15,(7, 4), w, k).
cell(16,(4, 3), w, r).
cell(16,(8, 3), b, k).
cell(16,(4, 4), w, k).
cell(17,(5, 8), w, r).
cell(17,(3, 4), b, k).
cell(17,(4, 8), w, k).
cell(18,(1, 2), w, r).
cell(18,(3, 8), b, k).
cell(18,(2, 3), w, k).
cell(19,(8, 1), w, r).
cell(19,(2, 6), b, k).
cell(19,(7, 1), w, k).
cell(20,(3, 4), w, r).
cell(20,(6, 3), b, k).
cell(20,(2, 5), w, k).
cell(21,(5, 1), w, r).
cell(21,(4, 7), b, k).
cell(21,(5, 2), w, k).
cell(22,(1, 2), w, r).
cell(22,(2, 4), b, k).
cell(22,(2, 1), w, k).
cell(23,(1, 5), w, r).
cell(23,(2, 4), b, k).
cell(23,(2, 5), w, k).
cell(24,(2, 4), w, r).
cell(24,(1, 1), b, k).
cell(24,(1, 4), w, k).
cell(25,(5, 7), b, r).
cell(25,(1, 5), w, k).
cell(25,(7, 4), b, r).
cell(26,(6, 4), b, r).
cell(26,(7, 8), w, k).
cell(26,(3, 4), b, r).
cell(27,(2, 2), b, k).
cell(27,(6, 4), b, k).
cell(27,(7, 5), w, r).
cell(28,(8, 1), w, k).
cell(28,(1, 2), w, r).
cell(28,(6, 1), w, k).
cell(29,(2, 6), w, r).
cell(29,(6, 6), b, k).
cell(29,(1, 5), b, r).
cell(30,(6, 6), w, r).
cell(30,(6, 7), b, k).
cell(30,(8, 4), b, k).
cell(31,(3, 8), w, r).
cell(31,(3, 1), w, k).
cell(31,(6, 2), b, k).
cell(32,(3, 7), b, r).
cell(32,(3, 5), b, r).
cell(32,(6, 4), b, r).
cell(33,(4, 4), b, k).
cell(33,(1, 3), w, r).
cell(33,(7, 8), w, k).
cell(34,(7, 7), b, k).
cell(34,(5, 2), w, k).
cell(34,(3, 8), b, r).
cell(35,(4, 3), b, k).
cell(35,(2, 1), w, r).
cell(35,(4, 4), w, k).
cell(36,(1, 7), w, r).
cell(36,(8, 4), w, r).
cell(36,(8, 6), w, k).
cell(37,(7, 1), w, k).
cell(37,(1, 6), w, k).
cell(37,(4, 2), w, k).
cell(38,(7, 8), w, r).
cell(38,(2, 8), b, r).
cell(38,(4, 3), w, r).
cell(39,(5, 5), w, r).
cell(39,(2, 8), w, k).
cell(39,(4, 3), w, r).
cell(40,(4, 3), w, r).
cell(40,(6, 5), b, k).
cell(40,(1, 1), b, r).
cell(41,(5, 2), b, r).
cell(41,(3, 8), w, r).
cell(41,(1, 5), w, r).
cell(42,(7, 8), b, r).
cell(42,(6, 1), b, r).
cell(42,(4, 6), b, k).
cell(43,(7, 5), b, k).
cell(43,(7, 6), w, r).
cell(43,(1, 6), w, k).
cell(44,(3, 2), w, r).
cell(44,(5, 7), w, r).
cell(44,(7, 4), b, k).
cell(45,(6, 3), b, r).
cell(45,(7, 2), w, r).
cell(45,(8, 2), b, k).
cell(46,(4, 1), w, r).
cell(46,(3, 6), b, k).
cell(46,(5, 8), b, k).
cell(47,(8, 4), b, r).
cell(47,(1, 8), b, k).
cell(47,(1, 2), b, r).
cell(48,(3, 1), b, k).
cell(48,(2, 1), b, k).
cell(48,(1, 7), w, r).
cell(49,(3, 3), w, k).
cell(49,(5, 4), w, r).
cell(49,(5, 2), b, r).