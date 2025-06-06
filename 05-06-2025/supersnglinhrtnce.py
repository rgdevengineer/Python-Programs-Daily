
# Modify the Dog class to use super() to call the parent class method inside its own speak() method.

class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        super().speak()
        print("Dog speaks")

d = Dog()
d.speak()