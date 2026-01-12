# from random import randint

# print("Welcome to the guessing game!")

# while True:
#   try:
#     first = int(input("Give the first number "))
#     last = int(input("Give the second number "))

#     if first > last:
#             print("First number must be smaller than the second one.")
#             continue
      
#     num = randint(first, last)
#     break
#   except ValueError:
#     print("Please enter valid numbers.")
  

  

# while True:
#   try:
#     guess = int(input("Please enter your guess "))
#     if guess == num:
#       print("You guessed! Congrats! 🥳🧡")
#       break
#     else:
#       print("No, please try again.")
#   except ValueError:
#     print("Please enter valid numbers.")
  
  # Version with sys module

import sys
from random import randint

num = randint(int(sys.argv[1]), int(sys.argv[2]))

while True:
  try:
    guess = int(input("Guess a number that falls between two you just chose: "))
    if num == guess:
      print("You guessed! Congrats! 🥳🧡")
      break
  except ValueError:
    print("Please enter a number")
    continue