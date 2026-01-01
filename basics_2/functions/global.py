total = 0

# How do we use global total variable here?
def count():
  global total
  total += 1
  return total

count()
count()
count()
print(total) # 3

# A better way using dependency injection = pass values in instead of grabbing them globally
def count(total):
  total += 1
  return total

for _ in range(3):
    total = count(total)

print(total) # 6