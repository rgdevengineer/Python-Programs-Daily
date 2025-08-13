
'''
Challenge 4: Remove Sublist From List
In this challenge, your task is to remove a sublist from a list.

Problem Statement
Given a removeList() function, create a list named l with the following values:

[1, 4, 9, 10, 23]

Remove the sublist [4, 9] from list l

Input
A list

Output
The updated list after the sublist has been removed

Sample Input
[1, 4, 9, 10, 23]

Sample Output
[1, 10, 23]

'''

def removeList():
  l1 = [1, 4, 9, 10, 23]
  l2 = [4, 9]
  for item in l2:
    if item in l1:
      l1.remove(item)
  return l1
  
result = removeList()
print(result)