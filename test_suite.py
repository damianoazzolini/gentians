import unittest

import main

# c1 = Clause(["penguin(X)"],["bird(X)","not can(X,fly)"])

def init_program_bird() -> 'main.Solver':
    backgorund : 'list[str]' = [
    'bird(alice).', 
    'bird(betty).', 
    'can(alice,fly).', 
    'can(betty,swim).', 
    'ability(fly).', 
    'ability(swim).'
    ]
    positive_examples : 'list[str]' = ["penguin(betty)."]

    negative_examples : 'list[str]' = ["penguin(alice)."]

    language_bias_head : 'list[str]' = ['modeh(1, penguin(+)).']
    language_bias_body : 'list[str]' = ['modeb(1, bird(+)).', 'modeb(*, not can(+,#)).']

    return main.Solver(backgorund, positive_examples, negative_examples, language_bias_head, language_bias_body)


class TestCoverage(unittest.TestCase):
    

    def test_coverage_1_1(self):
        c1 = main.Clause(["penguin(X)"],["bird(X)"])
        p = main.Program([c1], 0, 0)
        s = init_program_bird()
        pos, neg = s.test_coverage(p)
        expected_pos = 1
        expected_neg = 1
        self.assertEqual(pos, expected_pos, f"Pos expected {expected_pos} found {pos}")
        self.assertEqual(neg, expected_neg, f"Neg expected {expected_neg} found {neg}")

    def test_coverage_1_0(self):
        c1 = main.Clause(["penguin(X)"],["bird(X)", "not can(X,fly)"])
        p = main.Program([c1], 0, 0)
        s = init_program_bird()
        pos, neg = s.test_coverage(p)
        expected_pos = 1
        expected_neg = 0
        self.assertEqual(pos, expected_pos, f"Pos expected {expected_pos} found {pos}")
        self.assertEqual(neg, expected_neg, f"Neg expected {expected_neg} found {neg}")

    
    def test_coverage_0_1(self):
        c1 = main.Clause(["penguin(X)"],["bird(X)", "can(X,fly)"])
        p = main.Program([c1], 0, 0)
        s = init_program_bird()
        pos, neg = s.test_coverage(p)
        expected_pos = 0
        expected_neg = 1
        self.assertEqual(pos, expected_pos, f"Pos expected {expected_pos} found {pos}")
        self.assertEqual(neg, expected_neg, f"Neg expected {expected_neg} found {neg}")



if __name__ == '__main__':
    unittest.main()