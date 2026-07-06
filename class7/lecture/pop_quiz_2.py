import numpy as np

arr = np.array([1, 2, 3, 4])
arr = arr * 2
print(np.mean(arr) + np.max(arr))
# Output: 13.0
# arr * 2 gives [2 4 6 8]; mean is 5.0 and max is 8.
