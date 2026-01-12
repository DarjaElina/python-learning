from random import randint

print("Welcome to the guessing game!")

while True:
  try:
    first = int(input("Give the first number "))
    last = int(input("Give the second number "))

    if first > last:
            print("First number must be smaller than the second one.")
            continue
      
    num = randint(first, last)
    break
  except ValueError:
    print("Please enter valid numbers.")
  

  

while True:
  try:
    guess = int(input("Please enter your guess "))
    if guess == num:
      print("You guessed! Congrats! 🥳🧡")
      break
    else:
      print("No, please try again.")
  except ValueError:
    print("Please enter valid numbers.")
  