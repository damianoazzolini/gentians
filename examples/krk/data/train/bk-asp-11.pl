
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

cell(0,(8, 2), w, r).
cell(0,(1, 5), b, k).
cell(0,(8, 3), w, k).
cell(1,(1, 3), w, r).
cell(1,(6, 6), b, k).
cell(1,(0, 2), w, k).
cell(2,(1, 2), w, r).
cell(2,(6, 4), b, k).
cell(2,(2, 1), w, k).
cell(3,(1, 7), w, r).
cell(3,(5, 3), b, k).
cell(3,(0, 7), w, k).
cell(4,(1, 7), w, r).
cell(4,(3, 8), b, k).
cell(4,(0, 6), w, k).
cell(5,(1, 5), w, r).
cell(5,(4, 6), b, k).
cell(5,(0, 5), w, k).
cell(6,(2, 7), w, r).
cell(6,(5, 2), b, k).
cell(6,(1, 7), w, k).
cell(7,(8, 8), w, r).
cell(7,(5, 3), b, k).
cell(7,(7, 8), w, k).
cell(8,(8, 3), w, r).
cell(8,(3, 1), b, k).
cell(8,(7, 3), w, k).
cell(9,(5, 7), w, r).
cell(9,(3, 8), b, k).
cell(9,(6, 7), w, k).
cell(10,(8, 4), w, r).
cell(10,(5, 4), b, k).
cell(10,(7, 3), w, k).
cell(11,(6, 8), w, r).
cell(11,(4, 8), b, k).
cell(11,(7, 7), w, k).
cell(12,(8, 1), w, r).
cell(12,(3, 5), b, k).
cell(12,(8, 2), w, k).
cell(13,(2, 5), w, r).
cell(13,(3, 3), b, k).
cell(13,(2, 4), w, k).
cell(14,(2, 7), w, r).
cell(14,(8, 2), b, k).
cell(14,(1, 8), w, k).
cell(15,(7, 2), w, r).
cell(15,(4, 2), b, k).
cell(15,(6, 1), w, k).
cell(16,(8, 5), w, r).
cell(16,(2, 8), b, k).
cell(16,(7, 4), w, k).
cell(17,(8, 7), w, r).
cell(17,(3, 2), b, k).
cell(17,(7, 8), w, k).
cell(18,(7, 3), w, r).
cell(18,(1, 4), b, k).
cell(18,(8, 2), w, k).
cell(19,(7, 3), w, r).
cell(19,(4, 8), b, k).
cell(19,(8, 3), w, k).
cell(20,(7, 5), w, r).
cell(20,(8, 1), b, k).
cell(20,(8, 4), w, k).
cell(21,(7, 7), w, r).
cell(21,(6, 1), b, k).
cell(21,(8, 7), w, k).
cell(22,(1, 8), w, r).
cell(22,(4, 6), b, k).
cell(22,(1, 7), w, k).
cell(23,(4, 1), w, r).
cell(23,(1, 3), b, k).
cell(23,(4, 0), w, k).
cell(24,(2, 5), w, r).
cell(24,(2, 8), b, k).
cell(24,(3, 4), w, k).
cell(25,(8, 6), w, r).
cell(25,(8, 7), b, r).
cell(25,(5, 7), w, k).
cell(26,(3, 6), b, k).
cell(26,(6, 3), b, r).
cell(26,(1, 2), w, k).
cell(27,(5, 3), w, k).
cell(27,(3, 2), b, k).
cell(27,(2, 2), w, r).
cell(28,(4, 3), w, r).
cell(28,(3, 5), b, k).
cell(28,(2, 3), w, r).
cell(29,(4, 8), b, r).
cell(29,(3, 6), w, k).
cell(29,(1, 7), w, r).
cell(30,(5, 8), b, r).
cell(30,(2, 2), b, k).
cell(30,(4, 4), b, k).
cell(31,(8, 5), b, r).
cell(31,(1, 1), w, k).
cell(31,(4, 3), w, k).
cell(32,(7, 8), w, r).
cell(32,(7, 3), w, r).
cell(32,(1, 5), b, k).
cell(33,(4, 3), w, k).
cell(33,(8, 1), b, r).
cell(33,(6, 2), b, k).
cell(34,(4, 5), b, r).
cell(34,(5, 7), w, r).
cell(34,(4, 6), b, r).
cell(35,(4, 1), b, k).
cell(35,(2, 7), b, k).
cell(35,(6, 3), w, r).
cell(36,(1, 5), b, k).
cell(36,(7, 5), b, r).
cell(36,(8, 3), b, k).
cell(37,(6, 2), w, k).
cell(37,(6, 7), w, r).
cell(37,(1, 5), w, r).
cell(38,(3, 1), w, k).
cell(38,(7, 1), w, k).
cell(38,(8, 7), w, r).
cell(39,(1, 1), w, k).
cell(39,(8, 8), b, r).
cell(39,(2, 7), b, r).
cell(40,(7, 6), w, r).
cell(40,(2, 2), b, r).
cell(40,(3, 5), w, r).
cell(41,(8, 4), w, r).
cell(41,(7, 7), w, k).
cell(41,(6, 4), w, k).
cell(42,(8, 3), w, r).
cell(42,(3, 7), b, k).
cell(42,(3, 4), w, r).
cell(43,(8, 7), w, r).
cell(43,(7, 1), w, r).
cell(43,(7, 8), b, k).
cell(44,(5, 4), b, r).
cell(44,(6, 3), b, r).
cell(44,(2, 4), w, k).
cell(45,(2, 3), b, k).
cell(45,(3, 7), b, r).
cell(45,(1, 4), w, r).
cell(46,(2, 2), b, r).
cell(46,(7, 2), w, k).
cell(46,(7, 4), b, k).
cell(47,(2, 4), b, k).
cell(47,(7, 4), w, k).
cell(47,(6, 5), b, r).
cell(48,(4, 6), w, k).
cell(48,(8, 7), w, r).
cell(48,(8, 8), b, r).
cell(49,(4, 6), b, k).
cell(49,(3, 5), w, r).
cell(49,(6, 3), w, k).