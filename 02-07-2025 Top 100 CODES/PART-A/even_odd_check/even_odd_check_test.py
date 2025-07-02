
from even_odd_check import Solution

s = Solution()

def test_even():
    assert s.checkNumber(10) == "Even"
    assert s.checkNUmber(-20) == "Even"
    assert s.checkNumber(9000) == "Even"

def test_odd():
    assert s.checkNumber(-7) == "Odd"
    assert s.checkNumber(-99) == "Odd"
    assert s.checkNumber(-99999) == "Odd"

# def test_one():
#     assert s.checkNumber(1) == "One"

# def test_zero():
#     assert s.checkNumber(0) == "Zero"

import pytest

def test_even_odd_input():
    with pytest.raises(TypeError):
        s.checkNumber("10")
    with pytest.raises(TypeError):
        s.checkNumber(3.14)
    with pytest.raises(TypeError):
        s.checkNumber(None)