# -*- coding: utf-8 -*-
"""
Created on Tue May 27 23:14:42 2025

@author: ritwi
"""

# Update Using enumerate() + condition

l = [10,23,34,32,12,41]

for indx, value in enumerate(l):
    if value == 34:
        l[indx] = 90
print(l)