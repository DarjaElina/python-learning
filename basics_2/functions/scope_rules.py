# 1. Start with local

a = 1

def confusion():
  a = 5
  return a

print(a) # 1
print(confusion()) # 5

print("==========================")

# 2. Parent local

a = 1

def parent():
  a = 10
  def confusion():
    return a
  return confusion()

print(parent()) # 10
print(a) # 1

print("==========================")

# 3. Global

def confusion():
  return a

print(a) # 1
print(confusion()) # 1

print("==========================")

# 4. Built-in Python functions

a = 1

def confusion():
  return sum

print(confusion()) # <built-in function sum>

