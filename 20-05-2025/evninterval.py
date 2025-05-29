# -*- coding: utf-8 -*-
"""
Created on Tue May 20 21:21:11 2025

@author: ritwi
"""

# even and odd numbers printing in an interval

lower = int(input("Please enter lower limit = "))
upper = int(input("Please enter upper limit = "))

for num in range(lower, upper+1):
    if(num % 2 != 0):
        print(num + 2)
'''       
for num in range(lower, upper+1):
    if(num % 2 == 0):
        print(num)
        '''