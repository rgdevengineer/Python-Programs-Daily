
# Shape Area

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Square(Shape):
    def area(self):
        return 4 * 4  

class Circle(Shape):
    def area(self):
        return 3.14 * 3 * 3 

def print_area(shape):
    print("Area:", shape.area())

print_area(Square())  
print_area(Circle())  
