# -*- coding: utf-8 -*-
"""
Created on Fri May 30 23:57:15 2025

@author: ritwi
"""

# create a recursive function to calculate the factorial of a number

def factorial(n):
    if n == 0:
        return 1
    
    else:
        return n * factorial(n-1)