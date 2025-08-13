
'''
Challenge 1: Sum Elements of a List
In this challenge, you are required to compute the sum of elements in an array.

Problem Statement
Create a sumList function that receives a list as a parameter and returns the sum of all the elements in the list.

Input
A list

Output
Sum of elements in the list

Sample Input
[1, 2, 3, 4, 5]

Sample Output
15
'''

def sumList(l):
    sum = 0
    for i in l:
        sum = sum + i
    return sum
        