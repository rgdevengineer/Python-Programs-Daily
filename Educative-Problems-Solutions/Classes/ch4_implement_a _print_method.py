
'''
Challenge 4: Implement a Print Method
In this exercise, you will modify the rectangle class such that the print method actually prints values instead of addresses.

Problem Statement
Implement a function in the Rectangle class __str__ method, such that when you print one of the objects using the print() command, it prints the coordinates as x1, y1, x2, y2.

For instance, the code

rectangle = Rectangle(2, 3, 5, 7)
print(rectangle)
should print

2, 3, 5, 7
Input
A class Rectangle with constructor having the rectangle coordinates x1, y1, x2, and y2 respectively

Output
Print the coordinates of the rectangle

Sample Input
x1 = 2, y1 = 3, x2 = 5, y2 = 7

Sample Output
2, 3, 5, 7
'''

class Rectangle:
  def __init__(self, x1, y1, x2, y2): # class constructor
    self.x1 = x1 # class variable
    self.y1 = y1 # class variable
    self.x2 = x2 # class variable
    self.y2 = y2 # class variable        
    
    print(f"{self.x1}, {self.y1}, {self.x2}, {self.y2}")