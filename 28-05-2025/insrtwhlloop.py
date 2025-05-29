# -*- coding: utf-8 -*-
"""
Created on Wed May 28 20:56:47 2025

@author: ritwi
"""

# insert while loop

lst = [10,12,14,16]

for i, val in enumerate(lst[:]):
    if val == 12:
        lst.insert(i+1, 90)

print(lst)