amazon_cart = [
  "notebooks",
  "sunglasses",
  "toys",
  "grapes"
]

print(amazon_cart[0:2])

print(amazon_cart[0::2])

# Lists are mutable
amazon_cart[0] = "laptops"
print(amazon_cart)

new_cart = amazon_cart[0:3]
print(new_cart)

another_cart = amazon_cart

print(another_cart)
print(amazon_cart)

another_cart[0] = "catfood"

print(another_cart) # ['catfood', 'sunglasses', 'toys', 'grapes']
print(amazon_cart) # also ['catfood', 'sunglasses', 'toys', 'grapes'] 🤔

# If we want to create a copy, we should use:

yet_another_cart = amazon_cart[:]
yet_another_cart[0] = "toads"

print(yet_another_cart) # ['toads', 'sunglasses', 'toys', 'grapes']
print(amazon_cart) # ['catfood', 'sunglasses', 'toys', 'grapes']