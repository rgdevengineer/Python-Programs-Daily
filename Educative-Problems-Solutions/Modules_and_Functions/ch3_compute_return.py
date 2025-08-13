
'''
Challenge 3: Compute & Return Maximum
In this lesson, you are required to compute the maximum of two numbers and return the maximum value.

Problem Statement
Implement the findMaximum function that receives two numbers as arguments x and y and returns the maximum of the numbers.

Input
Two numbers x and y

Output
The maximum of two numbers x and y

Sample Input
x = 2, y = 3

Sample Output
3
'''

def findMaximum(x, y):
  if x > y:
    return x
  else:
    return y
  