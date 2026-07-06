import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 1, 3, 5]

# Line plot -- trends and change over time
plt.plot(x, y)
plt.title("Line Plot")
plt.show()

# Scatter plot -- one dot per data point
plt.scatter(x, y)
plt.title("Scatter Plot")
plt.show()

# Bar chart -- comparing amounts across categories
labels = ["A", "B", "C", "D", "E"]
values = [3, 7, 2, 5, 4]
plt.bar(labels, values)
plt.title("Bar Chart")
plt.show()
