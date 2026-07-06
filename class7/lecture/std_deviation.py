import numpy as np

# Standard deviation measures how spread out values are from the mean.
# Small std: values cluster near the mean.
# Large std: values spread far from it.

a = np.array([9, 10, 10, 11])   # tightly clustered
b = np.array([2, 5, 15, 18])    # spread out

print(np.mean(a), np.std(a))    # 10.0  0.70...
print(np.mean(b), np.std(b))    # 10.0  6.04...
# Same mean, very different spread.
