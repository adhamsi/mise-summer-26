# --- continue Example ---
# Prints: 2, 6, 8

i = 0
while i <= 6:
    i = i + 2
    if i == 4:
        continue  # skip print for i=4
    print(i)


# --- break Example ---
# Prints: 2

i = 0
while i <= 6:
    i = i + 2
    if i == 4:
        break  # exit loop when i=4
    print(i)