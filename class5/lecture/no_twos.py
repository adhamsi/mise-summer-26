N = int(input())
for i in range(1, N + 1):      # Part I: loop over each number 1 to N
    containsTwos = False
    val = i
    while val >= 1:             # Part II: check each digit
        if val % 10 == 2:
            containsTwos = True
        val = val // 10
    if not(containsTwos):       # Part III: print only if no 2 was found
        print(i)
