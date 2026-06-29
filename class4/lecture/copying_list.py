# Integers: b is independent
a = 1
b = a
a = 2
print(b) # 1

# Lists: b = a shares the same list!
a = [1]
b = a; a[0] = 2
print(b) # [2] -- b changed too!

# Reassigning a does not affect b
a = [1]
b = a; a = [2]
print(b) # [1] -- b unchanged