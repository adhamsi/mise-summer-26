class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(self.name, "says Woof!")

d = Dog("Rex")
d.bark()
# Output: Rex says Woof!
