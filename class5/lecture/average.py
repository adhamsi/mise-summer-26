def average(nums):
    total = 0
    for x in nums:
        total = total + x
    return total / len(nums)

print(average([2, 4, 6, 8]))  # 5.0
