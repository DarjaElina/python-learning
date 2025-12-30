# enumerate() gives you the index and the value automatically

# Use enumerate() when:

# You loop over a list/tuple/etc
# You need both index + value (most common case!)

for i, char in enumerate('Hello New Year Python! 🐍❄️'):
  print(i, char)

# With Tuples
for i, num in enumerate((1, 2, 3)):
  print(i, num)

# with range
for i, num in enumerate(list(range(10))):
  print(i, char)

for i, char in enumerate(list(range(30, 100))):
  if char == 50:
    print(f"Index of 50 is: {i}")