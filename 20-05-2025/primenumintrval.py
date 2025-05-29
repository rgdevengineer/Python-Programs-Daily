# -*- coding: utf-8 -*-
"""
Created on Tue May 20 20:19:54 2025

@author: ritwi
"""

# Python Program to Print all Prime Numbers in an Interval

'''
num = int(input("Please enter a number = "))

flag = False

if num == 0 or num == 1:
    print(f"{num} is not a prime number.")
elif num > 1:
    for i in range(2, num):
        if(num % 2 == 0):
            flag = True
            break
    if flag:
        print("The number is prime.")
    else:
        print("The number is not prime.")

'''

#num = int(input("Please enter a number = "))

lower = int(input("Please enter a lower limit = "))
upper = int(input("Please enter a upper limit = "))

for num in range(lower, upper +1):
    if num > 1:
        for i in range(2, num):
            if(num % 2 == 0):
                break
        else:
            print(num)