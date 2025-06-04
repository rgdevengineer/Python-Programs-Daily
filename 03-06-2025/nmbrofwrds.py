# -*- coding: utf-8 -*-
"""
Created on Tue Jun  3 21:09:51 2025

@author: ritwi
"""

# Write a program to find the number of words in a string

str = input('Enter a string: ')

i=c=0

flag = True

for s in str:
    if flag == False and str[i] == ' ':
        c += 1
        
    if str[i] == ' ':
        flag = True
    else:
        flag = False
    i += 1
    
print('No. of words: ', c+1)