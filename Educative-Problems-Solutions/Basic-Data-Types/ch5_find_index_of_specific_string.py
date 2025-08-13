
'''
Challenge 5: Find Index of a Specific Value in a String
In this challenge, find the index of the desired value in a string.

Problem Statement
Given a string, use a findOccurence(s) function that allows you to find the first occurrences of "b" and "ccc"​ in the string.

Input
A string

Output
The first occurrence of “b” and “ccc” in the string

Sample Input
aaabbbccc

Sample Output
[3, 6]
'''

def findOccurence(s):
  index_b = s.find('b')
  index_ccc = s.find('ccc')
  return [index_b, index_ccc]
input_string = "aaabbbccc"
result = findOccurence(input_string)
print(result)