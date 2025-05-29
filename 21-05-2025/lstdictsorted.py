# -*- coding: utf-8 -*-
"""
Created on Wed May 21 21:24:21 2025

@author: ritwi
"""

# list to dictionary using sorted 

l = [9,8,7,6,4,3,1]

d = {i: value for i, value in enumerate(sorted(l, reverse = True))}

print(d)