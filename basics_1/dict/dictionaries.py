# Python dictionary is a data structure that stores the value in key: value pairs.
# Values in a dictionary can be of any data type and can be duplicated.

dictionary = {
  'a': [1, 2, 3],
  'b': "Hello",
  'c': True,
  'd': 10
}

print(dictionary['b']) # Hello

# print(dictionary['x']) # KeyError: 'x'

print(dictionary['a'][1]) # 2

my_list = [
  {
    'a': [1, 2, 3],
    'b': "Hello",
    'c': True,
    'd': 10
  },
   {
    'a': [4, 5, 6],
    'b': "World",
    'c': False,
    'd': 100
  }
]

print(my_list[0]['a'][2]) # 3