

from two_sum import two_sum

def test_example_case():
    assert two_sum([2, 7, 11, 15], 9) == [1, 2]

def test_another_case():
    assert two_sum([1, 3, 4, 6, 8, 10], 10) == [3, 4]

def test_large_values():
    assert two_sum([1, 2, 3, 4, 4, 9, 56, 90], 8) == [4, 5]

def test_duplicate_values():
    assert two_sum([1, 1, 2, 3], 2) == [1, 2]

def test_no_solution():
    assert two_sum([1, 2, 3], 10) == []

def test_edge_case_single_element():
    assert two_sum([5], 5) == []           

def test_negative_numbers():
    assert two_sum([-3, -1, 0, 2, 4], 1) == [1, 5]
