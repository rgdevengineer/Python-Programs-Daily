# -*- coding: utf-8 -*-
"""
Created on Fri May 30 23:52:41 2025

@author: ritwi
"""

# write a generator function that yields even numbers upto a specific limit

def even_generator(limit):
    for i in range(2, limit + 1, 2):
        yield i
        
for num in even_generator(10):
    print(num)