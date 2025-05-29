# -*- coding: utf-8 -*-
"""
Created on Wed May 28 18:37:48 2025

@author: ritwi
"""

# delete duplicates from a list

lst = [12,15,15,13,19,21]

lst = list(set(lst))

seen = set()

lst = [x for x in lst if not (x in seen or seen.add(x))]

print(lst)