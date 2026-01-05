# map, filter, zip and reduce

# map()

my_list = [1, 2, 3]
def multiply_by_2(item):
  return item * 2

print(list(map(multiply_by_2, my_list))) # [2, 4, 6]

print(my_list) # [1, 2, 3], map() doesn't modify the original list, but creates a copy

# filter()

def is_odd(num):
  return num % 2 != 0

my_list = [4, 2, 7, -10, 5, 3, 2]

print(list(filter(is_odd, my_list))) # [7, 5, 3]

# zip()

my_list = [1, 2, 3]
your_list = [10, 20, 30]

print(list(zip(my_list, your_list))) # [(1, 10), (2, 20), (3, 30)]

# reduce()

from functools import reduce

def accumulator(acc, curr):
  return acc + curr


print(reduce(accumulator, my_list, 0)) # 6