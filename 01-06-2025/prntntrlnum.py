# -*- coding: utf-8 -*-
"""
Created on Sun Jun  1 23:47:59 2025

@author: ritwi
"""

# Create a function print_natural_numbers that takes an integer n and prints the first n natural numbers.

def print_natural_numbers(number):
    for i in range(1, number+1):
        print(i)
        
print_natural_numbers(10)