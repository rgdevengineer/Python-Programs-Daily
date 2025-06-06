
# Create a class Person with a constructor that prints a message. 
# Inherit it into Student class and call the base class constructor using super().

class Person:
    def __init__(self):
        print("Person constructor called")

class Student(Person):
    def __init__(self):
        super().__init__()
        print("Student constructor called")

s = Student()