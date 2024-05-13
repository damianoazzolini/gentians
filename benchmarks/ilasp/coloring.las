edge(1, 2).
edge(1, 3).
edge(2, 5).
edge(2, 6).
edge(3, 4).
edge(4, 5).
edge(5, 6).
node(1..6).
e(X,Y) :- edge(X,Y).
e(Y,X) :- edge(Y,X).
node(1..6).

#pos({red(1), blue(2), blue(3), red(4), green(5), red(6)}, {}).
#pos({red(1), blue(2), green(3), blue(4), green(5), red(6)}, {}).
#pos({red(1), blue(2), green(3), red(4), green(5), red(6)}, {}).
#pos({green(1), blue(2), red(3), blue(4), green(5), red(6)}, {}).
#pos({green(1), blue(2), blue(3), red(4), green(5), red(6)}, {}).
#pos({red(1), blue(2), green(3), blue(4), red(5), green(6)}, {}).

#neg({red(1), red(2)}, {}).
#neg({red(1), red(3)}, {}).
#neg({blue(1), blue(2)}, {}).
#neg({green(3), green(4)}, {}).


#modeha(1, red(var(t)), (positive)).
#modeha(1, green(var(t)), (positive)).
#modeha(1, blue(var(t)), (positive)).


#modeb(1, e(var(t), var(t)), (positive)). 
#modeb(2, red(var(t)), (positive)). 
#modeb(2, green(var(t)), (positive)).
#modeb(2, blue(var(t)), (positive)).
#modeb(1, node(var(t)), (positive)).

#minhl(3).
#maxhl(3).

% #bias("saturate.").

% #disallow_multiple_head_variables