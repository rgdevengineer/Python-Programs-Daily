
from find_all_duplicates import find_duplicates

def test_example():
    assert sorted(find_duplicates([4, 3, 2, 7, 8, 2, 3, 1])) == [2, 3]

def test_no_duplicates():
    assert find_duplicates([1, 2, 3, 4, 5]) == []

def test_all_duplicates():
    assert sorted(find_duplicates([1, 1, 2, 2, 3, 3])) == [1, 2, 3]

def test_single_element():
    assert find_duplicates([1]) == []

def test_empty():
    assert find_duplicates([]) == []

def test_large_input():
    nums = list(range(1, 5001)) + list(range(1, 5001))
    assert sorted(find_duplicates(nums)) == list(range(1, 5001))
