# -*- coding: utf-8 -*-
"""
Created on Tue Jun  3 20:20:24 2025

@author: ritwi
"""

#  Write a program to know the type of character entered by the user

str = input('Enter a charater: ')
ch = str[0]

if ch.isalnum():
    print('It is alphabetic or numeric character')
    if ch.isalpha():
        print('It is an alphabet')
        if ch.isupper():
            print('It is capital letter')
        else:
            print('It is lowercase letter')
    else:
        print('It is a numeric digit')
elif ch.isspace():
    print('It is a space')
else:
    print('It may be a special character')