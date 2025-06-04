# -*- coding: utf-8 -*-
"""
Created on Mon Jun  2 20:44:00 2025

@author: ritwi
"""
#  Check if Two Strings are Rotations

def is_rotation(str1, str2):
    return len(str1) == len(str2) and str2 in (str1 + str1)

print(is_rotation("abcde", "deabc")) 
