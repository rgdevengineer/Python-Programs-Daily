# -*- coding: utf-8 -*-
"""
Created on Tue May 20 16:55:00 2025

@author: ritwi
"""

num = int(input("Please enter a number = "))

flag = False

if num == 0 or num == 1:
    print(num,"is not a prime number")
   
elif num > 1:
    for i in range(2,num):
        if(num % 2 == 0):
            flag = True
            break
    if flag:
        print("The number is not a prime number")
    else:
        print("The number is a prime number")