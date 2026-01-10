from time import time

def performance(fn):
  def wrapper(*args, **kwargs):
    start = time()
    result = fn(*args, **kwargs)
    end = time()
    print(f"Function took {end - start} s")
    return result
  return wrapper


@performance
def mem_efficient():
  f = 0
  for i in range(10000000):
    f += i * 5


@performance
def not_so_mem_efficient():
  s = 0
  for i in list(range(10000000)):
    s += i * 5

mem_efficient()
not_so_mem_efficient()

# Second experiment

@performance
def mem_efficient():
  for i in range(10000000):
    i * 5


@performance
def not_so_mem_efficient():
  for i in list(range(10000000)):
    i * 5

mem_efficient()
not_so_mem_efficient()