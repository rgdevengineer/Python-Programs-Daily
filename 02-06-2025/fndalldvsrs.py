# -*- coding: utf-8 -*-
"""
Created on Mon Jun  2 20:44:00 2025

@author: ritwi
"""

# find all divisiors

def find_divisors(n):
    return [i for i in range(1, n+1) if n % i == 0]

print(find_divisors(12))  
