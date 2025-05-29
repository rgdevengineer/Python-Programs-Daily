# -*- coding: utf-8 -*-
"""
Created on Wed May 21 18:04:23 2025

@author: ritwi
"""

# List to Dictionary

x = [1,2,3,4,5,6]

y = {index: value for index, value in enumerate(x)}

print(y)