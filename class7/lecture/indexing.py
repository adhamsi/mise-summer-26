import numpy as np

arr = np.arange(10, 20)

print(arr[0])    # 10
print(arr[-1])   # 19
print(arr[2:5])  # [12 13 14]

# 2D arrays are indexed as m[row, col]
m = np.array([[1, 2], [3, 4]])
print(m[1, 0])  # 3
