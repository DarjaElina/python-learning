# Using try/except inside a function
def sum(num1, num2):
  try:
    return num1 + num2
  except:
    print("Something went wrong! 😥")

print(sum('1', 2)) # not so useful, because we dont know what exactly went wrong

def sum(num1, num2):
  try:
    print("Calculating...")
    return num1 + num2
  except TypeError as err:
    print(f"Please enter numbers: {err}")
  finally:
    print("Done executing! 🥳")

print(sum('1', 2))

print(sum(10, 2))