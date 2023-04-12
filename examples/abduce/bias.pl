head_pred(grandparent, 2).
body_pred(father, 2).
body_pred(father, 2).
body_pred(mother, 2).
body_pred(mother, 2).

max_body(3).

% ********** SOLUTION **********
% Precision:1.00 Recall:1.00 TP:8 FN:0 TN:10 FP:0 Size:12
% grandparent(A,B):- mother(A,C),mother(C,B).
% grandparent(A,B):- mother(C,B),father(A,C).
% grandparent(A,B):- father(C,B),father(A,C).
% grandparent(A,B):- father(C,B),mother(A,C).
% ******************************