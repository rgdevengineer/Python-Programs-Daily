
'''
Sort each row of a 2D matrix using Bubble Sort.

Input: [[3, 2, 1], [9, 5, 6]]
Output: [[1, 2, 3], [5, 6, 9]]
'''

def bubble_sort_matrix(matrix):
    for row in matrix:
        n = len(row)
        for i in range(n):
            for j in range(n - i - 1):
                if row[j] > row[j + 1]:
                    row[j], row[j + 1] = row[j + 1], row[j]
    return matrix

matrix = [[3, 2, 1], [9, 5, 6]]
print(bubble_sort_matrix(matrix))
