

from string_utils import compress_string, remove_vowels

def test_compress_string_basic():
    assert compress_string("aaabbcc") == "a3b2c2"

def test_compress_string_single_char():
    assert compress_string("a") == "a1"

def test_compress_string_empty():
    assert compress_string("") == ""

def test_compress_string_no_repeats():
    assert compress_string("abc") == "a1b1c1"

def test_remove_vowels_basic():
    assert remove_vowels("beautiful") == "btfl"

def test_remove_vowels_uppercase():
    assert remove_vowels("AEIOU") == ""

def test_remove_vowels_mixed():
    assert remove_vowels("Python") == "Pythn"

def test_remove_vowels_empty():
    assert remove_vowels("") == ""
