
# Modify the Parent and Child classes to call their parent class methods using super()

class Grandparent:
    def show(self):
        print("I am Grnadparent")

class Parent(Grandparent):
    def show(self):
        print("I am parent")
        super().show()
        print("I am Parent")

class Child(Parent):
    def show(self):
        super().show()
        print("I am Child")

c = Child()
c.show()