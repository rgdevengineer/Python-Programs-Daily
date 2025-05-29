# -*- coding: utf-8 -*-
"""
Created on Mon May 26 18:35:35 2025

@author: ritwi
"""

# Calculating evens numbers of the list items in a list

lst = [12,14,56,73,23,22,90,98,12,14,16]

evens = [x for x in lst if x % 2 == 0]

print(evens)