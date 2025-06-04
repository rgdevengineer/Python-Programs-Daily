# -*- coding: utf-8 -*-
"""
Created on Mon Jun  2 20:44:00 2025

@author: ritwi
"""
# check armstrong numbers

def is_armstrong(n):
    digits = [int(x) for x in str(n)]
    power = len(digits)
    return n == sum(d**power for d in digits)

print(is_armstrong(153))  
