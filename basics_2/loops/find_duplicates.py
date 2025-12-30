letters = ['a', 'b', 'c', 'b', 'm', 'n', 'n']

seen = set()

duplicates = set()

for letter in letters:
  if letter in seen:
    duplicates.add(letter)
  else:
    seen.add(letter)

print(list(duplicates))


# letters = ['a', 'b', 'c', 'b', 'm', 'n', 'n']

# duplicates = []

# for letter in letters:
#   if letters.count(letter) > 1:
#     if letter not in duplicates:
#       duplicates.append(letter)
  
  
# print(duplicates)