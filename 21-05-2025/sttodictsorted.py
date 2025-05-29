# -*- coding: utf-8 -*-
"""
Created on Wed May 21 20:59:48 2025

@author: ritwi
"""

# set to dictionary and also in sorted order

s = {9,8,7,6,5,4,3,2,1}

dict = {index: value for index, value in enumerate(sorted(s , reverse = True))}

print(dict)

