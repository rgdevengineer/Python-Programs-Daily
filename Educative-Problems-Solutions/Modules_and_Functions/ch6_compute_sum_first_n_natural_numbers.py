
'''
Challenge 6: Compute Sum of First 'n' Natural Numbers
In this challenge, your task is to compute the sum of the first 'n' natural numbers.

Problem Statement
Implement a sum_N_Numbers recursive function to compute the sum of the n natural numbers (where (n) is a function parameter). Start by thinking about the base case (the sum of the first 1 integers is?) and then think about the recursive case.

Note: Natural Numbers start from 1, i.e., 1, 2, 3, 4, 5, …

Input
A natural number n

Output
The sum of all numbers from 1 upto that input natural number n

Sample Input
7

Sample Output
28
'''

def sum_N_Numbers (n):
  for i in range(1, n+1):
    print(i)
  return sum(range(1, n+1))
  