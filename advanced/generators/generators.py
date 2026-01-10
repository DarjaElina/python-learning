# A generator function is a special type of function that returns an iterator object. Instead of using return to send back a single value, generator functions use yield to produce a series of results over time. The function pauses its execution after yield, maintaining its state between iterations.

range(100) # range is a lazy iterable, not a generator, but it behaves similarly to one
# for i in range(100) → values generated on the fly, one by one

# Creating our own generator

def my_generator(num):
  for i in range(num):
    yield i

# for item in my_generator(100):
#   print(item)

g = my_generator(5)
print(next(g)) # 0
print(next(g)) # 1
print(next(g)) # 2
print(next(g)) # 3
print(next(g)) # StopIteration
# print(next(g)) # ❌ StopIteration