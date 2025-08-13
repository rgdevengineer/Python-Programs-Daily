
'''
Challenge 4: Check If List Is Sorted
In this challenge, check whether a list is sorted or not.

Problem Statement
Make an isSorted function that receives a list as a ​parameter and returns true if the list is sorted in ascending order.

For instance, [1, 2, 2, 3] is ordered while [1, 2, 3, 2] is not.

Input
A list

Output
True if the list is sorted and False otherwise
'''

def isSorted(list):
  if list == sorted(list):
    return True
  else:
    return False