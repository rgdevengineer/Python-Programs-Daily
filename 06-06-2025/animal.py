
# Polymorphism with Class Methods
# Write a Python program demonstrating polymorphism 
# where different employee types have their own calculate_salary() method called via a common function.

class FullTimeEmployee:
    def calculate_salary(self):
        return "Full-Time Salary: Rs.50,000/-"

class PartTimeEmployee:
    def calculate_salary(self):
        return "Part-Time Salary: Rs.20,000/-"
    
class Intern:
    def calculate_salary(self):
        return "Intern Salary: Rs.5,000/-"
    
def show_salary(employee):
    print(employee.calculate_salary())

emp1 = FullTimeEmployee()
emp2 = PartTimeEmployee()
emp3 = Intern()

show_salary(emp1)
show_salary(emp2)
show_salary(emp3)