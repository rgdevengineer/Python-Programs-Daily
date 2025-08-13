
'''
Challenge 3: Implement Area and Perimeter Member Methods
Solve an exercise to practice your Python classes, especially the member methods inside a class.

Problem Statement
Implement the area() and perimeter() methods to return the area and perimeter of the rectangle respectively, where

Area=width∗height
Perimeter=2∗width+2∗height

Input
A class Rectangle with constructor having the rectangle coordinates x1, y1, x2, and y2 respectively

Output
The area and perimeter of the rectangle

Sample Input
x1 = 2, y1 = 7, x2 = 5, y2 = 3

Sample Output
Area = 12, Perimeter = 14
'''

class Rectangle:
  def __init__(self, x1, y1, x2, y2): # class constructor
    if x1<x2 and y1>y2:
      self.x1 = x1 # class variable
      self.y1 = y1 # class variable
      self.x2 = x2 # class variable
      self.y2 = y2 # class variable
    else:
      print("Incorrect coordinates of the rectangle!")
        
  def width(self):
    return self.x2-self.x1
      
  def height(self):
    return self.y1-self.y2
  
  def area(self):
    return (self.x2 - self.x1)*(self.y1 - self.y2)
  
  def perimeter(self):
    return 2*((self.x2 - self.x1) + (self.y1 - self.y2))