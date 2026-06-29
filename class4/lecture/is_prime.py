def isPrime(n):
  if n == 1:
    return False
  for factor in range(2, n):
    if n % factor == 0:
      return False
  return True

print(isPrime(7))
print(isPrime(32))
print(isPrime(719))

# What if we want to find all of the primes from 1 to 1000 and print them?
