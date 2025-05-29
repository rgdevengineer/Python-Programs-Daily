# -*- coding: utf-8 -*-
"""
Created on Mon May 26 18:45:07 2025

@author: ritwi
"""

# Calculating odd numbers of the list items in a list

lst = [12,32,44,90,98,55,75,99,21,33,43]

odd = [x for x in lst if x % 2 != 0]

print(odd)