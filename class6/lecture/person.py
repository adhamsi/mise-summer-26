# Simple class with a class-level attribute and a method
class Person:
    name = ""

    def greet(self):
        print("Hello!")

p = Person()
p.name = "Pedro"
print(p.name)   # Pedro
p.greet()       # Hello!

# Better: using __init__ so each object gets its own data
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello! My name is", self.name)

p = Person("Pedro")
p.greet()       # Hello! My name is Pedro
