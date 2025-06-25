
'''
Set Matrix Zeroes
Given an m x n integer matrix, if an element is 0, set its entire row and column to 0 in-place.
Input:
matrix = [
 [1,1,1],
 [1,0,1],
 [1,1,1]
]
Output:
[
 [1,0,1],
 [0,0,0],
 [1,0,1]
]
'''

from typing import List

def set_zeroes(matrix: List[List[int]]) -> None:

    if not matrix or not matrix[0]:
        return
    
    rows = len(matrix)
    cols = len(matrix[0])

    zero_rows = set()
    zero_cols = set()

    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 0:
                zero_rows.add(r)
                zero_cols.add(c)

    for r in zero_rows:
        for c in range(cols):
            matrix[r][c] = 0

    for c in zero_cols:
        for r in range(rows):
            matrix[r][c] = 0