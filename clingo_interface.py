import clingo
import sys

import utils


class Coverage:
    def __init__(self, l_pos : 'list[int]' = [], l_neg : 'list[int]' = []):
        self.l_pos = l_pos
        self.l_neg = l_neg

    def __str__(self) -> str:
        return "Positive: " + ','.join([str(x) for x in self.l_pos]) + " - Negative: " + ','.join([str(x) for x in self.l_neg])
        
    def __repr__(self) -> str:
        return self.__str__()


class ClingoInterface:
    def __init__(self, lines : 'list[str]', clingo_arguments : 'list[str]' = ['-Wnone', '0']) -> None:
        self.lines = lines
        self.clingo_arguments = clingo_arguments


    # TODO: cambiare questione coverage
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

        
    def extract_coverage_and_set_clauses(self,
        program : 'list[str]', 
        interpretation_pos : 'list[list[str]]', 
        interpretation_neg : 'list[list[str]]',
        fixed : bool = True
        ) -> 'dict[str,Coverage]':
        '''
        Extracts the coverage for every subset of clauses.
        '''
        # l_results : 'list[tuple[int,int,list[int]]]' = []
        # TODO: ora fisso il numero massimo di clausole e il
        # solver ASP mi dice quale combinazione è la migliore.
        # Potrei invece (da fare) considerare iterativamente un 
        # numero di clausole maggiore.
        
        ctl = clingo.Control(self.clingo_arguments)
        # print("----- HERE -----")
        # print('FISSATO')
        # # program = ["tails(V0); heads(V0):-  coin(V0)."]
        # program = [ "odd(V1):- even(V0), prev(V1,V0).", "even(V1):-  prev(V1,V0), odd(V0).", ":- even(V1), odd(V0), prev(V1,V0)."]
        # program = ["odd(V1); even(V1):- odd(V0), prev(V1,V0), r(0).", "odd(V0):-  even(V1), prev(V0,V1), r(1)."]
        # program = ["red(X) ; green(X) ; blue(X) :- node(X).", ":- e(X,Y), red(X), red(Y).", ":- e(X,Y), green(X), green(Y).", ":- e(X,Y), blue(X), blue(Y)."]
        # program = [':- e(V0,V1),node(V0),red(V0),red(V1).', ':- e(V1,V0),green(V1),green(V0).', 'blue(V0);green(V0);red(V0):- node(V0).', 'blue(V0);red(V1):- e(V1,V0).', 'blue(V1);green(V0):- red(V1),red(V0).', 'red(V1):- blue(V1),blue(V0),e(V0,V1).']

        try:
            generated_program = ""
            # add the background knowledge
            for clause in self.lines:
                generated_program += f"{clause}\n"
                # ctl.add('base', [], clause)

            # add the sampled program
            cl_index = 0

            # program = ["heads(V1) :- coin(V1), not tails(V1).", "tails(V1) :- coin(V1), not heads(V1)."]
            
            for clause in program:
                if not fixed:
                    r = f"r({cl_index})"
                    nc = clause[:-1] + f", {r}.\n"
                    # print(nc)
                    generated_program += nc
                    generated_program += "{" + r + "}.\n"
                    cl_index += 1
                else:
                    generated_program += clause
            generated_program += '\n'

            if len(interpretation_pos) > 0:
                generated_program += f"pos_exs(0..{len(interpretation_pos)}).\n"
                generated_program += utils.generate_clauses_for_coverage_interpretations(
                    interpretation_pos, True)
            
            if len(interpretation_neg) > 0:
                generated_program += f"neg_exs(0..{len(interpretation_neg)}).\n"
                generated_program += utils.generate_clauses_for_coverage_interpretations(
                    interpretation_neg, False)
            
            
            generated_program += '''
            extended_p(I):- pos_exs(I), cpi(I), not cpe(I).
            extended_n(I):- neg_exs(I), cni(I), not cne(I).
            
            total_extended_p(N):- N = #count{X : extended_p(X)}.
            total_extended_n(N):- N = #count{X : extended_n(X)}.
            
            #show extended_p/1.
            #show extended_n/1.
            
            #show total_extended_p/1.
            #show total_extended_n/1.
            '''
            if not fixed:
                generated_program += "\n#show r/1."

            # print("ASP PROGRAM\n"+ generated_program)
            
            # sys.exit()
            
            ctl.add('base', [], generated_program)
            
            # ground the program
            ctl.ground([("base", [])])
        except Exception as e:
            return {"Error": Coverage([],[])}
        
        # res = str(ctl.solve())
        answer_sets : 'list[str] '= []
        # key: rule_id (string containing the selected rules)
        # value: tuple(covered_pos, covered_neg)
        # needes since I need to check that NO answer sets cover
        # negative examples.
        # comb_rules : 'dict[str,tuple[int,int]]' = {}
        # comb_rules : 'list[tuple[str,int,int]]' = []
        comb_rules : 'dict[str,Coverage]' = {}
        
        # print(f'----- {mode}')
        with ctl.solve(yield_=True) as handle:  # type: ignore
            for m in handle:  # type: ignore
                answer_sets.append(str(m))
        
        # print("--- Answer sets ---")
        # print(answer_sets)
        # there can be multiple AS 
        for answer_set in answer_sets:
            # cp = 0
            # cn = 0
            l_cp : 'list[int]' = []
            l_cn : 'list[int]' = []
            l_rules : 'list[int]' = []
            for atom in answer_set.split(' '):
                # extracts the atoms
                # if atom.startswith('covered_pos'):
                #     cp = int(atom.split('covered_pos(')[1][:-1])
                # elif atom.startswith('covered_neg'):  
                #     cn = int(atom.split('covered_neg(')[1][:-1])
                if atom.startswith('r'):
                    l_rules.append(int(atom.split('r(')[1][:-1]))
                elif atom.startswith('extended_p'):
                    l_cp.append(int(atom.split('extended_p(')[1][:-1]))
                elif atom.startswith('extended_n'):
                    l_cn.append(int(atom.split('extended_n(')[1][:-1]))
            
            if fixed:
                # needed since for fixed there are no r/1 atoms
                l_rules = [i for i in range(len(program))]
            dict_key = ''.join(str(index) for index in l_rules)
            if dict_key in comb_rules:
                # this solution also considers duplicates
                comb_rules[dict_key].l_pos.extend(l_cp)
                comb_rules[dict_key].l_neg.extend(l_cn)
            else:
                comb_rules[dict_key] = Coverage(l_cp, l_cn)

        # print(comb_rules)
        return comb_rules
        
        