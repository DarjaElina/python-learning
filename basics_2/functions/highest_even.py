def highest_even(li):
  max_even = None
  for val in li:
    if val % 2 == 0:
      if max_even is None or val > max_even:
        max_even = val
  return max_even

print( highest_even([-9, 4, 2, 4500, 6, 2, 100]))

# Second version

def highest_even(li):
  evens = []
  for item in li:
    if item % 2 == 0:
      evens.append(item)
  return max(evens)

print( highest_even([-9, 4, 2, 4500, 6, 2, 100]))