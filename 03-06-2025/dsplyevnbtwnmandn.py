# -*- coding: utf-8 -*-
"""
Created on Tue Jun  3 18:35:45 2025

@author: ritwi
"""

# dispaly even numbers between m and n

m, n = [int(i) for i in input("Enter minimum and maximum range: ").split(',')]

x = m

if x % 2 != 0:
    x = x+1
    
while x>=m and x<=n:
    print(x)
    x+=2