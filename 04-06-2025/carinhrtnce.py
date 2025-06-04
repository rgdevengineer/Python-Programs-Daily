
# Car Inheritance 

class Car:
    @staticmethod
    def start():
        print("Car Started...")
    
    @staticmethod
    def stop():
        print("Car stopped.")

class TataCar(Car):
    def __init__(self, name):
        self.name = name

car1 = TataCar("Curvv")
car2 = TataCar("Punch")

print(car1.start())
