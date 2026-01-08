# Higher order functions (HOF)

# 1. A function that accepts another function
def greet(func):
  func()

# 2. A function that returns another function
def greet():
  def func():
    return "Hello! 🤍"
  return func

# map(), reduce(), filter() are examples of HOF

# Decorators

# A decorator is a design pattern in Python that allows a user to add new functionality to an existing object without modifying its structure.

# A decorator is a higher-order function, which means that it accepts other functions as arguments and returns a new, enhanced function, method, or class.

def my_decorator(func):
  def wrapper(*args, **kwargs):
    # we can enhance our function here
    print("Enhancing with stars: ✨✨✨✨✨")
    func(*args, **kwargs)
  return wrapper

@my_decorator
def say_hello(greeting):
  print(greeting)

say_hello("Hey friend!")


# How this works under the hood
# say_hello_2 = my_decorator(say_hello)
# say_hello_2()