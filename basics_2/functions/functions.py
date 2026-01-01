def say_hello():
  print("HELLO 2026!! 🎊")

say_hello()

# function parameters
def say_hello(name, emoji):
  print(f"HELLO {name}!! {emoji}")

say_hello("NEW 2026 YEAR", "🎆")

# default parameters and keyword arguments

say_hello(name="PYTHON", emoji="❄️")

# default parameters
def say_hello(name="Vecna", emoji="👹"):
  print(f"HELLO {name}!! {emoji}")

say_hello()

# return

def sum(num_1, num_2):
  return num_1 + num_2

print(sum(4, 5))

# if function doesn't return anything, it automatically returns None

# Docstrings

def show_cat(cat):
  '''
  Info: this function prints a cat from paramaters.
  '''
  print(f"Here is the cat: {cat}")

show_cat("🐈")

# help(show_cat) # 👇

# Help on function show_cat in module __main__:

# show_cat(cat)
#     Info: this function prints a cat from paramaters.

print(show_cat.__doc__) # Same

# Clean code
def is_even(num):
  return num % 2 == 0

print(is_even(50))