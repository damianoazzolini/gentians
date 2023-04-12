import clingo
import sys

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
        Returns the number of covered positive and covered
        negative examples.
        '''
        ctl = clingo.Control(self.clingo_arguments)
        try:
            # self.lines = self.lines[1:]
            # self.lines.append("odd(V0):- even(V1), prev(V0,V1).")
            # self.lines.append("even(V0):- odd(V1), prev(V0,V1).")
            for clause in self.lines:
                # print(clause)
                ctl.add('base', [], clause)
            ctl.ground([("base", [])])
        except Exception as e:
            return -1, -1
            # print(type(e))
            # print(e.args)
            # # TODO: handle unsafe vars or check this while 
            # # generating the clause
            # print('Syntax error, parsing failed.')
        
        # res = str(ctl.solve())
        
        answer_sets : 'list[str] '= []

        # print(f'----- {mode}')
        with ctl.solve(yield_=True) as handle:  # type: ignore
            for m in handle:  # type: ignore
                answer_sets.append(str(m))
        
        print("answer sets")
        print(answer_sets)

        count_positive = 0
        count_negative = 0
        
        # print(*answer_sets, sep='\n')
        # print("interpretation_pos")
        # print(interpretation_pos)
        # print("interpretation_neg")
        # print(interpretation_neg)

        # se unsat restituire 0
        if len(answer_sets) == 0:
            # unsat
            return 0, len(interpretation_neg)

        # check the coverage of the positive and negative examples
        
        # check positive coverage
        for interp in interpretation_pos:
            # for each positive example
            found = True
            for model in answer_sets:
                # loop through the computed answer sets
                # print(model)
                for ii in interp.split(' '):
                    if ii not in model:
                        found = False
                        # exact coverage: every atom should be present
                        break
            count_positive += int(found)

        # check negative coverage        
        for interp in interpretation_neg:
            found = False
            for model in answer_sets:
                for ii in interp.split(' '):
                    if ii in model:
                        found = True
                        # exact coverage: none of the atoms should be present
                        break
            count_negative += int(found)

        return count_positive, count_negative

        # if (res == 'SAT' and mode) or (res == 'UNSAT' and not mode):
        #     return True
        # else:
        #     return False
        
    def extract_coverage_and_set_clauses(self,
        program : 'list[str]', 
        interpretation_pos : 'list[str]', 
        interpretation_neg : 'list[str]',
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
        try:
            generated_program = ""
            # add the background knowledge
            for clause in self.lines:
                generated_program += f"{clause}\n"
                # ctl.add('base', [], clause)
                
            # add the sampled program
            cl_index = 0

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

            # add the interpretation pos
            cl_index = 0
            for atoms in interpretation_pos:
                r = f"cp({cl_index}):- {','.join(atoms.split(' '))}.\n"
                # print(r)
                generated_program += r
                # ctl.add('base', [], r)
                cl_index += 1
            generated_program += '\n'
            
            
            # add the interpretation negative
            cl_index = 0
            for atoms in interpretation_neg:
                # split the answer set since none of the atoms should be true
                r = f"cn({cl_index}):- {','.join(atoms.split(' '))}.\n"
                # print(r)
                generated_program += r
                # ctl.add('base', [], r)
                cl_index += 1
            generated_program += '\n'
            
            generated_program += '''
            % s_sel(N):- N = #count{X : r(X)}.
            covered_pos(N):- N = #count{X : cp(X)}.
            covered_neg(N):- N = #count{X : cn(X)}.

            % @p is the priority: the greter it is, the higher is the
            % importance of the constraint. For example, here the most
            % important task is to maximize the coverage of the positive
            % then minimize the negative and then minimize the number
            % of clauses.
            % I cannot minimize or maximize since none of the AS should
            % cover negative examples.
            % #maximize{N@3 : covered_pos(N)}.
            % #minimize{N@2 : covered_neg(N)}.
            % #minimize{N@1 : s_sel(N)}.
            
            #show covered_neg/1.
            #show covered_pos/1.
            #show cp/1.
            #show cn/1.
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
                elif atom.startswith('cp'):
                    l_cp.append(int(atom.split('cp(')[1][:-1]))
                elif atom.startswith('cn'):
                    l_cn.append(int(atom.split('cn(')[1][:-1]))
            
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

        return comb_rules
        
        