# -*- coding: utf-8 -*-
"""
Created on Tue Jun  3 19:22:22 2025

@author: ritwi
"""

# Display and find the sum of a list of numbers using while loop

lst = [10,20,30,40,50]

sum = 0
i = 0

while i < len(lst):
    print(lst[i])
    sum += lst[i]
    i += 1
    
print('Sum = ', sum)