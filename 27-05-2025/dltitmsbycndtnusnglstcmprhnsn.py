# -*- coding: utf-8 -*-
"""
Created on Tue May 27 23:53:21 2025

@author: ritwi
"""

# Delete Items by Condition Using list comprehension

lst = [12,44,32,67,54,71,88,99]

lst = [x for x in lst if x % 2 != 0]

print(lst)