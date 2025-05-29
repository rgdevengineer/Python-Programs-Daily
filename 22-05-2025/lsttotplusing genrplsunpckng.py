# -*- coding: utf-8 -*-
"""
Created on Thu May 22 20:16:56 2025

@author: ritwi
"""

# list to tuple using generator + unpacking

l = [11,22,33,44,55,66]

gen = (x for x in l)

t = (*l,)

print(t)