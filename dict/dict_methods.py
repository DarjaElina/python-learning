user = {
  'name': "Mary",
  'basket': [1, 2, 3],
  'greeting': "hello"
}

# print(user["age"]) # ❌ KeyError: 'age'


# .get()

print(user.get('age')) # None, but no error!

# We can also add a default value
print(user.get('age', 55)) # IF age doesn't exist, add a default value

# Another way of creating dictionary
user2 = dict(name="Anna")
print(user2)

# in

print('basket' in user) # True
print('grade' in user) # False

# keys()
print('hello' in user.keys()) # False, because it's in values

# values()
print('hello' in user.values())


# items()
print(user.items())

# clear()
user.clear()
print(user)

# copy()

user = {
  'name': "Mary",
  'basket': [1, 2, 3],
  'greeting': "hello",
  "pet": "cat",
  'age': 20,
  
}

user2 = user.copy()
print(user)
print(user2)

# pop()
user.pop('name')
print(user) # {'basket': [1, 2, 3], 'greeting': 'hello'}

# popitem()
user.popitem() # removes the last key:value pair
print(user)

# update()

user.update({'age': 21})
print(user)

user.update({'favorite_food': "pizza"}) # will add a value if it's not already in a list
print(user) # {'basket': [1, 2, 3], 'greeting': 'hello', 'pet': 'cat', 'age': 21, 'favorite_food': 'pizza'}