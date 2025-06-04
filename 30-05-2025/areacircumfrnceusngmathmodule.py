# -*- coding: utf-8 -*-
"""
Created on Fri May 30 21:08:51 2025

@author: ritwi
"""

# create a function that returns both the area and circumference of a circle given its radius using math module

import math

def circle(radius):
    area = math.pi * radius**2
    circumference = 2 * math.pi * radius
    
    return area, circumference

A, C = circle(3)

print("Area = ", A , "Circumference = ", C)