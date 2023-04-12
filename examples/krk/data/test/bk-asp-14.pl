
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

cell(0,(1, 6), w, r).
cell(0,(8, 6), b, k).
cell(0,(1, 5), w, k).
cell(1,(7, 1), w, r).
cell(1,(4, 1), b, k).
cell(1,(6, 2), w, k).
cell(2,(1, 5), w, r).
cell(2,(2, 5), b, k).
cell(2,(0, 5), w, k).
cell(3,(4, 7), w, r).
cell(3,(6, 5), b, k).
cell(3,(4, 6), w, k).
cell(4,(6, 7), w, r).
cell(4,(7, 3), b, k).
cell(4,(7, 7), w, k).
cell(5,(5, 6), w, r).
cell(5,(8, 6), b, k).
cell(5,(4, 5), w, k).
cell(6,(8, 5), w, r).
cell(6,(5, 7), b, k).
cell(6,(7, 6), w, k).
cell(7,(3, 4), w, r).
cell(7,(4, 1), b, k).
cell(7,(2, 4), w, k).
cell(8,(8, 1), w, r).
cell(8,(2, 7), b, k).
cell(8,(8, 0), w, k).
cell(9,(7, 7), w, r).
cell(9,(1, 5), b, k).
cell(9,(7, 8), w, k).
cell(10,(8, 3), w, r).
cell(10,(6, 5), b, k).
cell(10,(7, 2), w, k).
cell(11,(7, 5), w, r).
cell(11,(1, 2), b, k).
cell(11,(6, 5), w, k).
cell(12,(6, 7), w, r).
cell(12,(7, 5), b, k).
cell(12,(7, 6), w, k).
cell(13,(5, 6), w, r).
cell(13,(8, 3), b, k).
cell(13,(5, 7), w, k).
cell(14,(3, 8), w, r).
cell(14,(8, 2), b, k).
cell(14,(4, 7), w, k).
cell(15,(2, 7), w, r).
cell(15,(4, 1), b, k).
cell(15,(3, 7), w, k).
cell(16,(5, 4), w, r).
cell(16,(6, 5), b, k).
cell(16,(5, 3), w, k).
cell(17,(1, 3), w, r).
cell(17,(1, 5), b, k).
cell(17,(0, 4), w, k).
cell(18,(1, 6), w, r).
cell(18,(4, 1), b, k).
cell(18,(0, 7), w, k).
cell(19,(2, 7), w, r).
cell(19,(1, 7), b, k).
cell(19,(1, 8), w, k).
cell(20,(8, 2), w, r).
cell(20,(5, 4), b, k).
cell(20,(8, 1), w, k).
cell(21,(5, 3), w, r).
cell(21,(3, 8), b, k).
cell(21,(4, 2), w, k).
cell(22,(2, 4), w, r).
cell(22,(3, 5), b, k).
cell(22,(1, 4), w, k).
cell(23,(7, 5), w, r).
cell(23,(5, 5), b, k).
cell(23,(7, 4), w, k).
cell(24,(4, 4), w, r).
cell(24,(8, 7), b, k).
cell(24,(3, 5), w, k).
cell(25,(6, 6), w, r).
cell(25,(8, 5), w, r).
cell(25,(1, 2), b, k).
cell(26,(5, 2), b, k).
cell(26,(4, 2), b, r).
cell(26,(1, 5), b, k).
cell(27,(4, 8), w, r).
cell(27,(2, 5), b, r).
cell(27,(4, 6), w, r).
cell(28,(8, 5), b, k).
cell(28,(2, 1), w, r).
cell(28,(6, 8), w, r).
cell(29,(4, 7), b, k).
cell(29,(5, 2), w, k).
cell(29,(4, 1), b, r).
cell(30,(8, 7), b, k).
cell(30,(2, 2), b, r).
cell(30,(6, 5), w, r).
cell(31,(1, 1), b, r).
cell(31,(4, 5), b, r).
cell(31,(1, 4), w, r).
cell(32,(6, 6), w, r).
cell(32,(7, 8), w, r).
cell(32,(2, 7), b, k).
cell(33,(1, 4), w, k).
cell(33,(4, 7), b, r).
cell(33,(5, 7), w, k).
cell(34,(2, 3), w, k).
cell(34,(5, 3), w, r).
cell(34,(4, 5), b, r).
cell(35,(5, 6), b, k).
cell(35,(7, 8), w, k).
cell(35,(7, 1), w, r).
cell(36,(7, 4), w, r).
cell(36,(5, 3), b, k).
cell(36,(4, 6), w, k).
cell(37,(3, 5), w, k).
cell(37,(4, 6), w, k).
cell(37,(7, 6), w, r).
cell(38,(3, 2), b, k).
cell(38,(1, 2), w, k).
cell(38,(4, 1), w, k).
cell(39,(2, 1), b, k).
cell(39,(1, 6), b, r).
cell(39,(2, 7), b, r).
cell(40,(6, 1), b, k).
cell(40,(6, 2), b, k).
cell(40,(2, 2), b, k).
cell(41,(5, 2), w, k).
cell(41,(7, 3), w, r).
cell(41,(2, 4), b, r).
cell(42,(5, 6), b, r).
cell(42,(4, 1), w, r).
cell(42,(2, 1), b, k).
cell(43,(3, 8), w, r).
cell(43,(4, 4), w, k).
cell(43,(8, 5), b, r).
cell(44,(7, 3), w, r).
cell(44,(8, 1), w, r).
cell(44,(7, 7), b, k).
cell(45,(3, 6), b, k).
cell(45,(5, 1), b, r).
cell(45,(5, 7), w, r).
cell(46,(4, 2), w, k).
cell(46,(3, 5), b, k).
cell(46,(1, 4), b, r).
cell(47,(6, 8), b, r).
cell(47,(4, 7), w, k).
cell(47,(7, 8), w, r).
cell(48,(6, 4), w, k).
cell(48,(8, 2), w, k).
cell(48,(7, 6), w, k).
cell(49,(4, 8), b, k).
cell(49,(2, 8), w, k).
cell(49,(6, 2), w, k).