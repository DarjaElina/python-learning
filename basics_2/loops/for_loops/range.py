print(range(100)) # range(0, 100)

# range() is really useful in for-loops

for number in range(0, 100):
  print(f"Number is {number} ❄️")

# using _ if we don't really care about the variable name here

for _ in range(0, 10):
  print(_)

# Range's 3rd parameter - step
for _ in range(0, 10, 2):
  print(_)

# Negative step means going backwards
for _ in range(10, 0, -1):
  print(_)


# range inside another range
for _ in range(5):
  print(list(range(10)))
