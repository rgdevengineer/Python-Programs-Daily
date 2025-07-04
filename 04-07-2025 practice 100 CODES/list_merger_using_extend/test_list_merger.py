

import pytest
from list_merger import ListMerger

def test_basic_merge():
    merger = ListMerger([1, 2, 3], [4, 5])
    assert merger.merge_lists() == [1, 2, 3, 4, 5]

def test_empty_second_list():
    merger = ListMerger([1, 2, 3], [])
    assert merger.merge_lists() == [1, 2, 3]

def test_empty_first_list():
    merger = ListMerger([], [4, 5])
    assert merger.merge_lists() == [4, 5]

def test_both_empty_lists():
    merger = ListMerger([], [])
    assert merger.merge_lists() == []

def test_merge_with_duplicates():
    merger = ListMerger([1, 2, 2], [2, 3])
    assert merger.merge_lists() == [1, 2, 2, 2, 3]

def test_lists_with_different_types():
    merger = ListMerger([1, "a", 3.5], ["b", 2])
    assert merger.merge_lists() == [1, "a", 3.5, "b", 2]
