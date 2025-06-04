# -*- coding: utf-8 -*-
"""
Created on Sun Jun  1 23:33:33 2025

@author: ritwi
"""

# Write a function simple_calculator that takes two numbers and a string indicating the operation (+ or -) and prints the result.

def simple_calculator(a,b,operation):
    
    if operation == '+':
        result = a+b
        print(f"The sum of {a} and {b} = ", result)
        
    elif operation == '-':
        result = a-b
        print(f"The sum of {a} and {b} = ", result)
    
    else:
        print("Invalid operator used. Please use + or -")
        
simple_calculator(10, 5, '+')

simple_calculator(12, 6, '-')
        
    