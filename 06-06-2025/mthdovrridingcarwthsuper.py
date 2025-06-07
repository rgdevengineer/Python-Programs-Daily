
# Create a base class Vehicle with start() method. 
# Let Car and ElectricCar override it but also call the parent method using super().

class Vehicle:
    def start(self):
        print("Vehicle starting...")

class Car(Vehicle):
    def start(self):
        super().start()
        print("Car engine started.")

class ElectricCar(Car):
    def start(self):
        super().start()
        print("Electric motor is now running.")

ev = ElectricCar()
ev.start()
