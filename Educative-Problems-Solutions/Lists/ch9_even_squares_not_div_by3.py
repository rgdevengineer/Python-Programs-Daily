
'''
Challenge 9: Even Squares Not Divisible By Three
In this challenge, create a list of even squares that aren't divisible by three.

Problem Statement
Given a getSquare() function, make a list comprehension that returns a list with the squares of all even numbers from 0 to 20, but ignores those numbers that are divisible by 3.

Input
An empty list

Output
A list with the square of all even numbers not divisible by 3.
'''

def getSquare():
  l1 = [i ** 2 for i in range(0, 21) if i % 2 == 0 and i % 3 != 0] 
  return l1