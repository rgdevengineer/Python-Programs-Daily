# -*- coding: utf-8 -*-
"""
Created on Sat May 31 19:20:33 2025

@author: ritwi
"""

# Python program to demonstrate Keyword Arguments

def student(name, roll_no):
    print(name, roll_no)
    

student(name = "Rakesh", roll_no = 12)

student(roll_no = 15, name = "Ramesh")