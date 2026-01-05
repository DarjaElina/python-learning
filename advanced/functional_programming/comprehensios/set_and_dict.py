# Sets
my_set = {char for char in "hello"}
print(my_set)

# Dictionaries
simple_dict = {
  'a': 1,
  'b': 2,
  'c': 3,
  'd': 4,
  'e': 5
}
my_dict = {key: value ** 2 for key, value in simple_dict.items() if value % 2 == 0} # {'b': 4, 'd': 16}
print(my_dict)

my_dict = {str(num): num * 2 for num in [1, 2, 3]} # {'1': 2, '2': 4, '3': 6}
print(my_dict)