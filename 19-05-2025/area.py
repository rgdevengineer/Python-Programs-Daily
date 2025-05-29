# -*- coding: utf-8 -*-
"""
Created on Mon May 19 16:34:57 2025

@author: ritwi
"""

a = float(input("Enter the first base of the triangle = "))
b = float(input("Enter the first base of the triangle = "))
c = float(input("Enter the first base of the triangle = "))

s = (a+b+c)/2

area = (s*(s-a)*(s-b)*(s-c))**0.5

print(area)