# -*- coding: utf-8 -*-
"""
Created on Tue Jun  3 21:32:02 2025

@author: ritwi
"""

# write a function which can return another function

def display():
    def message():
        return 'Hello Python'
    return message

fun = display()
print(fun())