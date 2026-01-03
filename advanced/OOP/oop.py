# OOP

print(type(None)) # <class 'NoneType'>
print(type(True)) # <class 'bool'>
print(type(5)) # <class 'int'>
print(type(5.5)) # <class 'float'>
print(type("hi")) # <class 'str'>
print(type([])) # <class 'list'>
print(type(())) # <class 'tuple'>
print(type({})) # <class 'dict'>

# Create our own class

# Classes' names should start with capital letter

class MyClass:
  pass

my_obj = MyClass()
print(type(my_obj)) # <class '__main__.MyClass'>

# Creating our own objects

class PlayerCharacter:
  # Class Object Attribute
  # Static, not dynamic ‼️
  membership = True

  # Constructor function
  def __init__(self, name, age):
    # We can use Class Object Attributes here
    if self.membership:
       # Class attributes
      self.name = name
      self.age = age

  def run(self):
    print('Running 🏃')

  def introduce(self):
    print(f"My name is {self.name}")

  def play_dnd(self):
    print("I can play D&D!")

player_1 = PlayerCharacter("Mike", 15)

print(player_1) # <__main__.PlayerCharacter object at 0x104c770e0>

player_1.run()

print(player_1.name)

player_2 = PlayerCharacter("Dustin", 15)

print(player_2.name)
print(player_2.age)

player_1.attack = 50

print(player_1.attack)

# help(player_1)

player_2.introduce()
player_2.play_dnd()