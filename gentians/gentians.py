
import os.path
import sys
import time

# from argparse import Namespace

from .arguments import parse_arguments, version, Arguments
from .example_programs import run_example
from .program_sampler import ProgramSampler, Clause
from .strategies import Strategy, PlacedClause
from .utils import print_error_and_exit
from .parser import Parser, Program
from .variable_placer import VariablePlacer


class Solver:
    def __init__(self,
        # background : 'list[str]',
        # positive_examples : 'list[list[str]]',
        # negative_examples : 'list[list[str]]',
        # language_bias_head : 'list[str]',
        # language_bias_body : 'list[str]',
        program : Program,
        arguments : Arguments
        ) -> None:
        # self.background : 'list[str]' = background
        # self.positive_examples : 'list[list[str]]' = positive_examples
        # self.negative_examples : 'list[list[str]]' = negative_examples
        # self.language_bias_head : 'list[str]' = language_bias_head
        # self.language_bias_body : 'list[str]' = language_bias_body
        self.program : Program = program
        self.arguments : Arguments = arguments

    def solve(self) -> None:
        '''
        Main loop
        '''

        best_found : bool = False
        best_stub_for_next_round : 'list[Clause]' = []

        sampler = ProgramSampler(self.program.language_bias_head, self.program.language_bias_body, self.arguments)

        placer = VariablePlacer(self.arguments)

        start_total_time = time.time()

        for it in range(self.arguments.iterations):
            # Step 0: sample a list of clauses
            print(f"Sampling loop: {it}")
            start_time = time.time()
            print("Sampling clauses")
            cls = sampler.sample_clauses_stub(self.arguments.clauses_to_sample)
            sample_time = time.time() - start_time

            # add the best from the previous rounds
            cls.extend(best_stub_for_next_round)
            # clean up the best stub
            best_stub_for_next_round = []
            # Step 1: remove duplicates
            instantiated_clauses = [c.instantiated for c in cls]
            flat_instantiated_clauses = [item for sublist in instantiated_clauses for item in sublist]
            sampled_clauses = sorted(list(set(flat_instantiated_clauses)))
            print(f"Sampled {len(sampled_clauses)} different clauses in {sample_time} seconds")

            if self.arguments.verbosity >= 1:
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

            placed_list_improved : 'list[PlacedClause]' = list(map(PlacedClause, placed_list))

            print(f"Total clauses stub: {len(placed_list)}")
            print(f"Total number of possible clauses: {sum(len(pl) for pl in placed_list)}")

            if len(placed_list) == 0:
                print("No clauses found")
                sys.exit()

            if self.arguments.verbosity >= 2:
                for el in placed_list:
                    print(f"{len(el)}: {el}")

            # Step 3: genetic algorithm
            start_time = time.time()
            current_strategy = Strategy(
                placed_list_improved,
                self.program,
                self.arguments
            )

            prg, score, best_found, best_index_stub_for_the_next_round = current_strategy.genetic_solver()
            
            genetic_time = time.time() - start_time

            for i in best_index_stub_for_the_next_round:
                best_stub_for_next_round.append(sampled_clauses[i]) 

            print(f"Evolutionary cycle {it} - Time {genetic_time}")
            if best_found:
                print("--- Found best program ---")
            else:
                print(f"Current best with score: {score}")
            print("--------------------------")
            print(*prg, sep="\n")
            print("--------------------------")

            if best_found:
                break

        print(f"Total time: {time.time() - start_total_time}")


def main():
    """
    Main function.
    """
    print(f"Running GENTIANS version {version}.")
    args = parse_arguments()

    if args.profile:
        import cProfile
        import pstats
        import io
        from pstats import SortKey
        pr = cProfile.Profile()
        pr.enable()

    if args.version:
        sys.exit()

    if not args.example:
        if args.filename:
            p = Parser(args.filename)
            program = p.read_from_file()
        else:
            print_error_and_exit("Specify a file with the task or an example")
    else:
        # background, positive_examples, negative_examples, language_bias_head, language_bias_body = run_example(args.example)
        program = run_example(args.example)
    
    # generate auto language bias
    if args.automatic_language_bias != 0:
        print("Generating automatic language bias")
        program.auto_generate_language_bias(args.automatic_language_bias)
    
    if args.predicate_invention != 0:
        print("Invention mode")
        program.invent_predicates(args.predicate_invention)

    s = Solver(program, args)

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