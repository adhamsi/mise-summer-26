# Set basics
l = [1, 2, 1, 1, 2, 3]
S = set(l)      # {1, 2, 3}
print(S)

print(2 in S)   # True
S.add(11)
S.remove(2)
print(len(S))   # 3

# Count unique values
nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
unique = set(nums)
print(len(unique))  # 7
