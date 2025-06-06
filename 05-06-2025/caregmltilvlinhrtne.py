
# Multi Level Inheritance

class Car:
    @staticmethod
    def start():
        print("Car Started")

    @staticmethod
    def stop():
        print("Car Stopped")

class TataCar(Car):
    def __init__(self, brand):
        self.brand = brand

class Nexon(TataCar):
    def __init__(self, type):
        self.__init__ = type

car1 = Nexon("Disel")
car1.start()        