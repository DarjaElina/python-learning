# Tuples are like lists but immutable

my_tuple = (1, 2, 3, 4, 5)

# my_tuple[1] = 100 ❌ 'tuple' object does not support item assignment

print(my_tuple)

print(my_tuple[1]) # 2
print(5 in my_tuple) # True

# Because tuples are immutable, they can be keys in dictionaries

my_dict = {
  (1, 2): [1, 2]
}

print(my_dict[(1, 2)]) # [1, 2]

# slicing a tuple

new_tuple = my_tuple[1:2]
print(new_tuple) # (2,)


# access by index
x = my_tuple[0]
y = my_tuple[1]

print(x, y)

# unpacking
x, y, z, *others = (1, 2, 3, 4, 5)
print(x, y, z, others) # 1 2 3 [4, 5]

# tuple methods

# count() prints how many time item occurs in tuple

print(my_tuple.count(5)) # 1

# index() returns index of an item
print(my_tuple.index(5)) # 4

# len()
print(len(my_tuple)) # 5