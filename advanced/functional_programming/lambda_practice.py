# Square
my_list = [1, 2, 3, 4, 5, 6]
print(list(map(lambda item: item ** 2, my_list)))


# Sort list based on 2nd value
tuples = [(0, 2), (4, 3), (9, 9), (10, -1)]
print(sorted(tuples, key=lambda x: x[1]))