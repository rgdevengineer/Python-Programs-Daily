# -*- coding: utf-8 -*-
"""
Created on Sun Jun  1 23:21:46 2025

@author: ritwi
"""

# Write a function repeat_message that accepts a message and a number n, and prints the message n times.

def repeat_message(message, n):
    for _ in range(n):
        print(message)
        
repeat_message('HELLO PYTHON', 5)