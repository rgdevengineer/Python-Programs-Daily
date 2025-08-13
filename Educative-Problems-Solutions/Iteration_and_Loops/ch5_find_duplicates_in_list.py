
'''
Challenge 5: Find Duplicates in a List
In this challenge, your task is to find duplicates in a list.

Problem Statement
Implement the hasDuplicates function which verifies if a list has duplicate values.

Input
A list

Output
True if the list has duplicates and False otherwise
'''

def hasDuplicates(list):
  #return len(list) != len(set(list))
  seen = set()
  for item in list:
    if item in seen:
      return True
    seen.add(item)
  return False