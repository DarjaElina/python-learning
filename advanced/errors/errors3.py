# What if we do want to stop pur program when there is an error?

while True:
  try:
    num = int(input("Enter a number "))
    raise ValueError("Here is your custom error 🤗")
  finally:
    print("Buy!")
  