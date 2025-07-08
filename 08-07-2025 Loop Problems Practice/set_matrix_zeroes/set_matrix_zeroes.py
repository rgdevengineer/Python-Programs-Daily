
'''
Set Matrix Zeroes
Given an m x n integer matrix, if an element is 0, set its entire row and column to 0. Do it in-place.
'''

def setZeroes(matrix):
    if not matrix or not matrix[0]:
        return
    
    m, n = len(matrix), len(matrix[0])

    first_row_has_zero = False
    first_col_has_zero = False

    for col in range(n):
        if matrix[0][col] == 0:
            first_row_has_zero = True
            break
    
    for row in range(m):
        if matrix[row][0] == 0:
            first_col_has_zero = True
            break

    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0

    if first_row_has_zero:
        for col in range(n):
            matrix[0][col] = 0

    if first_col_has_zero:
        for row in range(m):
            matrix[row][0] = 0