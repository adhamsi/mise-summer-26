import numpy as np
import matplotlib.pyplot as plt

# 1. simulate
N = 10000
die1 = np.random.randint(1, 7, N)
die2 = np.random.randint(1, 7, N)
sums = die1 + die2

# 2. summarize
print("mean:", np.mean(sums))
print("std: ", np.std(sums))

# 3. visualize
plt.hist(sums, bins=range(2, 14))
plt.xlabel("sum of two dice")
plt.ylabel("how many rolls")
plt.savefig("plot.png")
