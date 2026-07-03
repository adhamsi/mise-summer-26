# Functions are objects: they can be assigned to variables and stored in lists
f = len
print(f([1, 2, 3]))  # 3

fns = [abs, str, type]
for fn in fns:
    print(fn(-7))
# 7
# -7
# <class 'int'>

# Passing a function as a key to sort/max
nums = [-3, 1, -5, 2]
nums.sort(key=abs)
print(nums)  # [1, 2, -3, -5]

# max with key: find the dict key with the largest value
sales = {"Mon": 45, "Tue": 62, "Wed": 38, "Thu": 71, "Fri": 55}
best = max(sales, key=sales.get)
print(best, sales[best])  # Thu 71
