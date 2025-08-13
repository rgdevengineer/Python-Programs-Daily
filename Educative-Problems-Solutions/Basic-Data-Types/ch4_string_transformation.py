
'''
Challenge 4: String Transformation
This challenge will test your knowledge on string transformation using python.

Problem Statement
Given a getStr() function, write the necessary sequence of operations to transform the string (containing three literals) in such a way that every literal is tripled​ respectively.

Input
A string

Output
Triple of every string literal

Sample Input
abc

Sample Output
aaabbbccc
'''

def getStr(s):
  # strlen = 0
  # result = ''
  # for i in range(0, len(s)):
  #   result += s[i:i+1] * 3
    
  # strlen = len(result)
  # return [s, strlen]
#   return "abc"
# def triple_literals():
#   s = getStr()
#   result = ''.join([char * 3 for char in s])
#   print(result)
# triple_literals
  i = 0
  while i < len(s):
      s = s[:i+1] + s[i] + s[i+1:]
      s = s[:i+1] + s[i] + s[i+1:]
      i += 3  # Move to next original character (tripled now)
  strlen = len(s)
  return [s, strlen]

print(getStr("abc"))