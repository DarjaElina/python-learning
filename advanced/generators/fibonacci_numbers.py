def fibonacci_numbers(num):
  a = 0
  b = 1
  for i in range(num):
    yield a
    print(f"a is {a}")
    temp = a
    print(f"temp is {temp}")
    a = b
    print(f"a after reassigning is {a}")
    b = temp + b
    print(f"b is {b}")

for x in fibonacci_numbers(10):
  print(x)

# list example
# def fib_list(num):
#   a = 0
#   b = 1
#   result = []
#   for i in range(num):
#     result.append(a)
#     temp = a
#     a = b
#     b = temp + b
#   return result

# print(fib_list(10))
  
