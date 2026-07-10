n = int(input("Enter the max value for n: ")) # Range is 1 .. n

lo, hi = 1, n

number_of_tries = 0
while lo <= hi:
  number_of_tries += 1

  mid = (lo + hi) // 2
  
  print("Guess: " + str(mid))
  
  user_response = input("Say higher/lower/right: ")

  if user_response == "higher":
    lo = mid + 1
  elif user_response == "lower":
    hi = mid - 1
  else:
    print("Solved in " + str(number_of_tries) + " tries!")
    break