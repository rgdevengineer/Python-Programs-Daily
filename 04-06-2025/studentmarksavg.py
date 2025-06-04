
# create student class that name and marks of 3 subjects as arguments in constructor.
# THEN CREATE A METHOD TO PRINT THE AVERAGE

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("Hi", self.name, "Your average score is:", sum/3)

s1 = Student("Rakesh Ghosh", [99, 98, 97])
s1.get_avg()

s1.name = "RG"
s1.get_avg()

s1.name = "RGhosh"
s1.get_avg()

        