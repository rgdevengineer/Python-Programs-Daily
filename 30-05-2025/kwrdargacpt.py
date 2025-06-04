# -*- coding: utf-8 -*-
"""
Created on Fri May 30 23:45:26 2025

@author: ritwi
"""

# Create a function that accepts any number of keyword arguments and prints them in the format

def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}:{value}")
        
        
print_kwargs(name="Harry Potter", power="Magic")

print_kwargs(name="Harry Porter")

print_kwargs(name="Harry POrter", power="Magic", enemy="Voldemort")


