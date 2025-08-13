
'''
Challenge 6: Lowercase to Uppercase
This challenge tests your knowledge of strings. Your task is to change the letter case of a string.

Problem Statement
Given a function changeCase(s), the task is to convert the strings from upper case to lower case.

Input
A string in upper case

Output
Change case of the string in lower case

Sample Input
“AAA BBB CCC”

Sample Output
“aaa bbb ccc”
'''

def changeCase(s):
  s = 'AAA BBB CCC'
  a = s.upper() # convert string to "AAA BBB CCC"
  b = s.lower() # convert string to "aaa bbb ccc"
  return [a, b]