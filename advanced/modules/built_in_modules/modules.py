# random

from random import random, randint, choice, shuffle

# help(random) # see documentation

# print(dir(random)) # all available methods

print(random()) # random number between 0 and 1

print(randint(0, 10)) # prints random number between 0 and 10

print(choice([1, 2, 3, 4, 5])) # picks a random from list

print(choice("Hello Python!")) # or from string

my_list = [1, 2, 3, 4, 5, 6, 7]
shuffle(my_list)
print(my_list) # [1, 2, 3, 4, 5, 6, 7]
