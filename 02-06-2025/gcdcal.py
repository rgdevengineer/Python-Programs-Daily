# -*- coding: utf-8 -*-
"""
Created on Mon Jun  2 20:44:00 2025

@author: ritwi
"""
# gcd calculation

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

print(gcd(48, 18))  
