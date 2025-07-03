
# test_sum_in_range.py

import pytest
from sum_in_range import Solution  

s = Solution()

def test_sum_in_range_basic():
    assert s.sumInRange(1, 5) == 15       # 1+2+3+4+5
    assert s.sumInRange(3, 6) == 18       # 3+4+5+6
    assert s.sumInRange(10, 10) == 10     # Single number
    assert s.sumInRange(1, 1) == 1        # Single number (smallest)

def test_sum_in_range_large():
    assert s.sumInRange(1, 100) == 5050   # Gauss formula
    assert s.sumInRange(50, 100) == sum(range(50, 101))

def test_sum_in_range_invalid_order():
    with pytest.raises(ValueError):
        s.sumInRange(10, 5)  # left > right

def test_sum_in_range_negative_or_zero():
    with pytest.raises(ValueError):
        s.sumInRange(0, 5)   # left must be ≥ 1
    with pytest.raises(ValueError):
        s.sumInRange(-3, 4)

def test_sum_in_range_type_error():
    with pytest.raises(TypeError):
        s.sumInRange("3", "6")
    with pytest.raises(TypeError):
        s.sumInRange(1.5, 5.5)
