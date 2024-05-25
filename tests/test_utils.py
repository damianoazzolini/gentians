import pytest

import gentians.utils

class TestUnit:
    @pytest.mark.parametrize("l_in, expected_atoms", [
        ([[0,3],[1,5],[2,4]], "v0(0) v0(3) v1(1) v1(5) v2(2) v2(4)"),
        ([[0,3],[1,5]], "v0(0) v0(3) v1(1) v1(5)"),
        ([[0,3],[1,5],[2]], "v0(0) v0(3) v1(1) v1(5) v2(2)")
    ])
    def test_from_list_to_as(self, l_in, expected_atoms):
        computed = gentians.utils.from_list_to_as(l_in)
        assert expected_atoms == computed
    
    @pytest.mark.parametrize("atoms_in, expected_list", [
        ("v0(0) v0(3) v1(1) v1(5) v2(2) v2(4)", [[0,3],[1,5],[2,4]]),
        ("v0(0) v0(3) v1(1) v1(5)", [[0,3],[1,5]]),
        ("v0(0) v0(3) v1(1) v1(5) v2(2)", [[0,3],[1,5],[2]]),
        ("v1(1) v1(7) v1(5) v0(0) v0(3) v2(2) v2(4)", [[0,3],[1,5,7],[2,4]])
    ])
    def test_from_as_to_list(self, atoms_in, expected_list):
        computed = gentians.utils.from_as_to_list(atoms_in)
        assert expected_list == computed

    def test_find_symmetric_answer_sets(self):
        s = "v0(0) v0(3) v1(1) v1(5) v1(7) v2(2) v2(4)"
        expected = ["v0(0) v0(3) v1(1) v1(5) v1(7) v2(2) v2(4)", "v0(0) v0(3) v2(1) v2(5) v2(7) v1(2) v1(4)"]
        assert gentians.utils.find_symmetric_answer_sets(s) == expected
    
    @pytest.mark.parametrize("rule, expected_list", [
        (":- blue(V1),blue(V1),e(V0,V0),green(V0).", ['#false', 'blue(V1)', 'blue(V1)', 'e(V0,V0)', 'green(V0)']),
        ("a:- blue(V1),blue(V1),e(V0,V0),green(V0).", ['a', 'blue(V1)', 'blue(V1)', 'e(V0,V0)', 'green(V0)'])
    ])
    def test_get_atoms(self, rule, expected_list):
        assert gentians.utils.get_atoms(rule) == expected_list



class TestIntegration:
    @pytest.mark.parametrize("rule, is_valid", [
        (":- blue(V1),blue(V1),e(V0,V0),green(V0).", False),
        (":- blue(V1),blue(V0),e(V0,V1),green(V0).", True),
        (":- e(V0,V1),V0>V1.", True),
        (":- e(V0,V1),V0>V0.", False),
        (":- e(V0,V1),V0>=V0.", False),
        (":- e(V0,V1),V0>=V1.", True),
        (":- e(V0,V1),V0+V1=V2.", True),
        (":- e(V0,V1),V0+V0=V2.", True),
        (":- e(V0,V1),V0+V0=V0.", False),
        (":- e(V0,V1),V0+V0=V2.", True),
        (":- e(V0,V1),V0+V0=V2, not a(V2).", True),
        (":- e(V0,V1),V0+V0=V2, not a(V3).", False),
        ("a:- V = #sum{X : a(X)}.", True)
    ])
    def test_is_valid_rule(self, rule, is_valid):
        assert gentians.utils.is_valid_rule(rule) == is_valid
