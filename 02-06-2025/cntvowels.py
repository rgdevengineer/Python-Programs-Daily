# -*- coding: utf-8 -*-
"""
Created on Mon Jun  2 20:44:00 2025

@author: ritwi
"""
# counting vowels in a string

def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

print(count_vowels("Function")) 
