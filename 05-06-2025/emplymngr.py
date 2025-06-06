
# Create a class Employee with a method work().
# Create a subclass Manager that overrides the work() method.

class Employee:
    def work(self):
        print("Employee is working")

class Manager(Employee):
    def work(self):
        print("Manager is managing")

m = Manager()
m.work()
