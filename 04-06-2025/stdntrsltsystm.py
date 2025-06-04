
# Student Result System

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def result(self):
        if self.marks >= 40:
            print(self.name, "Passed")
        else:
            print(self.name, "Failed")

s = Student("Amit", 35)
s.result()