
import pytest
from factorial_calculator import FactorialCalculator

def test_factorial_zero():
    fc = FactorialCalculator(0)
    assert fc.calculate() == 1

def test_factorial_one():
    fc = FactorialCalculator(1)
    assert fc.calculate() == 1

def test_factorial_positive_number():
    fc = FactorialCalculator(5)
    assert fc.calculate() == 120

def test_factorial_large_number():
    fc = FactorialCalculator(10)
    assert fc.calculate() == 3628800

def test_factorial_negative_number():
    fc = FactorialCalculator(-3)
    with pytest.raises(ValueError, match="Factorial is not defined for negative numbers."):
        fc.calculate()
