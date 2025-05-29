# -*- coding: utf-8 -*-
"""
Created on Mon May 26 22:31:43 2025

@author: ritwi
"""

# matrix operation in nested loop

matrix = [[1,2], [3,4]]

flat = [x for row in matrix for x in row]

print(flat)