import time

def sum_loop(n):
  total = 0
  current = 1
  while current <= n:
    total += current
    current += 1
  return total

def sum_formula(n):
  return n * (n + 1) // 2

# These functions give the same answer, so we expect no output
# from this loop.
for n in range(1, 1000):
  if sum_loop(n) != sum_formula(n):
    print("Not the same answer: " + str(n))

# Try this for large n.
n = int(input())

start_loop = time.time()
sum_loop(n)
end_loop = time.time()

print("Loop: " + str(end_loop - start_loop) + " seconds")

start_sum = time.time()
sum_formula(n)
end_sum = time.time()

print("Formula: " + str(end_sum - start_sum) + " seconds")