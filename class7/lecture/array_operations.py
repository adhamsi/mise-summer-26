import numpy as np

arr = np.array([1, 2, 3, 4])

print(arr + 10)      # [11 12 13 14]
print(arr > 2)       # [False False  True  True]
print(arr[arr > 2])  # [3 4]

a = np.array([1, 2, 3])
b = np.array([10, 20, 30])
print(a + b)  # [11 22 33]
