

from longest_unique_substring import length_of_longest_substring

def test_example_case():
    assert length_of_longest_substring("abcabcbb") == 3  # "abc"

def test_all_unique():
    assert length_of_longest_substring("abcdef") == 6

def test_all_same():
    assert length_of_longest_substring("aaaaa") == 1

def test_mixed():
    assert length_of_longest_substring("pwwkew") == 3  # "wke"

def test_empty():
    assert length_of_longest_substring("") == 0

def test_numbers_and_symbols():
    assert length_of_longest_substring("123!@#123") == 6  # "123!@#"
