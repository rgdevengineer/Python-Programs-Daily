
'''
Challenge 8: Sum of Squares of Even Numbers
In this challenge, your task is to create a list of the squares of even numbers.

Problem Statement
Given an evenSquare() function, create a list with the squares of the even numbers from 0 to 20. The final output should be the sum of even numbers in the list:

Input
A list with the square of even numbers from 0-20

Output
The sum of the numbers in the list
'''

def evenSquareSum():
  l1 = [x**2 for x in range(0, 21) if x % 2 == 0]
  return sum(l1)