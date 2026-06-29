# List equality is based on elements and order
print([1, 2, 3] == [1, 2, 3])  # True
print([1, 2, 3] == [2, 3, 1])  # False

# Lists can have any datatypes!
mixed_list = [False, 1, "two", 3.0]
print(mixed_list)

# Checking the type of a list
print(type([1, 2, 3]))  # <class 'list'>


# Defining a function to print list items
def print_list(my_list):
    print(my_list[0])
    print(my_list)


# Calling the function
print_list([1, 2, 3])