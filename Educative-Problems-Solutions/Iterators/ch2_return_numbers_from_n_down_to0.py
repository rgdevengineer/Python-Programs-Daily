
'''
Challenge 2: Return Numbers From n Down to 0
Solve a challenge to iterate through a list in reverse order.

Problem Statement
Edit the following class, such that it returns all numbers from n down to 0.

Input
A number n

Output
The range of numbers from n down to 0

Sample Input
8

Sample Output
[8, 7, 6, 5, 4, 3, 2, 1, 0]
'''

class MyRange:
  def __init__(self, n):
    self.n = n

  def __iter__(self):
    return self

  def next(self):
    return list(range(self.n, -1, -1))
    
myrange = MyRange(8)
print(myrange.next())