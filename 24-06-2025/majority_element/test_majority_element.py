
from majority_element import majority_element

def test_case_1():
    assert majority_element([3, 2, 3]) == 3

def test_case_2():
    assert majority_element([2, 2, 1, 1, 1, 2, 2]) == 2

def test_case_3():
    assert majority_element([1, 1, 1, 1, 2, 3, 4]) == 1

def test_case_4():
    assert majority_element([9]) == 9

def test_case_5():
    assert majority_element([5, 5, 6, 5, 6, 5, 5]) == 5
