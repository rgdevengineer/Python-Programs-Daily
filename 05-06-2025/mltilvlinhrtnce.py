
# Create 3 classes: Grandparent, Parent, and Child. 
# Each has a method to print a message. Parent inherits from Grandparent, and Child inherits from Parent.

class Grandparent:
    def show_grandparent(self):
        print("I am Grnadparent")

class Parent(Grandparent):
    def show_parent(self):
        print("I am parent") 

class Child(Parent):
    def show_child(self):
        print("I am Child")

c = Child()
c.show_grandparent()
c.show_parent()
c.show_child()