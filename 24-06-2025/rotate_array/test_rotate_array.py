
from rotate_array import rotate_array

def test_basic_rotation():
    assert rotate_array([1, 2, 3, 4, 5, 6, 7], 3) == [5, 6, 7, 1, 2, 3, 4]

def test_rotate_by_zero():
    assert rotate_array([1, 2, 3], 0) == [1, 2, 3]

def test_rotate_full_length():
    assert rotate_array([1, 2, 3], 3) == [1, 2, 3]

def test_k_greater_than_length():
    assert rotate_array([1, 2, 3], 5) == [2, 3, 1]

def test_single_element():
    assert rotate_array([9], 100) == [9]

def test_empty_array():
    assert rotate_array([], 3) == []
