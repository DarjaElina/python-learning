dictionary = {
  123: [1, 2, 3],
  True: "Hello",
  # [1, 2, 3]: 27
}

print(dictionary[123]) # works fine
print(dictionary[True]) # works fine
# print(dictionary[[1, 2, 3]]) # ❌ TypeError: unhashable type: 'list'

# Dictionary keys must be immutable.