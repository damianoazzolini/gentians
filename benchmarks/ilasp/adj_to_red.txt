edge(a,b).
edge(b,a).
edge(c,d).
edge(c,e).
edge(d,e).
colour(a,red).
colour(b,green).
colour(c,red).
colour(d,red).
colour(e,green).
red(red).
green(green).

    

#pos({target(b)},{}). 
#pos({target(c)},{}).

    
#neg({target(a)},{}). 
#neg({target(d)},{}). 
#neg({target(e)},{}).

#modeh(1, target(var(t)), (positive)).

#modeb(1, target(var(t)), (positive)).
#modeb(1, edge(var(t),var(t)), (positive, symmetric, anti_reflexive )).
#modeb(1, colour(var(t),var(t)), (positive, symmetric, anti_reflexive )).
#modeb(1, red(var(t)), (positive)).
#modeb(1, green(var(t)), (positive)).

% #bias("saturate.").