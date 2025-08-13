
'''
Challenge 2: Yield Numbers From n Down to 0
Practice an exercise on generators to return all numbers from n to 0 in descending order.
Problem Statement
Implement a generator reverse(n) that returns All numbers from n down to 0.
Input
A number n
Output
All numbers from n down to 0.
Sample Input
8
Sample Output
8, 7, 6, 5, 4, 3, 2, 1, 0
'''

def reverse(n):
  i = n
  while i >= 0:
    yield i
    i -= 1
# for num in reverse(8):
#   print(num, end=", ")