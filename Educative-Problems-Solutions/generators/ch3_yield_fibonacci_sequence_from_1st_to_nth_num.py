
'''
Challenge 3: Yield Fibonacci Sequence From 1st to Nth Number
Practice an exercise on generators to return a sequence of fibonacci numbers.

Problem Statement
Create a generator to return the Fibonacci sequence starting from the first element up to n.
The Fibonacci Sequence is the series of numbers in which the next term is found by adding the two previous terms:
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
Here , the number 0 is the first term, 1 is the second term, 1 is the third term and so on…
Input
A number n
Output
The range of fibonacci numbers from 0 to n
Sample Input
8
Sample Output
[0, 1, 1, 2, 3, 5, 8, 13]
'''

def fibonacci(n):
  a, b = 0, 1
  for _ in range(n):
    yield a
    a, b = b, a+b
# n = int(input()) 
# print(list(fibonacci(n)))