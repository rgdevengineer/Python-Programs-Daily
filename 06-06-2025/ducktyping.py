
# Duck Typing (a type of Polymorphism)
#  Demonstrate duck typing with a class that has a code() method.

class PythonDeveloper:
    def code(self):
        print("Writing Python Code....")

class JavaDeveloper:
    def code(self):
        print("Writing Java Code....")

def start_coding(developer):
    developer.code()

dev1 = PythonDeveloper()
dev2 = JavaDeveloper()

start_coding(dev1)
start_coding(dev2)