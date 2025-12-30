# break

my_list = [1, 2, 3, 4, 5]
for item in my_list:
  print(item)
  if item == 3:
    break

i = 0
while i < len(my_list):
  print(my_list[i])
  i += 1
  if i == 3:
    break

# continue

# The continue keyword is used to end the current iteration in a for loop (or a while loop),
# and continues to the next iteration.

for item in my_list:
  print(item)
  if item == 3:
    continue

# pass

# A pass statement signals to a loop that there is “no code to execute here.”
# It's a placeholder for future code. 

for item in my_list:
  # empty loop would give an error so we can use pass
  pass
