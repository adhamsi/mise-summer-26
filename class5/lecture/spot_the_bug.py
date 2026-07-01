# Can you spot what is wrong?

N = int(input())
for i in range(1, N + 1):
    containsTwos = False

    while i >= 1:
        if i % 10 == 2:
            containsTwos = True
        i = i // 10       # BUG: modifies i instead of a separate variable!

    if not(containsTwos):
        print(i)          # i is now 0, not the original number
