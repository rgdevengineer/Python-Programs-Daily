# -*- coding: utf-8 -*-
"""
Created on Mon May 26 18:20:11 2025

@author: ritwi
"""

# Calculating square numbers of the list items in a list

n = int(input("Please enter a number for the range = "))

square = [x**2 for x in range(n)]

print(square)   

