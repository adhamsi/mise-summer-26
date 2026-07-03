# Tuple basics: ordered, immutable sequence
point = (3, 7)
rgb   = (255, 128, 0)

print(point[0])   # 3
print(len(rgb))   # 3

x, y = point      # unpacking
print(x, y)       # 3 7

t = (1, "hi", True)  # mixed types allowed

# Assigning to an element raises a TypeError
# point[0] = 10    # TypeError!

# One-element tuple needs a trailing comma
single = (42,)
print(type(single))   # <class 'tuple'>
print(type((42)))     # <class 'int'>  -- not a tuple!
