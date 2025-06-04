# -*- coding: utf-8 -*-
"""
Created on Tue Jun  3 20:05:04 2025

@author: ritwi
"""

# write a python program to know whether a sub string exists inmain string or not

str = input("Enter main string: ")
sub = input("Enter sub string: ")

if sub in str:
    print(sub+' is found in main string')
else:
    print(sub+' is not found in main string')