coin(c1).
coin(c2).
coin(c3).

#modeh(1, heads(var(coin))).
#modeh(1, tails(var(coin))).

#modeb(1, heads(var(coin))).
#modeb(1, tails(var(coin))).
#modeb(1, coin(var(coin)), (positive)).

#modeh(heads(var(coin)), (positive)).
#modeh(tails(var(coin)), (positive)).

% #constant(coin, c1).
% #constant(coin, c2).
% #constant(coin, c3).

#pos({heads(c1), tails(c2), heads(c3)},
     {tails(c1), heads(c2), tails(c3)}).

#pos({heads(c1), heads(c2), tails(c3)},
     {tails(c1), tails(c2), heads(c3)}).

% #bias("saturate.").