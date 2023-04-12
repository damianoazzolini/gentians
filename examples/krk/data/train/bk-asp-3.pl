
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

cell(0,(2, 4), w, r).
cell(0,(2, 6), b, k).
cell(0,(1, 5), w, k).
cell(1,(3, 8), w, r).
cell(1,(1, 4), b, k).
cell(1,(2, 8), w, k).
cell(2,(8, 2), w, r).
cell(2,(6, 6), b, k).
cell(2,(8, 3), w, k).
cell(3,(4, 8), w, r).
cell(3,(2, 5), b, k).
cell(3,(5, 7), w, k).
cell(4,(3, 6), w, r).
cell(4,(8, 1), b, k).
cell(4,(3, 5), w, k).
cell(5,(6, 5), w, r).
cell(5,(3, 4), b, k).
cell(5,(7, 5), w, k).
cell(6,(1, 5), w, r).
cell(6,(2, 8), b, k).
cell(6,(2, 6), w, k).
cell(7,(1, 3), w, r).
cell(7,(6, 2), b, k).
cell(7,(2, 2), w, k).
cell(8,(3, 5), w, r).
cell(8,(6, 7), b, k).
cell(8,(2, 5), w, k).
cell(9,(1, 1), w, r).
cell(9,(7, 2), b, k).
cell(9,(2, 0), w, k).
cell(10,(2, 4), w, r).
cell(10,(3, 3), b, k).
cell(10,(1, 5), w, k).
cell(11,(2, 7), w, r).
cell(11,(7, 5), b, k).
cell(11,(3, 7), w, k).
cell(12,(3, 4), w, r).
cell(12,(1, 8), b, k).
cell(12,(2, 3), w, k).
cell(13,(8, 7), w, r).
cell(13,(2, 6), b, k).
cell(13,(7, 7), w, k).
cell(14,(5, 1), w, r).
cell(14,(8, 5), b, k).
cell(14,(4, 2), w, k).
cell(15,(3, 7), w, r).
cell(15,(8, 5), b, k).
cell(15,(2, 8), w, k).
cell(16,(7, 8), w, r).
cell(16,(4, 4), b, k).
cell(16,(6, 7), w, k).
cell(17,(8, 8), w, r).
cell(17,(6, 5), b, k).
cell(17,(7, 8), w, k).
cell(18,(3, 2), w, r).
cell(18,(2, 1), b, k).
cell(18,(4, 1), w, k).
cell(19,(3, 2), w, r).
cell(19,(1, 4), b, k).
cell(19,(3, 3), w, k).
cell(20,(6, 6), w, r).
cell(20,(3, 5), b, k).
cell(20,(5, 7), w, k).
cell(21,(8, 3), w, r).
cell(21,(1, 3), b, k).
cell(21,(8, 2), w, k).
cell(22,(2, 8), w, r).
cell(22,(2, 6), b, k).
cell(22,(2, 7), w, k).
cell(23,(6, 1), w, r).
cell(23,(2, 1), b, k).
cell(23,(6, 2), w, k).
cell(24,(7, 6), w, r).
cell(24,(5, 7), b, k).
cell(24,(8, 5), w, k).
cell(25,(6, 6), w, r).
cell(25,(3, 4), b, k).
cell(25,(4, 5), b, k).
cell(26,(1, 8), b, k).
cell(26,(7, 8), w, k).
cell(26,(4, 1), w, r).
cell(27,(7, 1), b, k).
cell(27,(1, 8), w, k).
cell(27,(3, 3), w, k).
cell(28,(2, 1), w, k).
cell(28,(6, 3), b, k).
cell(28,(4, 6), b, k).
cell(29,(7, 1), b, k).
cell(29,(1, 7), b, r).
cell(29,(8, 3), b, r).
cell(30,(6, 4), b, r).
cell(30,(5, 4), b, k).
cell(30,(1, 8), w, r).
cell(31,(8, 3), b, k).
cell(31,(2, 6), b, k).
cell(31,(6, 3), b, r).
cell(32,(1, 4), b, r).
cell(32,(7, 6), b, r).
cell(32,(1, 7), w, k).
cell(33,(3, 7), b, k).
cell(33,(3, 4), b, k).
cell(33,(8, 2), b, r).
cell(34,(1, 5), w, k).
cell(34,(5, 8), w, k).
cell(34,(3, 1), b, k).
cell(35,(8, 3), w, r).
cell(35,(5, 3), b, r).
cell(35,(6, 3), b, r).
cell(36,(7, 5), b, k).
cell(36,(8, 1), w, k).
cell(36,(6, 7), b, r).
cell(37,(5, 6), w, k).
cell(37,(5, 2), w, k).
cell(37,(1, 8), w, k).
cell(38,(6, 4), b, k).
cell(38,(5, 8), b, r).
cell(38,(2, 4), w, r).
cell(39,(2, 4), b, k).
cell(39,(2, 1), b, k).
cell(39,(4, 8), b, k).
cell(40,(8, 4), w, r).
cell(40,(7, 6), w, r).
cell(40,(1, 1), b, k).
cell(41,(4, 1), b, k).
cell(41,(2, 4), b, r).
cell(41,(6, 3), w, k).
cell(42,(7, 7), b, k).
cell(42,(8, 2), b, k).
cell(42,(1, 2), w, r).
cell(43,(2, 1), w, k).
cell(43,(7, 8), w, k).
cell(43,(6, 2), w, r).
cell(44,(5, 8), w, k).
cell(44,(5, 1), b, k).
cell(44,(6, 6), b, r).
cell(45,(1, 8), w, k).
cell(45,(3, 8), w, r).
cell(45,(7, 3), w, k).
cell(46,(2, 6), w, r).
cell(46,(2, 3), w, k).
cell(46,(7, 6), b, k).
cell(47,(1, 2), w, k).
cell(47,(7, 1), b, r).
cell(47,(7, 3), w, k).
cell(48,(1, 6), b, r).
cell(48,(6, 3), b, r).
cell(48,(7, 5), w, r).
cell(49,(2, 4), w, r).
cell(49,(4, 2), b, r).
cell(49,(5, 5), w, r).