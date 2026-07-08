import numpy as np

t = np.array([28, 30, 29, 33])
hot = t[t > 28]
print(len(hot) + np.min(hot))
# Output: 32
# hot is [30 29 33]; len is 3, min is 29.
