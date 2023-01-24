import clingo

class ClingoInterface:
    def __init__(self, lines : 'list[str]', clingo_arguments : 'list[str]' = ['-Wnone', '0']) -> None:
        self.lines = lines
        self.clingo_arguments = clingo_arguments


    def init_clingo_ctl(self) -> 'clingo.Control':
        '''
        Init clingo and grounds the program
        '''
        ctl = clingo.Control(self.clingo_arguments)
        try:
            for clause in self.lines:
                ctl.add('base', [], clause)
            ctl.ground([("base", [])])
        except RuntimeError:
            # TODO: handle unsafe vars or check this while 
            # generating the clause
            print('Syntax error, parsing failed.')

        return ctl


    def test_coverage_example(self, interpretation_pos : 'list[str]', interpretation_neg : 'list[str]') -> 'tuple[int,int]':
        '''
        Init clingo and grounds the program.
        mode == True -> positive example
        mode == False -> negative example
        Returns true if program covers the example.
        '''
        ctl = clingo.Control(self.clingo_arguments)
        try:
            # add the background knowledge
            # print(self.lines)
            for clause in self.lines:
                # print(clause)
                ctl.add('base', [], clause)

            # add the statement for the coverage: an interpretation is
            # a set of literals: [i_1, i_2, ..., i_n]
            # first define an auxiliary clause
            # i:- i_1, i_2, ..., i_n
            # Then add
            # :- not interpretation if mode is True (positive)
            # :- interpretation if mode is False (negative)
            # aux_clause : str = "__aux_i__:- "
            # for el in interpretation:
            #     aux_clause += el + ','
            # aux_clause = aux_clause[:-1] + '.'
            
            # ctl.add('base', [], aux_clause)
            # print(aux_clause)
            # ctl.add('base', [], ':- ' + ('not ' if mode else '') + "__aux_i__.")
            # print(':- ' + ('not ' if mode else '') + "__aux_i__.")

            ctl.ground([("base", [])])
        except Exception as e:
            return -1, -1
            # print(type(e))
            # print(e.args)
            # # TODO: handle unsafe vars or check this while 
            # # generating the clause
            # print('Syntax error, parsing failed.')
        
        res = str(ctl.solve())
        
        answer_sets : 'list[str] '= []

        # print(f'----- {mode}')
        with ctl.solve(yield_=True) as handle:  # type: ignore
            for m in handle:  # type: ignore
                answer_sets.append(str(m))
        # print(answer_sets)

        count_positive = 0
        count_negative = 0
        
        # print(*answer_sets, sep='\n')
        # print(interpretation_pos)

        for interp in interpretation_pos:
            # print(interp.split(' '))
            found = False
            for model in answer_sets:
                if all(i in model for i in interp):
                # if interp in model:
                    found = True
                    break
                    # print('in')
            count_positive += int(found)
        
        # TODO: fix this
        for interp in interpretation_neg:
            found = False
            for model in answer_sets:
                if all(i in model for i in interp):
                # if interp in model:
                    found = True
                    break
            count_negative += int(found)
                
        
        return count_positive, count_negative

        # if (res == 'SAT' and mode) or (res == 'UNSAT' and not mode):
        #     return True
        # else:
        #     return False
        
        