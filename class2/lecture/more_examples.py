def f(x, y, z):      # 3 arguments and a return value
    return x + y + z

print(f(1, 3, 2))   # Prints 6
# print(f(1, 2))    # WRONG! Needs 3 arguments


def g():             # No arguments, with a return value
    return 42

print(g())           # Prints 42


def hi_goodbye(x, y):   # 2 arguments, no return value (void)
    print("hi" * x)
    print()
    print("goodbye" * y)

hi_goodbye(2, 5)
hi_goodbye(3, 1)
