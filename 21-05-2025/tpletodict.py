# -*- coding: utf-8 -*-
"""
Created on Wed May 21 18:17:13 2025

@author: ritwi
"""

# Tuple to Dictionary

t = (6,5,4,3,2,1)

d = {index: value for index, value in enumerate(t)}

print(d)