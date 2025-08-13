
'''
Challenge 5: Compute nth Fibonacci Number
In this challenge, you are required to compute the nth Fibonacci number.

Problem Statement
Implement the Fibonacci function that takes a number n and calculates the nth Fibonacci.

The Fibonacci Sequence is the series of numbers: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, … The next number is found by adding up the previous two consecutive numbers.

Input
An integer

Output
nth fibonacci term

Sample Input
7

Sample Output
13
'''

def fibonacci(n):
  if n == 0:
    return 0
  elif n == 1:
    return 1
  a, b = 0, 1
  for _ in range(2, n+1):
    a, b = b, a+b
  return b
  