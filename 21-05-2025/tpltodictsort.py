# -*- coding: utf-8 -*-
"""
Created on Wed May 21 21:12:26 2025

@author: ritwi
"""

# tuple to dictionary sorted

t = (9,8,7,6,5,4,3)

d = {i: value for i,value in enumerate(sorted(t, reverse = True))}

print(d)

