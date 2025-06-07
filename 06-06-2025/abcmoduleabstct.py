
# Define a Shape base class with an area() method.
#  Subclasses like Rectangle, Triangle, and Circle must implement it.
#  Write a function total_area(shapes) to calculate the combined area of multiple shapes.

from math import pi

class Shape:
    def area(self):
        raise NotImplementedError

class Rectangle(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h
    def area(self):
        return self.w * self.h

class Triangle(Shape):
    def __init__(self, b, h):
        self.b = b
        self.h = h
    def area(self):
        return 0.5 * self.b * self.h

class Circle(Shape):
    def __init__(self, r):
        self.r = r
    def area(self):
        return pi * self.r ** 2

def total_area(shapes):
    return sum(shape.area() for shape in shapes)

# Test
shapes = [Rectangle(10, 5), Triangle(4, 3), Circle(3)]
print("Total Area:", total_area(shapes))
