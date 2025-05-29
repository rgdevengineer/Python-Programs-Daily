# -*- coding: utf-8 -*-
"""
Created on Mon May 19 19:33:27 2025

@author: ritwi
"""

# Python Program to Check Leap Year

year = int(input("Please enter a year to check = "))

if year % 4 == 0 or year % 400:
    print(f"The year {year} is a leap year")
else:
    print(f"The year {year} is not a leap year")
    