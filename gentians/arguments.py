import argparse

program_description = "GENTIANS: GENeTic algorithm for Inductive learning of ANswer Set programs."

version = "1.0.1" 

def parse_arguments() -> 'argparse.Namespace':
    '''
    Parses command line arguments.
    '''
    command_parser = argparse.ArgumentParser(description=program_description)
    command_parser.add_argument(
        "-dir",
        "--directory",
        help="Directory storing the bk.pl, exs.pl, and bias.pl files (Popper format).",
        type=str,
        default="."
    )
    command_parser.add_argument(
        "-v",
        "--verbose",
        help="Verbosity",
        type=int,
        choices=range(0,3),
        default=0
    )
    command_parser.add_argument(
        "-vars",
        "--variables",
        help="Max number of variables to consider in a rule",
        type=int,
        default=3
    )
    command_parser.add_argument(
        "-d",
        "--depth",
        help="Max number of literals in rules",
        type=int,
        default=3
    )
    command_parser.add_argument(
        "-pil",
        "--prob-increase",
        help="Probability to add one more literal in the current clause (used in sampling)",
        type=float,
        default=0.5
    )
    command_parser.add_argument(
        "-dh",
        "--disjunctive-head",
        help="Max atoms in head",
        type=int,
        default=1
    )
    command_parser.add_argument(
        "-s",
        "--sample",
        help="Number of clauses to sample",
        type=int,
        default=1000
    )
    command_parser.add_argument(
        "-ua",
        "--unbalanced-agg",
        help="Enable unbalanced aggregates",
        action="store_true"
    )
    command_parser.add_argument(
        "--max_as",
        help="Max number of answer sets to generate",
        type=int,
        default=5000
    )
    command_parser.add_argument(
        "-c",
        "--clauses",
        help="Max clauses to consider in a program",
        type=int,
        default=6
    )
    command_parser.add_argument(
        "-it",
        "--iterations",
        help="Max number of sample and genetic iterations",
        type=int,
        default=100
    )
    command_parser.add_argument(
        "-p",
        "--pop-size",
        help="Population size",
        type=int,
        default=50
    )
    command_parser.add_argument(
        "-itg",
        "--iterations-genetic",
        help="Number of iterations for the genetic algorithm",
        type=int,
        default=2000
    )
    command_parser.add_argument(
        "-mp",
        "--mutation-probability",
        help="Mutation probability",
        type=float,
        default=0.2
    )
    command_parser.add_argument(
        "-e",
        "--example",
        help="Load a predefined example",
        choices=[
            "coin", 
            "even_odd",
            "animals_bird",
            "coloring",
            "adjacent_to_red",
            "grandparent",
            "4queens",
            "5queens", 
            "clique", 
            "sudoku",
            # "euclid",
            # "dummy", 
            "subset_sum",
            "subset_sum_double",
            "subset_sum_double_and_sum",
            "subset_sum_double_and_prod",
            "subset_sum_triple",
            "hamming_0", 
            "hamming_1", 
            # "harder_hamming_0",
            # "harder_hamming_1",
            "magic_square_no_diag", 
            "latin_square", 
            "set_partition_sum",
            "set_partition_sum_and_cardinality", 
            "set_partition_sum_cardinality_and_square",
            "set_partition_sum_new", 
            "set_partition_sum_and_cardinality_new",
            "user_defined"
        ],
        default=None
    )
    command_parser.add_argument(
        "--comparison",
        help="Enables the usage of comparison \
        predicates: less than (<) with lt, less equal (<=) with leq, \
        greater than (>) with gt, greater equal (>=) with geq \
        equal (==) with eq and different (!=) with neq.\
        Example: --comparison lt gt eq diff",
        nargs='+',
        required=False,
        choices=["lt","leq","gt","geq","eq","neq"]
    )
    command_parser.add_argument(
        "--arithm",
        help="Enables the usage of arithmetic \
        predicates: add (+), sub(-), mul(*), div(/), and abs (||). Example: \
        --arithm add sub mul div abs",
        nargs='+',
        required=False,
        choices=["add","sub","mul","div","abs"]
    )
    command_parser.add_argument(
        "--cr",
        help="Enables the generation of choice rules.",
        action="store_true"
    )
    command_parser.add_argument(
        "--invention",
        help="Enables predicate invention with n predicates. Example --invention=1",
        type=int,
        default=0
    )
    command_parser.add_argument(
        "--aggregates",
        help="Enable aggregates. Example:\
        --aggregates sum(a/1) count (a/1). Specify the atom to aggregate.", 
        nargs='+',
        required=False
    )
    command_parser.add_argument(
        "--profile",
        help="Enables profiling", 
        default=False,
        action="store_true"
    )
    command_parser.add_argument(
        "--version",
        help="Prints the program version and exits", 
        action="store_true"
    )
    
    return command_parser.parse_args()