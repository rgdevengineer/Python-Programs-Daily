# -*- coding: utf-8 -*-
"""
Created on Wed May 21 21:20:02 2025

@author: ritwi
"""

# list to dictionary sorted reverse

l = [9,8,7,6,5,4]

d = {i: value for i, value in enumerate(sorted(l, reverse = False))}

print(d)