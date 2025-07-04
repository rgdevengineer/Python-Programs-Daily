

import pytest
from area import Solution

@pytest.fixture
def solution():
    return Solution()

def test_valid_triangle_area(solution):
    assert solution.triangleArea(3, 4, 5) == 6.0

def test_triangle_area_with_floats(solution):
    area = solution.triangleArea(7.0, 8.0, 9.0)
    assert round(area, 2) == 26.83

def test_invalid_triangle_raises(solution):
    with pytest.raises(ValueError):
        solution.triangleArea(1, 2, 10)

def test_zero_length_side(solution):
    with pytest.raises(ValueError):
        solution.triangleArea(0, 5, 7)

def test_negative_side(solution):
    with pytest.raises(ValueError):
        solution.triangleArea(-3, 4, 5)
