import numpy as np

g = np.array([80, 85, 90, 95])
print(np.mean(g))    # 87.5
print(np.median(g))  # 87.5

g[3] = 400           # replace one grade with an extreme outlier
print(np.mean(g))    # 163.75 -- pulled far by the outlier
print(np.median(g))  # 87.5   -- barely moves
