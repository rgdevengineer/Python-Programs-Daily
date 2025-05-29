# -*- coding: utf-8 -*-
"""
Created on Tue May 27 11:30:29 2025

@author: ritwi
"""

# update elements based on condition

l = [10,11,12,13,14,9,7]

for i in range(len(l)):
    if l[i] >= 10:
        l[i] = 0
        
print(l)
    