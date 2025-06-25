
from set_matrix_zero import set_zeroes

def test_example_case():
    matrix = [
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1]
    ]
    set_zeroes(matrix)
    assert matrix == [
        [1, 0, 1],
        [0, 0, 0],
        [1, 0, 1]
    ]

def test_all_zeroes():
    matrix = [
        [0, 0],
        [0, 0]
    ]
    set_zeroes(matrix)
    assert matrix == [
        [0, 0],
        [0, 0]
    ]

def test_no_zeroes():
    matrix = [
        [1, 2],
        [3, 4]
    ]
    set_zeroes(matrix)
    assert matrix == [
        [1, 2],
        [3, 4]
    ]

def test_zero_in_corner():
    matrix = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8]
    ]
    set_zeroes(matrix)
    assert matrix == [
        [0, 0, 0],
        [0, 4, 5],
        [0, 7, 8]
    ]

def test_single_row_with_zero():
    matrix = [[1, 0, 3, 4]]
    set_zeroes(matrix)
    assert matrix == [[0, 0, 0, 0]]

def test_single_column_with_zero():
    matrix = [[1], [0], [3], [4]]
    set_zeroes(matrix)
    assert matrix == [[0], [0], [0], [0]]

def test_multiple_zeroes_different_rows_and_columns():
    matrix = [
        [1, 2, 0],
        [4, 5, 6],
        [7, 0, 9]
    ]
    set_zeroes(matrix)
    assert matrix == [
        [0, 0, 0],
        [4, 0, 0],
        [0, 0, 0]
    ]

def test_all_elements_become_zero():
    matrix = [
        [0, 1],
        [2, 3],
        [4, 5]
    ]
    set_zeroes(matrix)
    assert matrix == [
        [0, 0],
        [0, 3],
        [0, 5]
    ]

def test_empty_matrix():
    matrix = []
    set_zeroes(matrix)
    assert matrix == []

def test_matrix_with_one_element_zero():
    matrix = [[0]]
    set_zeroes(matrix)
    assert matrix == [[0]]

def test_matrix_with_one_element_non_zero():
    matrix = [[7]]
    set_zeroes(matrix)
    assert matrix == [[7]]

def test_large_matrix():
    matrix = [
        [1, 2, 3, 4, 0],
        [6, 7, 8, 9, 10],
        [11, 0, 13, 14, 15],
        [16, 17, 18, 19, 20],
    ]
    set_zeroes(matrix)
    assert matrix == [
        [0, 0, 0, 0, 0],
        [6, 0, 8, 9, 0],
        [0, 0, 0, 0, 0],
        [16, 0, 18, 19, 0]
    ]
