
'''
Challenge 1: Return Even Numbers From 1 to n
Make your own iterator class to return a list of even numbers.

Problem Statement
Print a list of even numbers from 1 to (n). You just need to edit the next method to return all the positive even numbers from 1 to (n). The following test cases will test your code using

myrange = MyRange(n) # n is an integer
print(myrange.next())
Input
A number n

Output
The range of positive even number uptil n

Sample Input
8

Sample Output
[2, 4, 6, 8]
'''

class MyRange:
  def __init__(self, n):
    self.n = n

  def __iter__(self):
    return self

  def next(self):
    evens = []
    for i in range(2, self.n + 1, 2):
      evens.append(i)
    return evens
    
myrange = MyRange(8)
print (myrange.next())