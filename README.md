# GENTIANS: GENeTic algorithm for Inductive learning of ANswer Set programs.

This tool learns answer set programs from examples.
It also allows aggregates.

The documentation is in progress.

## Installation
```
python -m pip install .
```
in the root folder (here).
If you want to modify it, add the option `-e` before `.`

## Usage

You can get a list of the available options with:
```
gentians --help
```

There are several built in examples.
See the file `example_programs.py` to see the structure of these, together with a brief description.
For example if you want to run the hamming example, you can use
```
gentians -e hamming_0 -d 3 --aggregates "sum(d/2)" "count(d/2)" --comparison neq --verbose=2 --variables=4 -ua
```
where `-e` specifies the example, `-d` set the maximum length of a clause (number of literals), `--aggregates` is followed by the allowed aggregates, in this case `#sum` over `d/2` and `#count` over `d/2`, `--comparison` is followed by the allowed comparison operators, in this case `!=` (`neq`), `--verbose` is followed by the verbosity level, `--variables` is followed by the maximum number of variables in a rule, and `-ua` specifies that unbalanced aggregates are allowed.

All the experiments are stored as examples, so with the flag `-e` is it possible to run them all (simply select the one of interest). 

To specify your own example, fill the needed data into the function `user_defined` of `example_programs.py`.
Soon there will be the possibility to specify a scenario via files.

## Language Bias Definition
You can define the language bias (i.e., atoms and literals that can appear in the head and body of rules) with the following syntax.
For head atoms
```
#modeh(recall, atom, arity).
```
define an atom `atom` with arity `arity` that can appear at most once in the head.
For example, with `#modeh(1,a,2)` you may obtain `a(X,Y)` in the head.

For positive body literals
```
#modeb(recall, atom, arity, positive).
```
while for negative body literals
```
#modeb(recall, atom, arity, negative).
```
with the same syntax as for head atoms.
Here, `positive` and `negative` are reserved keywords so they should be written as they are.
For example, with `#modeb(1, a, 2, positive)` you may obtain `a(X,Y)` in the body while with `#modeb(1, a, 2, negative)` you may also obtain not `a(X,Y)`.

## Examples definition
Positive examples must follow the syntax
```
#pos({included}, {excluded}).
```
while negative examples must follow the syntax
```
#neg({included}, {excluded}).
```
where, in both cases, `included` and `excluded` can be either empty, a single atom, or a conjunction of atoms.

Some examples are:
```
#pos({odd(1), odd(3), even(2)}, {}).
#neg({even(3)}, {}).
```

## Aggregates in Language Bias
You can define aggregates in the language bias via the `--aggregates` option on the CLI (not directly in the source file, by now).

For one aggregation atom you can use:
`--aggregates "aggregation_function(aggregation_atom)"`
where `aggregation_function` is the aggregation function (`sum` or `count`, for example) and `aggregation_atom` is a term of the form `name/arity`, representing the atom aggregating on.
If you want to aggregate over multiple atoms, you can use multiple aggregation atoms separated by commas.
You can pass multiple aggregates.

Examples:
```bash
# defines a `#sum` aggregate over `x/3`
--aggregates "sum(x/3)"
# defines a `#sum` aggregate over `x/3` and `size/1`
--aggregates "sum(x/3,size/1)"
# defines a `#sum` aggregate over `p/2` and a `#count` aggregate also over `p/2`
--aggregates "sum(p/2)" "count(p/2)"
# defines a `#sum` aggregate over `p/2` and a #count aggregate over `q/2`
--aggregates "sum(p/2)" "count(q/2)"
```

## Comparison and Arithmetic Operators in Language Bias
You can define comparison operators and arithmetic operators in the language bias via the `--comparison` and `--arithm` option, respectively, on the CLI (not directly in the source file, by now).

The following comparison operators are considered: `lt` (<), `leq` (=<), `gt` (>), `geq` (>=), `eq` (=), and `neq` (!=).
The following arithmetic operators are considered: `add` (+), `sub` (-), `mul` (*), `div` (/), and `abs` (absolute value).
You can pass multiple comparison and arithmetic.

Examples:
```
--comparison neq
--comparison neq geq
--arithm add
--arithm add mul sub
```

## Automatic Language Bias
You can leave the solver discovering the language bias automatically.
This scans positive and negative examples and background knowledge and extracts the signature for each atom in the examples and each head and body literal in background knowledge.
Then, adds each signature as mode bias for the head and for the body.
You can activate this with the flag `-alb=n` where `n` is a number: if it is positive, indicates the recall for each literal (i.e., all literals will have the same recall); if it is negative, its absolute value indicates the recall for each literal and also states that these can be negated literals.
Note that `-alb` ignores the language bias defined in the program file (i.e., `#modeb` and `#modeh`).
If you also use `--aggregates`, `--comparison`, or `--arithm` options, these will be kept.

Example: suppose we have in the program
```
a:- b.
#pos({f(1)},{f(1,a)}).
```
The flag -alb=1 translates into:
```
#modeh(1, a, 0).
#modeh(1, f, 1).
#modeh(1, f, 2).
#modeh(1, b, 0).
#modeb(1, a, 0, positive).
#modeb(1, f, 1, positive).
#modeb(1, f, 2, positive).
#modeb(1, b, 0, positive).
```
If `-alb=-1` is used, the `#modeb` above will have `negative` instead of `positive` as fourth argument.

Currently, pay attention when using this together with aggregates, since you may encounter an infinite loop whle grounding the program.

## Predicate Invention
You can enable predicate invention with the option `--invention=N` where `N` is the number of predicates to invent.
For each `i` in `{1, ..., N}` it generates a predicate `__inv_i__` with arity 1 and 2 to consider in the head and body of clauses.

Example:
```
--invention=1
```

## Main Available Options

You can check all the available options with the flag `--help`.
Here we list only the main ones:
- `--variables`: maximum number of variables to consider in a rule. Default 3.
- `-d`: maximum number of literals in a rule (number of atoms in the head + number of literals in the body). Default 3
- `-dh`: set the maximum number of atoms in disjunctive head. Default 0.
- `-s`: number of clauses to sample. Default 1000
- `-ua`: enable unbalanced aggregates. Default false (i.e., not enabled).
- `-e`: run a predefined example
- `--comparison`: enable comparison operators. It should be followed by one or more among `lt`,`leq`,`gt`,`geq`,`eq`,`neq`. To allow the use of the same operator more than once (i.e., to increase it recall) write it many times. For example, `--comparison lt lt` enables the use of the operator `<` at most twice in the body. Default none (i.e., no comparison operators)
- `--arithm`: enable arithmetic operators. It should be followed by one or more among `add`,`sub`,`mul`,`div`,`abs`. To allow the use of the same operator more than once (i.e., to increase it recall) write it many times. For example, `--arithm add add` enables the use of the addition at most twice in the body. Default none (i.e., no arithmetic operators)
- `--aggregates`: enable the use of aggregates. It should be followed by an atom of the form `sum(a/1)`, where sum is the aggregate and a/1 is the atom to consider in the aggregation. Multiple atoms can be separated by a comma, such as `sum(a/1,b/1)`. 