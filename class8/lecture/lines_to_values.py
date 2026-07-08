# Every line comes in as a string ending with "\n".
# strip() removes it; int() and float() convert to numbers.
nums = []
with open("numbers.txt") as f:
    for line in f:
        n = int(line.strip())
        nums.append(n)

print(sum(nums))  # 49
