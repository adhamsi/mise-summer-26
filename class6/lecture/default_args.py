# Default arguments: the caller can omit optional parameters
def greet(name, msg="Hello"):
    print(msg + ", " + name)

greet("Alice")        # Hello, Alice
greet("Bob", "Hi")    # Hi, Bob

# Watch out: mutable defaults are created ONCE and reused across calls
def add_item(x, lst=[]):
    lst.append(x)
    return lst

print(add_item(1))  # [1]
print(add_item(2))  # [1, 2]  !! not [2]
print(add_item(3))  # [1, 2, 3]  !!

# Fix: use None as the default, create a fresh object inside the function
def add_item_fixed(x, lst=None):
    if lst is None:
        lst = []
    lst.append(x)
    return lst

print(add_item_fixed(1))  # [1]
print(add_item_fixed(2))  # [2]
