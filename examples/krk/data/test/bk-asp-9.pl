
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

cell(0,(3, 1), w, r).
cell(0,(2, 2), b, k).
cell(0,(3, 2), w, k).
cell(1,(2, 1), w, r).
cell(1,(3, 8), b, k).
cell(1,(2, 2), w, k).
cell(2,(5, 5), w, r).
cell(2,(2, 6), b, k).
cell(2,(4, 6), w, k).
cell(3,(4, 2), w, r).
cell(3,(3, 4), b, k).
cell(3,(3, 2), w, k).
cell(4,(7, 5), w, r).
cell(4,(3, 7), b, k).
cell(4,(8, 4), w, k).
cell(5,(7, 7), w, r).
cell(5,(5, 5), b, k).
cell(5,(6, 7), w, k).
cell(6,(1, 5), w, r).
cell(6,(1, 8), b, k).
cell(6,(0, 5), w, k).
cell(7,(2, 2), w, r).
cell(7,(4, 5), b, k).
cell(7,(3, 3), w, k).
cell(8,(1, 1), w, r).
cell(8,(5, 3), b, k).
cell(8,(2, 2), w, k).
cell(9,(2, 2), w, r).
cell(9,(6, 4), b, k).
cell(9,(2, 3), w, k).
cell(10,(8, 6), w, r).
cell(10,(2, 4), b, k).
cell(10,(8, 7), w, k).
cell(11,(1, 1), w, r).
cell(11,(1, 7), b, k).
cell(11,(2, 1), w, k).
cell(12,(8, 3), w, r).
cell(12,(7, 2), b, k).
cell(12,(7, 4), w, k).
cell(13,(3, 3), w, r).
cell(13,(3, 2), b, k).
cell(13,(2, 3), w, k).
cell(14,(5, 8), w, r).
cell(14,(5, 3), b, k).
cell(14,(4, 8), w, k).
cell(15,(4, 3), w, r).
cell(15,(1, 2), b, k).
cell(15,(3, 4), w, k).
cell(16,(6, 8), w, r).
cell(16,(6, 5), b, k).
cell(16,(7, 8), w, k).
cell(17,(8, 7), w, r).
cell(17,(3, 8), b, k).
cell(17,(7, 7), w, k).
cell(18,(3, 6), w, r).
cell(18,(7, 1), b, k).
cell(18,(2, 7), w, k).
cell(19,(6, 2), w, r).
cell(19,(3, 1), b, k).
cell(19,(5, 3), w, k).
cell(20,(4, 5), w, r).
cell(20,(8, 1), b, k).
cell(20,(4, 6), w, k).
cell(21,(7, 7), w, r).
cell(21,(3, 3), b, k).
cell(21,(7, 6), w, k).
cell(22,(3, 5), w, r).
cell(22,(8, 4), b, k).
cell(22,(2, 5), w, k).
cell(23,(5, 7), w, r).
cell(23,(4, 5), b, k).
cell(23,(5, 6), w, k).
cell(24,(2, 2), w, r).
cell(24,(8, 4), b, k).
cell(24,(1, 1), w, k).
cell(25,(3, 2), b, r).
cell(25,(2, 4), w, k).
cell(25,(8, 1), w, k).
cell(26,(1, 6), b, k).
cell(26,(3, 1), w, k).
cell(26,(6, 4), w, k).
cell(27,(8, 1), b, r).
cell(27,(2, 1), w, r).
cell(27,(1, 8), w, k).
cell(28,(3, 2), b, r).
cell(28,(1, 1), w, r).
cell(28,(8, 5), w, k).
cell(29,(7, 8), w, r).
cell(29,(6, 4), w, k).
cell(29,(3, 7), b, k).
cell(30,(3, 8), w, r).
cell(30,(7, 6), w, k).
cell(30,(7, 3), w, r).
cell(31,(5, 5), b, r).
cell(31,(4, 3), b, k).
cell(31,(1, 3), w, k).
cell(32,(1, 4), w, r).
cell(32,(7, 3), b, r).
cell(32,(6, 1), b, r).
cell(33,(4, 5), b, k).
cell(33,(2, 3), b, k).
cell(33,(4, 6), w, k).
cell(34,(6, 5), b, r).
cell(34,(5, 6), b, k).
cell(34,(8, 8), w, r).
cell(35,(3, 6), w, r).
cell(35,(3, 5), b, r).
cell(35,(5, 6), b, r).
cell(36,(6, 2), w, r).
cell(36,(4, 2), w, k).
cell(36,(8, 6), b, k).
cell(37,(4, 6), w, k).
cell(37,(4, 4), b, k).
cell(37,(7, 7), w, k).
cell(38,(7, 6), b, r).
cell(38,(5, 5), b, r).
cell(38,(6, 4), b, r).
cell(39,(3, 4), b, k).
cell(39,(6, 5), w, r).
cell(39,(2, 1), b, k).
cell(40,(1, 3), b, k).
cell(40,(6, 2), b, k).
cell(40,(1, 8), w, r).
cell(41,(2, 6), b, k).
cell(41,(2, 4), w, r).
cell(41,(7, 7), w, r).
cell(42,(6, 4), w, r).
cell(42,(1, 2), b, r).
cell(42,(8, 1), b, k).
cell(43,(5, 3), w, r).
cell(43,(8, 5), b, k).
cell(43,(5, 2), w, r).
cell(44,(8, 5), b, k).
cell(44,(7, 3), b, k).
cell(44,(5, 5), b, k).
cell(45,(8, 5), b, r).
cell(45,(4, 7), w, k).
cell(45,(1, 3), b, k).
cell(46,(5, 6), w, k).
cell(46,(8, 2), b, r).
cell(46,(8, 8), w, k).
cell(47,(4, 3), w, r).
cell(47,(2, 2), b, k).
cell(47,(3, 6), w, r).
cell(48,(8, 1), b, r).
cell(48,(3, 6), b, r).
cell(48,(4, 4), b, r).
cell(49,(4, 8), b, r).
cell(49,(2, 6), b, r).
cell(49,(6, 5), w, r).