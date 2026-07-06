import numpy as np
import matplotlib.pyplot as plt

# A histogram shows the shape of data:
# it splits the range into bins and counts how many values fall in each.
scores = np.random.randint(50, 101, 200)

plt.hist(scores, bins=15)
plt.xlabel("score")
plt.ylabel("how many students")
plt.title("Exam Score Distribution")
plt.show()
