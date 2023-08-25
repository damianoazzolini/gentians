# GENTIANS: GENeTic algoritm for inductive learning of ANswer Set programs.

This tool learns answer set programs from examples.
It also allows aggregates.


The documentation is in progress.

## Usage

You can get a list of the available options with:
```
python3 main.py --help
```

There are several built in examples.
See the file `example_programs.py` to see the structure of these, together with a biref description.
For example if you want to run the hamming example, you can use
```
python3 main.py -e hamming_0 -d 3 --aggregates "sum(d/2)" "count(d/2)" --comparison neq --verbose=2 --variables=4 -ua
```
where `-e` specifies the example, `-d` set the maximum length of a clause (number of literals), `--aggregates` is followed by the allowed aggregates, in this case `#sum` over `d/2` and `#count` over `d/2`, `--comparison` is followed by the allowed comparison operators, in this case `!=` (`neq`), `--verbose` is followed by the verbosity level, `--variables` is followed by the maximum number of variables in a rule, and `-ua` specifies that unbalanced aggregates are allowed.

All the experiments are stored as examples, so with the flag `-e` is it possible to run them all (simply select the one of interest). 

To specify your own example, fill the needed data into the function `user_defined` of `example_programs.py`.
Soon there will be the possibility to specifty a scenario via files.