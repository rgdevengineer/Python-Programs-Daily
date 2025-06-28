
from .regex_utils import extract_numbers, extract_words, is_valid_email  # ← if using as a package

# OR use relative path without dot if run directly:
# from regex_utils import extract_numbers, extract_words, is_valid_email


def test_find_first_index():
    assert find_first_index("banana", "a") == 1
    assert find_first_index("hello", "x") == -1

def test_find_last_index():
    assert find_last_index("banana", "a") == 5
    assert find_last_index("test", "z") == -1

def test_extract_email_domain_valid():
    assert extract_email_domain("user@example.com") == "example.com"
    assert extract_email_domain("abc@xyz.in") == "xyz.in"

def test_extract_email_domain_invalid():
    with pytest.raises(ValueError):
        extract_email_domain("notanemail.com")
    with pytest.raises(ValueError):
        extract_email_domain("wrong@")

def test_extract_after():
    assert extract_after("user@example.com", "@") == "example.com"
    assert extract_after("key:value", ":") == "value"
    assert extract_after("no_delimiter", "#") == ""

def test_extract_before():
    assert extract_before("user@example.com", "@") == "user"
    assert extract_before("key:value", ":") == "key"
    assert extract_before("no_delimiter", "#") == ""
