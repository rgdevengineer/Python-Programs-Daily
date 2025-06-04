# -*- coding: utf-8 -*-
"""
Created on Sun Jun  1 23:42:08 2025

@author: ritwi
"""

# Define a function check_number_type that takes a number and prints whether it's positive, negative, or zero

def check_number_type(number):
    
    if number > 0:
        print('The number is positive')
    
    elif number < 0:
        print('The number is negative')
        
    else:
        print('The number is zero')
        
check_number_type(12)
check_number_type(-14)
check_number_type(0)