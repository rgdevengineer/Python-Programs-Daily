# -*- coding: utf-8 -*-
"""
Created on Sun Jun  1 18:23:31 2025

@author: ritwi
"""

# Pass by Reference and pass by value

def my_fun(x):
    x[0] = 15
    
lst = [10,20,30,40,50,60,70]

my_fun(lst)

print(lst)