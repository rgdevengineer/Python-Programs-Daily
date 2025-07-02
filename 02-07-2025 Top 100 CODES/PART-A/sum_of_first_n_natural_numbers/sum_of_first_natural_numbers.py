
import pytest
from sum_of_first_n_natural_numbers import Solution  

s = Solution()

def test_natural_number():
    assert s.checkNumber(1) == "Natural Number"
    assert s.checkNumber(10) == "Natural Number"
    assert s.checkNumber(100) == "Natural Number"

def test_not_natural_number():
    assert s.checkNumber(0) == "Not a Natural Number"
    assert s.checkNumber(-5) == "Not a Natural Number"

def test_invalid_input():
    with pytest.raises(TypeError):
        s.checkNumber("5")
    with pytest.raises(TypeError):
        s.checkNumber(5.5)
    with pytest.raises(TypeError):
        s.checkNumber(None)