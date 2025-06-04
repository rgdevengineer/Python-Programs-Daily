# -*- coding: utf-8 -*-
"""
Created on Mon Jun  2 20:44:00 2025

@author: ritwi
"""

# Create a function check_divisibility that checks if a number is divisible by both 5 and 7.

def check_divisibility(number):
    if number % 5 == 0 and number % 7 == 0:
        return True
    else:
        return False
        
num = int(input("Please enter a number = "))

if check_divisibility(num):
    print("The number is divisible by 5 and 7")
else:
    print("The number is not divisible by 5 and 7")