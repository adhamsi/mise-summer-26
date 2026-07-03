# Immutable types: reassignment rebinds the variable; the original is unchanged
a = 42
b = a
b = 99
print(a)   # 42 -- unchanged

s = "hello"
t = s
t = t + "!"
print(s)   # hello -- unchanged

# Mutable objects: mutations through an alias affect the original
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

p1 = Point(1, 2)
p2 = p1       # same object!
p2.x = 99
print(p1.x)   # 99
