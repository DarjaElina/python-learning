def special_for(iterable):
  iterator = iter(iterable)
  while True:
    try:
      print(iterator)
      print(next(iterator))
    except StopIteration:
      break

# special_for([1, 2, 3])

# Note same memory space 👇
# <list_iterator object at 0x100de9b40>
# 1
# <list_iterator object at 0x100de9b40>
# 2
# <list_iterator object at 0x100de9b40>
# 3
# <list_iterator object at 0x100de9b40>

# Create our own range()

class MyGenerator():
  current = 0
  def __init__(self, first, last):
    self.first = first
    self.last = last

  def __iter__(self):
    return self

  def __next__(self):
    if MyGenerator.current < self.last:
      num = MyGenerator.current
      MyGenerator.current += 1
      return num
    raise StopIteration

my_gen = MyGenerator(0, 100)
for i in my_gen:
  print(i)