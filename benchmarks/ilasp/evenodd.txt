even(0).
prev(1,0).
prev(2,1).
prev(3,2).
prev(4,3).

#pos({odd(1), odd(3), even(2)}, {} ).

#neg({even(3)}, {}).
#neg({even(1)}, {}).
#neg({odd(2)}, {}).


#modeh(1, even(var(v)), (positive)).
#modeh(1, odd(var(v)), (positive)).

#modeb(1, even(var(v)), (positive)). 
#modeb(1, odd(var(v)), (positive)).
#modeb(1, prev(var(v),var(v)), (positive,anti_reflexive)).

% #bias("saturate.").