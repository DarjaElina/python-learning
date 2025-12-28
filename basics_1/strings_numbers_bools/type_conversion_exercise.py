from datetime import datetime

# Let's create a program that guesses our age

current_datetime = datetime.now()

birth_year = int(input("What year were your born? "))

print(f"You are {current_datetime.year - birth_year} yo 🎉")