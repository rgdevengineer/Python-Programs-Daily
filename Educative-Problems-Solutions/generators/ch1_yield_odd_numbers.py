
'''
Challenge 1: Yield Odd Numbers From 1 to n
Practice your concepts of generators by solving the exercise below.
Problem Statement
Create a generator to yield all the odd numbers from 1 to n.
Input
A number n
Output
All odd numbers from 1 uptil n
Sample Input
8
Sample Output
1, 3, 5, 7
'''

def odd(n):
  i = 1
  while i <= n:
    yield i
    i += 2