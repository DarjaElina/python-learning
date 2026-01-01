def super_function(*args, **kwargs):
  print(args) # tuple, (1, 2, 3, 4, 5)
  print(kwargs) # dictionary {'num_1': 5, 'num_2': 10}

  total = 0
  for value in kwargs.values():
    total += value
  return sum(args) + total

print(super_function(1, 2, 3, 4, 5, num_1=5, num_2=10))

# Order:
# 1. Parameters
# 2. *args
# 3. Default parameters
# 4. **kwargs