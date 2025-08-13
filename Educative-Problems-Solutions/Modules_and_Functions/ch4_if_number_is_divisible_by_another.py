
'''
Challenge 4: Check If a Number Is Divisible by Another
In this challenge, you are required to check if a number x is divisible by a number y.

Problem Statement
Implement a function named isDivisible that receives two parameters (named x and y) and only returns true if “x” can be divided by “y”(and false otherwise).

A number is divisible by another when the remainder of the division is zero. Use the modulo operator ("%").

Input
Two numbers x and y

Output
Returns true if x is divisible by y and false otherwise

Sample Input
x = 4, y = 2

Sample Output
True
'''

def isDivisible(x, y):
  return x % y == 0
