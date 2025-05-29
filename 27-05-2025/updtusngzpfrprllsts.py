# -*- coding: utf-8 -*-
"""
Created on Tue May 27 18:59:29 2025

@author: ritwi
"""

# Update using zip for parallel lists

a = [10,20,30,40,50]

b = [100,200,300,400,500]

update = [a+b for a,b in zip(a,b)]

print(update)