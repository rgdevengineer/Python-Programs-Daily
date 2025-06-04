
class Student:
    college_name = "ABC COLLEGE"
    def __init__(self):
        print("Adding new student in Database...")

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print("Adding new student in Database..")

s1 = Student("Karan",97)
print(s1.name, s1.marks)

s2 = Student("Arjun",88)
print(s2.name, s2.marks)

print(s2.college_name)