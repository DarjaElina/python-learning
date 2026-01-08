# We are going to create our own decorator that measures the performance of functions

from time import time

def performance(fn):
  def wrapper(*args, **kwargs):
    start_time = time()
    res = fn(*args, **kwargs)
    end_time = time()
    print(f"Function execution took {end_time - start_time} seconds 🐢")
    return res
  return wrapper

@performance
def slow_function():
  for i in range(1000000):
    i ** 100

slow_function()