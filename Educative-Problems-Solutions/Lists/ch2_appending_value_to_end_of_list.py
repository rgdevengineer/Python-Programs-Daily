
'''
Challenge 2: Appending Value to the End of a List
In this challenge, you are required to append values to the list.

Problem Statement
Given an AppendtoList() function, create a list named l with the following values:

[1, 4, 9, 10, 23]

and appends the number 90 at the end of the list.

Input
A list of numbers

Output
Append the value 90 to the end of the list l

Sample Input
[1, 4, 9, 10, 23]

Sample Output
[1, 4, 9, 10, 23, 90]
'''

def AppendtoList():
  l = [1, 4, 9, 10, 23]
  l.append(90)
  return l