def classify(n):
  if n > 0:
    if n % 2 == 0:
      return "positive even"
    else:
      return "positive odd"
  else:
    return "not positive"

print(classify(4)) # positive even
print(classify(7)) # positive odd
print(classify(-3)) # not positive