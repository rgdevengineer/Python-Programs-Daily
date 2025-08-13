
'''
Challenge 7: Lists of Even and Odd Numbers
In this challenge, you are required to create a list containing even and odd numbers.

Problem Statement
Given a ListofEvenOdds() function, create a list comprehension with all the even numbers from 0 to 20, and another one with all the odd numbers.

Input
Two empty lists

Output
List 1 with even numbers

List 2 with odd numbers
'''

def ListofEvenOdds():
  l1 = [i for i in range(0, 21) if i % 2 == 0] # list of even numbers
  l2 = [i for i in range(0, 21) if i % 2 != 0] # list of odd numbers 
  return [l1, l2]
  
# result = ListofEvenOdds()
# print(result)