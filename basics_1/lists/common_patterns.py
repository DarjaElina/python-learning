basket = [1, 2, 3, 4, 5, 6]

# Reverse list with slicing
print(basket[::-1]) # rememeber: negative step means going backwards and we are making a copy
# while .reverse() modifies list in-place

print(basket)
basket.reverse()
print(basket)

# range(start, stop)
print(list(range(1, 100)))

# join()

sentence = '!'
new_sentence = sentence.join(["hi", "my", "name", "is", "Dasha"])

print(new_sentence)

# List Unpacking

a, b, c = [1, 2, 3]
print(a)
print(b)
print(c)

# OR

a, b, c, *others = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(a)
print(b)
print(c)
print(others)