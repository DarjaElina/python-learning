# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

my_list = [char for char in "Hello Python!"]

print(my_list) # ['H', 'e', 'l', 'l', 'o', ' ', 'P', 'y', 't', 'h', 'o', 'n', '!']

my_nums = [(num * 2) for num in range(0, 10)]

print(my_nums)

# Keep only even numbers
evens = [(num ** 2) for num in range(0, 10) if num % 2 == 0]
print(evens)