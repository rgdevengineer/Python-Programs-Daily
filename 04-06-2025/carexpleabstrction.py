
# Abstraction Example

class Car:
    def __init__(self):
        self.acl = False
        self.brk = False
        self.clutch = False

    def start(self):
        self.clutch = True
        self.acl = True
        print("Car Started.....") 

car1 = Car()
car1.start()