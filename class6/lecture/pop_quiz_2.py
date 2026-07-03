d = {"a": 1, "b": 2, "c": 3}
d["b"] = 20
d["d"] = 4
total = 0
for v in d.values():
    total += v
print(total)
# Output: 28
# After updating "b" to 20 and adding "d": 4,
# values are 1, 20, 3, 4 -- sum is 28
