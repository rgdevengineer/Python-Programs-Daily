# -*- coding: utf-8 -*-
"""
Created on Mon May 26 22:19:46 2025

@author: ritwi
"""

# unzipping the elements

x = [11, 10, 12]

y = ['a', 'b', 'c']

zipped = list(zip(x,y))

unzipped = list(zip(*zipped))

print(unzipped)