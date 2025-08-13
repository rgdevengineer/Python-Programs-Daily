
'''
Challenge 1: Sublist of a List
In this challenge, you are required to make a sublist from a given list.

Problem Statement
Given a getSublist() function, create a list named l [1, 4, 9, 10, 23]. Using list slicing, get the sublists [1, 4, 9] and [10, 23].

Input
A list

Output
Two sublists
'''

def getSubList():
  l = [1, 4, 9, 10, 23]
  l1 = l[0:3]
  l2 = l[3:5] 
  return [l1, l2]  