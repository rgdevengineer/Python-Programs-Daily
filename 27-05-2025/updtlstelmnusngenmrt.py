# -*- coding: utf-8 -*-
"""
Created on Tue May 27 18:24:44 2025

@author: ritwi
"""

# Update list elements using enumerate

l = [10,20,30,40,50,60]

for idx, value in enumerate(l):
    l[idx] = value + 100

print(l)