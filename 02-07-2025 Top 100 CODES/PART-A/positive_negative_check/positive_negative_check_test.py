
from positive_negative_check import Solution

s = Solution()

def test_positive():
    assert s.checkNumber(10) == "positive"
    assert s.checkNumber(1) == "positive"
    assert s.checkNumber(9999) == "positive"

def test_negative():
    assert s.checkNumber(-1) == "negative"
    assert s.checkNumber(-111) == "negative"
    assert s.checkNumber(-9999) == "negative"

def test_zero():
    assert s.checkNumber(0) == "zero"

def test_edge_cases():
    assert s.checkNumber(-1000000000) == "negative"
    assert s.checkNumber(1000000000) == "positive"

import pytest

def test_non_integer_input():
    with pytest.raises(TypeError):
        s.checkNumber("10")
    with pytest.raises(TypeError):
        s.checkNumber(3.14)
    with pytest.raises(TypeError):
        s.checkNumber(None)
