# -*- coding: utf-8 -*-
"""
Created on Tue Jun  3 19:59:39 2025

@author: ritwi
"""

# Access each element of a string in forward and reverse orders using while loop

str = 'Core Python'

n = len(str)
i = 0
while i < n:
    print(str[i],end = ' ')
    i += 1
    
print()

i = -1
while i>=-n:
    print(str[i], end = ' ')
    i -= 1
print()

i = 1
n = len(str)
while i <= n:
    print(str[-i],end = ' ')
    i += 1