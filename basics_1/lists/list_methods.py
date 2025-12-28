basket = [1, 2, 3, 4, 5]

# List length
print(len(basket))

# Adding to list

# append(value)
new_list = basket.append(100)
print(new_list) # None, because append() does not return a new list

basket.append(200)
another_list = basket
print(another_list)


# insert(index, value)
basket.insert(3, 300) # adds 300 to the 3rd index
print(basket)

# extend
basket.extend([100, 101, 102]) # adds 100, 101 and 102 to the end of the list
print(basket)

# Removing from list

# pop()

basket.pop() # removes element from the end of the list
print(basket)

basket.pop(0) # removes element with index 0
print(basket)

# remove(value)
basket.remove(5)
print(basket)

# clear()
basket.clear() # clears the entire list
print(basket)