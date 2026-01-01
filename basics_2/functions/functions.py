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