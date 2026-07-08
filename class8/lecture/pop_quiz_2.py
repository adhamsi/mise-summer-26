words = ["mango", "kiwi", "mango",
         "fig", "kiwi", "mango"]
counts = {}
for w in words:
    counts[w] = counts.get(w, 0) + 1
print(counts["mango"] - counts["fig"])
# Output: 2
# "mango" appears 3 times, "fig" once: 3 - 1 = 2
