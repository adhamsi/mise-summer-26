operation = input()

first_number = int(input())
second_number = int(input())

if operation == "add" or operation == "Add":
  result = first_number + second_number
  print("The result is: " + str(result))
elif operation == "multiply" or operation == "Multiply":
  result = first_number * second_number
  print("The result is: " + str(result))
elif operation == "subtract" or operation == "Subtract":
  result = first_number - second_number
  print("The result is: " + str(result))
elif operation == "divide" or operation == "Divide":
  result = first_number / second_number
  print("The result is: " + str(result))
else:
  print("You must enter add/...")