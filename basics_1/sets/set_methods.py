# .difference()
# .discard()
# .difference_update()
# .intersection()
# .isdisjoint()
# .issubset()
# .issuperset()
# .union()

my_set = {1, 2, 3, 4, 5}
your_set = {4, 5, 6, 7, 8, 9, 10}

# .difference()
print(my_set.difference(your_set)) # {1, 2, 3}

# discard() removes element from set if it's a member
my_set.discard(1)
print(my_set) # {2, 3, 4, 5}

# .difference_update() removes all elements of another set from this set
my_set = {1, 2, 3, 4, 5}
your_set = {4, 5, 6, 7, 8, 9, 10}
my_set.difference_update(your_set)
print(my_set) # {1, 2, 3}

# .intersection() returns common items in 2 sets
my_set = {1, 2, 3, 4, 5}
your_set = {4, 5, 6, 7, 8, 9, 10}
print(my_set.intersection(your_set))
# shorthand
print(my_set & your_set)

# .isdisjoint() method returns True if none of the items are present in both sets, otherwise it returns False
print(my_set.isdisjoint(your_set)) # False

# .union() unifies 2 sets
print(my_set.union(your_set)) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# shorthand
print(my_set | your_set) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

# .issubset() checks if set is part of another set
my_set = {4, 5}
print(my_set.issubset(your_set)) # True

# .issuperset() checks if set includes another set
my_set = {1, 2, 3, 4, 5}
your_set = {2, 5}
print(my_set.issuperset(your_set)) # True
print(my_set.issuperset({10, 90, 2})) # False

