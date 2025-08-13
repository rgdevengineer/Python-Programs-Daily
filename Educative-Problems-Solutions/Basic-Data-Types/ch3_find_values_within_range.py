
'''
Challenge 3: Find Values Within a Range
In this challenge, find if values x and y are within the range.

Problem Statement
Given an inRange(x,y) function, write a method that determines whether a given pair (x, y) falls in the range (x < 1/3 < y). Essentially, you’ll be implementing the body of a function that takes in two numbers x and y and returns True if x < 1/3 < y; otherwise, it returns False.

Input
Two numbers, x and y

Output
True if x and y are in the range and False otherwise.

Sample Input
x = 2, y = 3

Sample Output
False
'''

def inRange(x, y):
  if x < 1/3 < y:
    return True
  else:
    return False
  