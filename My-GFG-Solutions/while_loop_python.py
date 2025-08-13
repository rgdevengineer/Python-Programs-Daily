
'''
While loop in Python

Let's get it more clearly through this question. Given a number x, 
the task is to print the numbers from x to 0 in decreasing order in a single line.

Example:

Input:
x = 3
Output:
3 2 1 0
Explanation:
Numbers in decreasing order from 3
are 3, 2, 1, 0.
Your Task:
This is a function problem. You need to complete the printInDecreasing() function and print the x from x to 0 in a single line.
'''

def printInDecreasing(x):
    while (x >= 0):
        print(x,end=' ')
        x -= 1