
# Override the speak() method in the Dog class to print "Dog speaks".

class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog speaks")

d = Dog()
d.speak()