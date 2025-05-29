# -*- coding: utf-8 -*-
"""
Created on Tue May 27 21:55:54 2025

@author: ritwi
"""

# update the even position only using function

def update(x):
    return x*2 if x % 2 == 0 else x
    
l = [10,12,23,44,45,67,90]

l = [update(x) for x in l]

print(l)

