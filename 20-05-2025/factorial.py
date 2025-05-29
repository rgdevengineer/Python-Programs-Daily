# -*- coding: utf-8 -*-
"""
Created on Tue May 20 21:27:48 2025

@author: ritwi
"""

# Python Program to Find the Factorial of a Number

#def fact(num):
num = int(input("Please enter a number = "))

fact = 1

for i in range(1, num+1):
    fact = fact * i
print(f"The factorial of {num} = ",fact)