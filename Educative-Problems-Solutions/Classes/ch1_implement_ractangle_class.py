
'''
Challenge 1: Implement a Rectangle Class
This lesson covers a basic exercise on classes and constructors.

Problem Statement
Implement a class named Rectangle to store the coordinates of a rectangle given the top-left corner (x1, y1) and the bottom-right corner (x2, y2).

Implement the class constructor with the parameters (x1, y1, x2, y2) and store them in the class instance using the self keyword.

Input
Given a class Rectangle

Output
Implement the class constructor and output if the rectangle can be created with the given the coordinates.

Sample Input
x1 = 2, y1 = 7, x2 = 8, y2 = 4

Sample Output
Rectangle(2, 7, 8, 4) created

10 |          
  |          
8 |  (2,7)       
  | +-----+  
6 | |     |  
  | |  r  |  
4 | +-----+(8,4) 
  |          
2 |          
  |          
 0-+----------
  |          
  0   2   4   6   8   1

r = Rectangle (2, 7, 8, 4)
Output:
Rectangle(2, 7, 8, 4) created
'''

class Rectangle:
  def __init__(self, x1, y1, x2, y2):
    self.x1 = x1
    self.y1 = y1
    self.x2 = x2
    self.y2 = y2
    
  def rectangle(self):
    print(f"Rectangle({self.x1}, {self.y1}, {self.x2}, {self.y2}) created")
    