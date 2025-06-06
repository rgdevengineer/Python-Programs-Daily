
# Define a class Shape with a method area(). 
# Create a class Rectangle that inherits from Shape and implements area() to calculate the area of a rectangle.

class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def area(self, length, width):
        return length * width
    
r = Rectangle()
print(r.area(5, 4))