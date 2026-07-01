scores = [[8,  9,  7],
          [6, 10,  8],
          [9,  9, 10]]

totals = []
for row in scores:
    row_sum = 0
    for score in row:
        row_sum += score
    totals.append(row_sum)

print(totals)  # [24, 24, 28]
