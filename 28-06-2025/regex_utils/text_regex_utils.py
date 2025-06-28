

from regex_utils import extract_numbers, extract_words, is_valid_email

def test_extract_numbers():
    assert extract_numbers("I have 2 apples and 34 bananas") == [2, 34]

def test_extract_numbers_empty():
    assert extract_numbers("No digits here!") == []

def test_extract_words():
    assert extract_words("Hello world_123!") == ["Hello", "world_123"]

def test_extract_words_with_numbers():
    assert extract_words("File name is file_2023.txt") == ["File", "name", "is", "file_2023", "txt"]

def test_is_valid_email_valid():
    assert is_valid_email("test.user@example.com") is True

def test_is_valid_email_invalid():
    assert is_valid_email("user@@example..com") is False

def test_is_valid_email_missing_domain():
    assert is_valid_email("someone@") is False

def test_is_valid_email_edge():
    assert is_valid_email("u@d.co") is True
