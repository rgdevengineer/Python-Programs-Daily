
# Create a base class Animal with a method speak() that prints "Animal speaks".
#  Create a derived class Dog that inherits from Animal and also has a method bark() that prints "Dog barks".

class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

d = Dog()
d.speak()
d.bark()