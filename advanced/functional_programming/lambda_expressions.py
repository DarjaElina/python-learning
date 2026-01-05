# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.

# lambda param: action(param)

from functools import reduce

my_list = [1, 2, 3, 4]
print(list(map(lambda item: item * 2, my_list)))

print(list(filter(lambda item: item % 2 != 0, my_list)))

print(reduce(lambda acc, item: acc + item, my_list))