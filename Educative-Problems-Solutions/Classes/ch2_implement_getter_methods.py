
'''
Challenge 2: Implement Getter Methods
This lesson covers a challenge on getter functions and how to create them.

Problem Statement
Implement the width() and height() methods which return, respectively, the width and height of a rectangle. The tests that follow will create two objects—instances of Rectangle to test the calculations.

Input
A class Rectangle with constructor having the rectangle coordinates x1, y1, x2, and y2 respectively

Output
The width and height of the rectangle

Sample Input
x1 = 2, y1 = 7, x2 = 8, y2 = 4

Sample Output
height = 3, width = 6

10 |          
9  |          
8  |          
7  |(2,7) ---6---- (8,7)
6  | |           |
5  3|      r      |
4  |(2,4) ------- (8,4)
3  |          
2  |          
1  |          
0 -+------------------
-1 |          
   0 1 2 3 4 5 6 7 8 9 10
    height = 3
    width = 6
'''

class Rectangle:
  def __init__(self, x1, y1, x2, y2): # class constructor
    if x1 < x2 and y1 > y2:
      self.x1 = x1 # class variable
      self.y1 = y1 # class variable
      self.x2 = x2 # class variable
      self.y2 = y2 # class variable
    else:
      raise ValueError("Incorrect coordinates of the rectangle!")
  
  def width(self):
    return abs(self.x2 - self.x1)
  
  def height(self):
    return abs(self.y1 - self.y2)
  