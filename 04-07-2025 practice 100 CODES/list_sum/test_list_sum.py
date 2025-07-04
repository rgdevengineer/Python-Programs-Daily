
# test_list_sum.py

import pytest
from list_sum import ListSum

def test_sum_basic():
    lister = ListSum([1, 2], [3, 4])
    assert lister.get_sum() == [1, 2, 3, 4]

def test_sum_with_empty_first():
    lister = ListSum([], [3, 4])
    assert lister.get_sum() == [3, 4]

def test_sum_with_empty_second():
    lister = ListSum([1, 2], [])
    assert lister.get_sum() == [1, 2]

def test_sum_both_empty():
    lister = ListSum([], [])
    assert lister.get_sum() == []

def test_sum_with_duplicates():
    lister = ListSum([1, 1], [1, 1])
    assert lister.get_sum() == [1, 1, 1, 1]

def test_sum_with_mixed_types():
    lister = ListSum([1, "a"], [2.5, True])
    assert lister.get_sum() == [1, "a", 2.5, True]
