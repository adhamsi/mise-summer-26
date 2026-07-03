a = [1, 2, 3]
b = a        # same object!

b.append(4)
print(a)     # [1, 2, 3, 4]

c = a.copy()  # new object
c.append(5)
print(a)      # [1, 2, 3, 4]
