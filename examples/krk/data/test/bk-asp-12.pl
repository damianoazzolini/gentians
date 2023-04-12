
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

cell(0,(5, 7), w, r).
cell(0,(7, 7), b, k).
cell(0,(4, 6), w, k).
cell(1,(3, 1), w, r).
cell(1,(3, 7), b, k).
cell(1,(2, 0), w, k).
cell(2,(2, 4), w, r).
cell(2,(8, 4), b, k).
cell(2,(3, 3), w, k).
cell(3,(6, 2), w, r).
cell(3,(8, 1), b, k).
cell(3,(7, 2), w, k).
cell(4,(2, 6), w, r).
cell(4,(7, 5), b, k).
cell(4,(2, 7), w, k).
cell(5,(6, 5), w, r).
cell(5,(1, 4), b, k).
cell(5,(6, 6), w, k).
cell(6,(6, 3), w, r).
cell(6,(5, 2), b, k).
cell(6,(7, 3), w, k).
cell(7,(5, 4), w, r).
cell(7,(2, 4), b, k).
cell(7,(5, 5), w, k).
cell(8,(3, 5), w, r).
cell(8,(5, 8), b, k).
cell(8,(2, 4), w, k).
cell(9,(8, 7), w, r).
cell(9,(1, 5), b, k).
cell(9,(8, 6), w, k).
cell(10,(1, 3), w, r).
cell(10,(2, 3), b, k).
cell(10,(0, 3), w, k).
cell(11,(3, 1), w, r).
cell(11,(3, 7), b, k).
cell(11,(3, 2), w, k).
cell(12,(5, 1), w, r).
cell(12,(8, 7), b, k).
cell(12,(4, 2), w, k).
cell(13,(7, 2), w, r).
cell(13,(6, 3), b, k).
cell(13,(8, 2), w, k).
cell(14,(8, 5), w, r).
cell(14,(8, 1), b, k).
cell(14,(8, 6), w, k).
cell(15,(1, 2), w, r).
cell(15,(6, 3), b, k).
cell(15,(2, 2), w, k).
cell(16,(2, 6), w, r).
cell(16,(5, 8), b, k).
cell(16,(3, 6), w, k).
cell(17,(4, 4), w, r).
cell(17,(6, 6), b, k).
cell(17,(4, 3), w, k).
cell(18,(1, 3), w, r).
cell(18,(3, 5), b, k).
cell(18,(0, 3), w, k).
cell(19,(6, 7), w, r).
cell(19,(3, 8), b, k).
cell(19,(5, 7), w, k).
cell(20,(3, 3), w, r).
cell(20,(1, 5), b, k).
cell(20,(3, 4), w, k).
cell(21,(8, 8), w, r).
cell(21,(6, 2), b, k).
cell(21,(8, 7), w, k).
cell(22,(6, 6), w, r).
cell(22,(7, 6), b, k).
cell(22,(7, 5), w, k).
cell(23,(2, 5), w, r).
cell(23,(1, 2), b, k).
cell(23,(3, 6), w, k).
cell(24,(7, 6), w, r).
cell(24,(6, 3), b, k).
cell(24,(8, 6), w, k).
cell(25,(8, 5), w, k).
cell(25,(8, 2), b, k).
cell(25,(7, 1), b, r).
cell(26,(8, 3), w, k).
cell(26,(2, 5), b, k).
cell(26,(1, 3), b, k).
cell(27,(7, 2), w, k).
cell(27,(5, 5), w, r).
cell(27,(2, 7), w, k).
cell(28,(4, 2), w, r).
cell(28,(6, 7), b, k).
cell(28,(3, 8), w, k).
cell(29,(2, 1), b, r).
cell(29,(7, 7), w, r).
cell(29,(6, 6), w, r).
cell(30,(3, 2), w, k).
cell(30,(3, 1), b, k).
cell(30,(2, 7), b, k).
cell(31,(1, 2), b, k).
cell(31,(3, 1), w, r).
cell(31,(8, 4), w, k).
cell(32,(4, 4), b, r).
cell(32,(7, 2), w, r).
cell(32,(3, 3), b, r).
cell(33,(8, 2), w, r).
cell(33,(7, 8), w, k).
cell(33,(5, 6), w, r).
cell(34,(4, 7), w, r).
cell(34,(3, 3), b, k).
cell(34,(8, 7), b, r).
cell(35,(1, 2), w, r).
cell(35,(1, 7), b, r).
cell(35,(7, 8), w, r).
cell(36,(4, 1), w, r).
cell(36,(5, 6), w, k).
cell(36,(7, 2), b, k).
cell(37,(6, 5), w, r).
cell(37,(4, 4), b, r).
cell(37,(7, 1), b, k).
cell(38,(1, 4), b, k).
cell(38,(8, 8), b, k).
cell(38,(2, 5), b, k).
cell(39,(8, 5), b, r).
cell(39,(4, 2), w, k).
cell(39,(6, 6), b, k).
cell(40,(1, 2), b, k).
cell(40,(7, 6), b, k).
cell(40,(2, 4), b, r).
cell(41,(6, 8), w, r).
cell(41,(3, 1), w, k).
cell(41,(2, 5), w, k).
cell(42,(8, 7), w, r).
cell(42,(8, 3), w, k).
cell(42,(2, 8), w, k).
cell(43,(8, 8), w, k).
cell(43,(8, 3), b, r).
cell(43,(6, 1), b, r).
cell(44,(7, 3), w, k).
cell(44,(6, 7), b, k).
cell(44,(7, 2), b, r).
cell(45,(2, 4), b, k).
cell(45,(2, 1), w, r).
cell(45,(7, 4), b, r).
cell(46,(2, 4), w, r).
cell(46,(4, 7), w, k).
cell(46,(7, 2), w, k).
cell(47,(2, 4), w, r).
cell(47,(7, 8), b, r).
cell(47,(3, 3), b, r).
cell(48,(2, 8), b, r).
cell(48,(6, 5), w, r).
cell(48,(4, 8), b, r).
cell(49,(5, 8), w, r).
cell(49,(4, 4), w, k).
cell(49,(2, 8), w, r).