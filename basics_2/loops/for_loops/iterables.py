# Iterable - list, dictionary, tuple, set, string
# Iterable can be iterated -> one by one to check each item in the collection

user = {
  'name': 'Steve',
  'age': 22,
  'can_swim': True
}

# we can iterate over dictionary items
# using .items()

for item in user.items():
  print(item)

# iterating over values
for value in user.values():
  print(value)

# iterating over keys
for key in user.keys():
  print(key)

# Tuple unpacking
for item in user.items():
  key, value = item
  print(key, value)

# OR with a shorthand
for key, value in user.items():
  key, value = item