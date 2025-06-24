

from check_duplicates import has_duplicates

def test_with_duplicates():
    assert has_duplicates([1, 2, 3, 1]) is True

def test_without_duplicates():
    assert has_duplicates([1, 2, 3, 4]) is False

def test_empty_list():
    assert has_duplicates([]) is False

def test_single_element():
    assert has_duplicates([42]) is False

def test_all_same_elements():
    assert has_duplicates([7, 7, 7]) is True
