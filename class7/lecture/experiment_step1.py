import random

# Rolling two dice once
die1 = random.randint(1, 6)
die2 = random.randint(1, 6)
print(die1 + die2)

# Rolling 100 times and collecting the sums
sums = []
for i in range(100):
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)
    sums.append(d1 + d2)

# How do we make sense of 100 numbers at once?
