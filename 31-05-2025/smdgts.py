# -*- coding: utf-8 -*-
"""
Created on Mon Jun  2 20:44:00 2025

@author: ritwi
"""
# sum of digits of a number

def sum_of_digits(n):
    return sum(int(d) for d in str(abs(n)))

print(sum_of_digits(12345))  # 15
