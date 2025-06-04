# -*- coding: utf-8 -*-
"""
Created on Fri May 30 23:26:45 2025

@author: ritwi
"""

# create a lambda function to compute the cube of a number

cube = lambda x : x ** 3

a = int(input("Please enter a number = "))

print(f'Cube of {a} is = ',cube(a))