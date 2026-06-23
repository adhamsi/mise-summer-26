def f(x):
    print("In f, x = ", x)
    x += 7
    return x - 1

def h(x):
    x += 3
    return f(x + 4)

x = 5
print(x)
print(f(x))
print(h(x))
print(x)
