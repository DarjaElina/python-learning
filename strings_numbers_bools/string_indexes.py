kitty = "Kitty"

print(kitty[0])
# print(kitty[10]) # error: out of range

# [start:stop:stepover]

digits = "01234567"
print(digits[0:3]) # 0 index included, 3 index not included

print(digits[0:8:2])

print(digits[1:])

print(digits[:5])

print(digits[::1])

print(digits[-1]) # negative indexes mean: start at the end

print(digits[::-1]) # reverses the string, negative stop = go backwards

# Strings immutability

# Strings in Python are immutable

kitty = "Meow meow"

# we can do:
kitty = "hissssssss"
print(kitty) # prints hissssssss

# but we cannot do:
kitty[0] = '8' # 'str' object does not support item assignment