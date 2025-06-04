
# Rectangle Class (Area & Perimeter)

class Rectangle:
    def __init__(self, ln, br):
        self.length = ln
        self.breadth = br

    def area(self):
        return self.length * self.breadth
    
    def perimeter(self):
        return 2 * (self.length + self.breadth)
    
rect = Rectangle(5, 3)

print("Area = ", rect.area())

print("Perimeter = ", rect.perimeter())