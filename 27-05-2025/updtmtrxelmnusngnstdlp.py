# -*- coding: utf-8 -*-
"""
Created on Tue May 27 18:44:17 2025

@author: ritwi
"""

# Update matrix elements using nested loop

matrix = [[1,2], [3,4]]

for row in matrix:
    for i in range(len(row)):
        row[i] += row[i] + 10
        
print(matrix)