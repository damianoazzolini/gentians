
import os.path
import sys
import time

from argparse import Namespace

from .arguments import parse_arguments, version
from .example_programs import run_example
from .program_sampler import ProgramSampler
from .strategies import Strategy, PlacedClause
from .utils import read_popper_format, print_error_and_exit
from .variable_placer import VariablePlacer


class Solver:
    def __init__(self,
        background : 'list[str]',
        positive_examples : 'list[list[str]]',
        negative_examples : 'list[list[str]]',
        language_bias_head : 'list[str]',
        language_bias_body : 'list[str]',
        arguments : Namespace
        ) -> None:
        self.background : 'list[str]' = background
        self.positive_examples : 'list[list[str]]' = positive_examples
        self.negative_examples : 'list[list[str]]' = negative_examples
        self.language_bias_head : 'list[str]' = language_bias_head
        self.language_bias_body : 'list[str]' = language_bias_body
        self.verbose : int = arguments.verbose
        self.max_depth : int = arguments.depth
        self.max_variables : int = arguments.variables
        self.disjunctive_head_length : int = arguments.disjunctive_head
        self.unbalanced_aggregates : bool = arguments.unbalanced_agg
        self.sample_loops : int = arguments.iterations
        self.n_clauses_genetic : int = arguments.clauses
        self.pop_size_genetic : int = arguments.pop_size
        self.mutation_probability : float = arguments.mutation_probability
        self.iterations_genetic : int = arguments.iterations_genetic
        self.arguments = arguments
        self.max_as = arguments.max_as

        self.aggregates : 'list[str]' = arguments.aggregates
        self.comparison : 'list[str]' = arguments.comparison
        self.arithm : 'list[str]' = arguments.arithm
        self.cr : bool = arguments.cr # for choice rules
        self.invention : bool = arguments.invention # predicate invention


    def solve(self) -> None:
        '''
        Main loop
        '''

        best_found : bool = False
        best_stub_for_next_round : 'list[str]' = []

        sampler = ProgramSampler(
            self.language_bias_head,
            self.language_bias_body,
            max_depth = self.max_depth,
            max_variables = self.max_variables,
            prob_increase_level= self.arguments.prob_increase,
            # max_clauses = max_clauses,
            verbose = self.verbose,
            enable_find_max_vars_stub=False,
            find_all_possible_pos_for_vars_one_shot=True,
            disjunctive_head_length=self.disjunctive_head_length,
            unbalanced_aggregates=self.unbalanced_aggregates,
            allowed_aggregates=self.aggregates,
            arithmetic_operators=self.arithm,
            comparison_operators=self.comparison
        )

        placer = VariablePlacer(
            max_variables=self.max_variables,
            verbose=self.verbose,
            unbalanced_aggregates=self.unbalanced_aggregates
        )

        start_total_time = time.time()

        for it in range(self.sample_loops):
            # Step 0: sample a list of clauses
            print(f"Sampling loop: {it}")
            start_time = time.time()
            print("Sampling clauses")
            cls = sampler.sample_clause_stub(self.arguments.sample)
            sample_time = time.time() - start_time

            # add the best from the previous rounds
            cls.extend(best_stub_for_next_round)
            # clean up the best stub
            best_stub_for_next_round = []
            # Step 1: remove duplicates
            sampled_clauses = sorted(list(set(cls)))
            print(f"Sampled {len(sampled_clauses)} different clauses in {sample_time} seconds")
            # sys.exit()
            if self.verbose >= 1:
                print("Sampled clauses:")
                sampled_clauses.sort(key=lambda x : len(x))
                for index, current_cl in enumerate(sampled_clauses):
                    print(f"{index}) {current_cl}")

            # Step 2: place the variables
            # This is THE bottleneck: generation of all the 
            # possible locations, which are #n_vars^#n_pos in the 
            # worst case
            start_time = time.time()

            placed_list : 'list[list[str]]' = placer.place_variables_list_of_clauses(sampled_clauses)
            placing_time = time.time() - start_time
            print(f"Placed variables in {placing_time} seconds")

            placed_list_improved : 'list[PlacedClause]' = []
            for p in placed_list:
                pl = PlacedClause(p)
                placed_list_improved.append(pl)

            print(f"Total clauses stub: {len(placed_list)}")
            print(f"Total number of possible clauses: {sum(len(pl) for pl in placed_list)}")

            if len(placed_list) == 0:
                print("No clauses found")
                sys.exit()

            if self.verbose >= 2:
                for el in placed_list:
                    print(f"{len(el)}: {el}")

            # Step 3: genetic algorithm
            start_time = time.time()
            current_strategy = Strategy(
                placed_list_improved,
                self.background,
                self.positive_examples,
                self.negative_examples
            )

            prg, score, best_found, best_index_stub_for_the_next_round = current_strategy.genetic_solver(
                self.n_clauses_genetic,
                self.pop_size_genetic,
                self.mutation_probability,
                self.iterations_genetic)
            genetic_time = time.time() - start_time

            for i in best_index_stub_for_the_next_round:
                best_stub_for_next_round.append(sampled_clauses[i]) 
            # print(best_stub_for_next_round)
            print(f"Evolutionary cycle {it} - Time {genetic_time}")
            if best_found:
                print("--- Found best program ---")
            else:
                print(f"Current best with score: {score}")
            for r in prg:
                print(r)
            print("--------------------------")
            # print(f"Program: {prg}")
            if best_found:
                break

        print(f"Total time: {time.time() - start_total_time}")


def main():
    """
    Main function.
    """
    args = parse_arguments()

    if args.profile:
        import cProfile
        import pstats
        import io
        from pstats import SortKey
        pr = cProfile.Profile()
        pr.enable()

    if args.version:
        print(f"GENTIANS version: {version}.")
        sys.exit()

    background = []
    positive_examples = []
    negative_examples = []
    language_bias_head = []
    language_bias_body = []

    if args.example is None:
        if (os.path.isfile(args.directory + "bk.pl") and
            os.path.isfile(args.directory + "exs.pl") and
            os.path.isfile(args.directory + "bias.pl")):
            background, positive_examples, negative_examples,\
                language_bias_head, language_bias_body = read_popper_format(
                    args.directory)
            # print(background, positive_examples, negative_examples, language_bias_head, language_bias_body)
        else:
            print_error_and_exit("Specify a directory or an example")
    else:
        background, positive_examples, negative_examples, language_bias_head, language_bias_body = run_example(args.example)

    s = Solver(
        background, 
        positive_examples, 
        negative_examples, 
        language_bias_head, 
        language_bias_body,
        args
    )

    s.solve()

    if args.profile:
        pr.disable()
        s = io.StringIO()
        sortby = SortKey.CUMULATIVE # sort by total time
        # sortby = SortKey.CALLS # sort by number of calls
        ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
        ps.print_stats()
        print(s.getvalue())

if __name__ == "__main__":
    main()