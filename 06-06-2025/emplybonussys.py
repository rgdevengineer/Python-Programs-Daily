
# ou have Employee as base class. Subclasses Manager, Developer, 
# and Intern should return different bonuses using the same method get_bonus().

class Employee:
    def get_bonus(self):
        raise NotImplementedError("Subclasses must implement this method.")

class Manager(Employee):
    def get_bonus(self):
        return 10000

class Developer(Employee):
    def get_bonus(self):
        return 5000

class Intern(Employee):
    def get_bonus(self):
        return 1000

def show_bonus(employee):
    print(f"Bonus: Rs.{employee.get_bonus()}")  # 'Rs.' is safer than '₹'

employees = [Manager(), Developer(), Intern()]

for emp in employees:
    show_bonus(emp)

