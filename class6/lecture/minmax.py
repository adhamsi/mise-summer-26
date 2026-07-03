def min_max(nums):
    return min(nums), max(nums)   # returns a tuple

lo, hi = min_max([3, 1, 4, 1, 5])
print(lo, hi)    # 1 5
