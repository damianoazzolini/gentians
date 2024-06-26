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
See the file `example_programs.py` to see the structure of these, together with a biref description.
For example if you want to run the hamming example, you can use
```
gentians -e hamming_0 -d 3 --aggregates "sum(d/2)" "count(d/2)" --comparison neq --verbose=2 --variables=4 -ua
```
where `-e` specifies the example, `-d` set the maximum length of a clause (number of literals), `--aggregates` is followed by the allowed aggregates, in this case `#sum` over `d/2` and `#count` over `d/2`, `--comparison` is followed by the allowed comparison operators, in this case `!=` (`neq`), `--verbose` is followed by the verbosity level, `--variables` is followed by the maximum number of variables in a rule, and `-ua` specifies that unbalanced aggregates are allowed.

All the experiments are stored as examples, so with the flag `-e` is it possible to run them all (simply select the one of interest). 

To specify your own example, fill the needed data into the function `user_defined` of `example_programs.py`.
Soon there will be the possibility to specify a scenario via files.

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