mother(i,a).
mother(c,f).
mother(c,g).
mother(f,h).
father(a,b).
father(a,c).
father(b,d).
father(b,e).

#pos( 
    {target(i,b), target(i,c), target(a,d), target(a,e), target(a,f), target(a,g), target(c,h)},
    {}
).


#neg({target(a,b)},{}). 
#neg({target(b,c)},{}). 
#neg({target(c,d)},{}). 
#neg({target(d,e)},{}). 
#neg({target(e,f)},{}). 
#neg({target(f,g)},{}). 
#neg({target(g,h)},{}). 
#neg({target(h,i)},{}).


#modeh(1, target(var(t),var(t)),(positive)).
#modeh(1, target_1(var(t),var(t)),(positive)).

#modeb(1, father(var(t),var(t)),(positive,anti_reflexive)).
#modeb(1, mother(var(t),var(t)),(positive,anti_reflexive)).
#modeb(2, target_1(var(t),var(t)),(positive,anti_reflexive)).

% #bias("allow_disjunction.").

% #minhl(4).
% #maxhl(4).
#disallow_multiple_head_variables.
% #max_penalty(30).
