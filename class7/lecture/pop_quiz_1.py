class Student:
    def __init__(self, name):
        self.name = name

reg = {"id1": Student("Ana")}
print(reg["id1"].name)
# Output: Ana
