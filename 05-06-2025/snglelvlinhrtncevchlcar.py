
# Create a base class Vehicle with a method start_engine(). 
# Create a subclass Car that inherits from Vehicle and adds a method drive().

class Vehicle:
    def start_engine(self):
        print("Engine started")

class Car(Vehicle):
    def drive(self):
        print("Car is driving")

c = Car()
c.start_engine()
c.drive()

