
# Employee Class with Salary Increment

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def increment(self, percent):
        self.salary += self.salary * (percent / 100)

    def show(self):
        print(f"Employee: {self.name}, Salary: {self.salary}")

emp = Employee("Ravi", 50000)
emp.increment(10)
emp.show()