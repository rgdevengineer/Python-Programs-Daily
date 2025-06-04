# -*- coding: utf-8 -*-
"""
Created on Mon Jun  2 20:44:00 2025

@author: ritwi
"""

# checking a string palindrome or not

def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome("madam")) 
