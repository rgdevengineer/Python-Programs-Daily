
'''
Challenge 2: Check Parity of a Number
In this challenge, you have to calculate the parity of a number.

Parity is a term to express if a given integer is even or odd.

Problem Statement
Given a checkParity(n) function, write code to determine if a given number n is even or odd. Think of this as a function that returns 0 if the number is even, and 1 if it is odd. You have been given some starter code where the function and return statement have already been written, so don’t worry about any Python-specific details about functions; just implement the function logic!

Input
A number

Output
The parity of the number

Sample Input
4

Sample Output
0
'''

def checkParity(n):
  if n % 2 == 0:
    return 0
  elif n % 2 != 0:
    return 1
  
  