
import pytest
from greatest_of_three import Solution  

s = Solution()

def test_greatest_distinct():
    assert s.greatest(10, 20, 30) == 30
    assert s.greatest(100, 50, 30) == 100
    assert s.greatest(-1, -2, -3) == -1

def test_greatest_with_duplicates():
    assert s.greatest(50, 50, 10) == 50
    assert s.greatest(20, 100, 100) == 100
    assert s.greatest(30, 30, 30) == 30

def test_greatest_with_negatives():
    assert s.greatest(-10, -20, -30) == -10
    assert s.greatest(-5, -5, -10) == -5

def test_greatest_with_mixed_signs():
    assert s.greatest(-10, 0, 10) == 10
    assert s.greatest(-50, 100, 0) == 100

def test_invalid_input():
    with pytest.raises(TypeError):
        s.greatest("10", 20, 30)
    with pytest.raises(TypeError):
        s.greatest(10, None, 5)
