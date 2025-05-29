# -*- coding: utf-8 -*-
"""
Created on Mon May 26 18:54:01 2025

@author: ritwi
"""

# List comprehension in nested loops

n = int(input("Enter the number = "))

nested = [[x*y for x in range(n)] for y in range(n)]

print(nested)

