# -*- coding: utf-8 -*-
"""
Created on Tue May 27 23:21:26 2025

@author: ritwi
"""

# Bulk Update with External Data

l = [10,43,56,78,90,31,37]

indices = [0, 2]
new_vals = [100, 300]

for indx,vals in zip(indices, new_vals):
    l[indx] = vals

print(l)