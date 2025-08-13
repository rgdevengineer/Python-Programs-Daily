
'''
Challenge 5: Inheritance
Solve an exercise on inheritance to brush up on the previous inheritance concepts.

Problem Statement
The code for the Rectangle class is implemented below:

Create a Square class as a ​subclass of Rectangle.

Implement the Square constructor. The constructor should have only the x1, y1 coordinates and the length of a side. Notice which arguments you’ll have to use when you invoke the Rectangle constructor while using super.

The following test cases will calculate the area of the square to check that the Square class correctly inherits attributes and methods from Rectangle.

Input
The coordinates and the length of the square

Output
Area of the square

Sample Input
Square([2, 3, 5])

x1 = 2, y1 = 3, length = 5

Sample Output
Area = 25
'''

class Rectangle:
  def __init__(self, x1, y1, x2, y2): # class constructor
    self.x1 = x1 # class variable
    self.y1 = y1 # class variable
    self.x2 = x2 # class variable
    self.y2 = y2 # class variable
        
  def width(self):
    return self.x2 - self.x1
      
  def height(self):
    return self.y2 - self.y1
  
  def area(self):
    return self.width() * self.height()
  
class Square(Rectangle):
  def __init__(self, x1, y1, length):
    x2 = x1 + length
    y2 = y1 + length
    super().__init__(x1, y1, x2, y2)