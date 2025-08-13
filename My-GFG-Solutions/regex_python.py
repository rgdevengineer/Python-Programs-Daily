
'''
Regex - Python

Regular expressions are extremely helpful in extracting useful information from loads of text. Regular expressions work on pattern-matching techniques. Extracting phone-number, validating passwords, and extracting images from web-pages are but a few examples of regex usage.

In this question, we'll learn the use of Regex in Python. You will be provided a string str in which you have to find all the numbers and print them.

Note: In Python, you need to import re module to use regex

Example:

Input: 
str = asdasd123asmdasdk34234kfdsd34sdfk5
Output: 
123 34234 34 5
Your Task:
This is a function problem. Do not take any input. just Complete the function numberMatcher() that takes str as input and print numbers in it, If there are no numbers then print -1.

Constraints:
1 <= |str| <= 105
'''

import re
def numberMatcher(str):
    pat=r'\d+'
    match=re.findall(pat,str) ##find all finds all the matched texts and returns a list
    if(match): 
        for i in match:
            print(i, end=" ")
    else:
        print(-1,end="")