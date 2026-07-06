import numpy as np

N = 10000
die1 = np.random.randint(1, 7, N)
die2 = np.random.randint(1, 7, N)
sums = die1 + die2

print(sums[:8])
# [ 7  9  5  6  8 11  4  7]   (your output will vary)

# Note: np.random.randint(1, 7, N) produces values 1 through 6.
# The upper bound (7) is excluded -- unlike random.randint(1, 6).
