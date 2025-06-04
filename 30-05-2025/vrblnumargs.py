# -*- coding: utf-8 -*-
"""
Created on Fri May 30 23:35:49 2025

@author: ritwi
"""

# write a function that takes variable number of arguments and returns their sum

def sum_all(*args):
    print(args)
    
    for i in args:
        print(i * 2)
    
    return sum(args)

print(sum_all(1,2,3))

print(sum_all(1,2,3,4,5,6))

print(sum_all(1,2,3,4,5,6,7,8,9,10))
