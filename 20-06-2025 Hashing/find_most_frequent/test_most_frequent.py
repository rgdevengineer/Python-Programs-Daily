
from most_frequent import find_most_frequent

def test_basic_case():
    assert find_most_frequent([1, 2, 3, 2, 2, 4]) == 2

def test_all_unique():
    result = find_most_frequent([1, 2, 3, 4])
    assert result in [1, 2, 3, 4]  # Any one is okay

def test_all_same():
    assert find_most_frequent([7, 7, 7]) == 7

def test_empty_list():
    assert find_most_frequent([]) is None

def test_tie_case():
    result = find_most_frequent([1, 2, 2, 3, 3])
    assert result in [2, 3]
