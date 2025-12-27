# Set is an unordered collection of unique objects

my_set = {1, 2, 3, 4, 4, 5, 5, 5}
print(my_set) # {1, 2, 3, 4, 5}, only unique values

my_set.add(100)
print(my_set)

my_list = [1, 1, 2, 2, 3, 3, 3, 4, 5]

my_unique_list = set(my_list)
print(my_unique_list) # {1, 2, 3, 4, 5}

# print(my_set[0]) # ❌ 'set' object is not subscriptable

print(1 in my_set)
print(len(my_set))

# convert to list
print(list(my_set))

# copy a set
new_set = my_set.copy()
print(new_set)

# clear a set
my_set.clear()
print(my_set) # set()