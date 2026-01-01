# :=
# 🦭

# Assigns values to variables as part of a larger expression

a = "Helloooooooooo"

if (len(a) > 10):
  print(f"Too long!! :( {len(a)} elements")

# Same with walrus 🦭🦭🦭

a = "Helloooooooooo WALRUS"

if ((n := len(a)) > 10):
  print(f"Too long!! :( {n} elements")

# Another example

while ((n := len(a)) > 0):
  print(n)
  a = a[:-1]