# Index

basket = ["cat", "dog", "fish", "bird"]
print(basket.index("fish")) # 2


# print(basket.index("fish", 0, 1)) # error! 'fish' is not in list

# How do we avoid this?

if "fish" in basket[:1]:
  print(basket.index("fish", 0, 1))
else:
  print("no fish :(")


# We can also do `in` for strings

print('i' in "Hiiiiiii")
print("l" in "kitty")

# Count, counts how many time value occurs in a list

print(basket.count("fish"))

# Sort, sorts the list in-place

basket = [9, 4, 2, 5, 7]
basket.sort()
print(basket)

basket = [9, 4, 2, 5, 7]
print(sorted(basket))

# remember: sort() modify array in-place while sorted() creates a copy of it

# copy()

new_basket = basket.copy()
print(new_basket)

# reverse()

basket.reverse()
print(basket)