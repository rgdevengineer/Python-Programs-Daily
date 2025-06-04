# -*- coding: utf-8 -*-
"""
Created on Fri May 30 20:49:37 2025

@author: ritwi
"""

# create a function that returns both the area and circumference of a circle given its radius

def area(r):
    return 3.14 * r * r

def circumference(r):
    return 2 * 3.14 * r

r = int(input("Please enter the value of the radius = "))

print('Area = ', 3.14 * r * r)

print('Circumference = ', 2 * 3.14 *r)
