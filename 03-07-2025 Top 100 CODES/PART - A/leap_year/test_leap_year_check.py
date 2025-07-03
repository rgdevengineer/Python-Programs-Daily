
import pytest
from leap_year_check import Solution  

s = Solution()

def test_leap_year_true_cases():
    assert s.isLeapYear(2024) is True
    assert s.isLeapYear(2000) is True
    assert s.isLeapYear(1600) is True
    assert s.isLeapYear(2400) is True

def test_leap_year_false_cases():
    assert s.isLeapYear(2023) is False
    assert s.isLeapYear(1900) is False
    assert s.isLeapYear(2100) is False
    assert s.isLeapYear(2021) is False

def test_invalid_year_type():
    with pytest.raises(TypeError):
        s.isLeapYear("2024")
    with pytest.raises(TypeError):
        s.isLeapYear(2024.0)
    with pytest.raises(TypeError):
        s.isLeapYear(None)

def test_invalid_year_value():
    with pytest.raises(ValueError):
        s.isLeapYear(0)
    with pytest.raises(ValueError):
        s.isLeapYear(-400)
