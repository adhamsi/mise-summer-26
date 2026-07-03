# Dictionary basics
pop = {
    "ghana":   31,
    "usa":    330,
    "portugal": 10
}

print(pop["ghana"])    # 31
pop["portugal"] = 11   # update
pop["france"] = 67     # add key
print(len(pop))        # 4

# Iterating
for country, n in pop.items():
    print(country, "->", n)

# Student registry
registry = {1001: "Alice", 1002: "Bob", 1003: "Carol"}
print(registry[1002])    # Bob
registry[1004] = "Dan"
print(len(registry))     # 4

# Best sales day
sales = {"Mon": 45, "Tue": 62, "Wed": 38, "Thu": 71, "Fri": 55}
best = max(sales, key=sales.get)
print(best, sales[best])  # Thu 71
