# SyntaxError, NameError, IndexError, KeyError, ZeroDivisionError are examples of built-in exceptions in Python

# def gonna_break():
#   my_list = [1, 2, 3, 4, 5]
#   print(my_list[100]) # IndexError: list index out of range 🥲

# gonna_break()

# Error handling allows our script continue running, even if there is an error

print("Height calculator tool")
while True:
  try:
    height = int(input("Input your height "))
    print(f"Your height is {height}cm!")
    10 / height
  except ValueError:
    print("Height calculator tool doesn't know how to convert strings to numbers 😑")
  except ZeroDivisionError:
    print("Height calculator tool will NOT divide by zero. 😠")
  else: break
