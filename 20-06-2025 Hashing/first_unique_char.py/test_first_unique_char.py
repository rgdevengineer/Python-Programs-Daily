

from first_unique_char import first_non_repeating_char

def test_basic():
    assert first_non_repeating_char("aabbcd") == 'c'

def test_all_repeating():
    assert first_non_repeating_char("aabbcc") is None

def test_first_unique():
    assert first_non_repeating_char("zabz") == 'a'

def test_empty_string():
    assert first_non_repeating_char("") is None

def test_single_char():
    assert first_non_repeating_char("x") == 'x'
