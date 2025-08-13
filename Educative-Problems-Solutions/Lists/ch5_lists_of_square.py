
'''
Challenge 5: List of Squares
Here is the challenge: you are required to create a list containing squares of numbers.

Problem Statement
Given a getSquare() function, create a list with the squares of the first 10 numbers, i.e., in the range from 1-10.

Input
An empty list

Output
An updated list with the square of each value in the list
'''

def getSquare():
  l1 = [i * i for i in range(1,11)] 
  return l1
