# -*- coding: utf-8 -*-
"""
Created on Mon May 19 19:37:33 2025

@author: ritwi
"""

# Python Program to Find the Largest Among Three Numbers

a = float(input("Enter the first number = "))
b = float(input("Enter the second number = "))
c = float(input("Enter the third number = "))

if a > b and a > c:
    print(f"The number {a} is the largest number among three numbers")
elif b > c and b > a:
    print(f"The number {b} is the largest number among three numbers")
elif c > a and c > b:
    print(f"The number {c} is the largest number among three numbers")
elif a == b == c:
    print("The three numbers are all same")
    
'''
elif a == b > c:
    print(f"Here two numbers are equal but they are greater than {c}")
elif a == c > b:
    print(f"Here two numbers are equal but they are greater than {b}")
elif b == c > a:
    print(f"Here two numbers are equal but they are greater than {a}")
elif a == b < c:
    print(f"Here two numbers are equal but {c} is greater than them")
elif a == c < b:
    print(f"Here two numbers are equal but {b} is greater than them")
elif b == c < a:
    print(f"Here two numbers are equal but {a} is greater than them")
elif a > b == c:
    print(f"Here two numbers are equal but {a} is the largest number")
'''
    
#else:
#    print("Please take valid numbers")
    
'''
elif a == b != c and c > a:
    print(f"Here {c} is the largest number")
#else:
 #   print("Invalid input")


11 11 3
12 12 15
(a>b)& || 
if 
'''