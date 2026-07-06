import matplotlib.pyplot as plt

x = list(range(10))
y = []
for n in x:
    y.append(n * n)

plt.plot(x, y)
plt.title("Squares of Numbers")
plt.xlabel("number")
plt.ylabel("square")
plt.savefig("plot.png")
