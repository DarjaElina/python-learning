# We can create class methods with the @classmethod decorator and use them for operations that involve class-level data.
# We use static methods for utility functionality that doesn't need class or instance data, and we can create them with the @staticmethod decorator.

class MyClass:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  
  # Because add() is a class method, we need to pass `class` as a 1st argument
  @classmethod
  def add(cls, num1, num2):
    return num1 + num2

  # We can instantiate objects inside class methods
  @classmethod
  def multiply(cls, num1, num2):
    return cls('Tommy', num1 * num2)

  @staticmethod
  def subtract(num1, num2):
    return num1 - num2

    

my_obj = MyClass("Mike", 20)

print(my_obj.add(1, 2))

# We can use @classmethod without instantiating a class 👇
print(MyClass.add(10, 29))

print(MyClass.multiply(3, 10).name)