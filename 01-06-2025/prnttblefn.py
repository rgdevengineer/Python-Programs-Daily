# -*- coding: utf-8 -*-
"""
Created on Sun Jun  1 21:28:35 2025

@author: ritwi
"""

# Create a function print_table that takes a number and prints its multiplication table from 1 to 10.

def print_table(number):
    for i in range(1,11):
        print(f"{number} x {i} = {number*i}")
        
print_table(10)
        
