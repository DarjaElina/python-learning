print(type("Hello Python!"))

username = "supercoder"
password = "supersecret"
long_string = '''
WOW
REALLY IMPRESSIVE

0 0
___
'''

print(long_string)

first_name = "Dasha"
last_name = "Elina"
full_name = first_name + " " + last_name

print(full_name)

# String concatenation = adding string together
print("Hello " + "Python " + "🐍")


# Type conversion
print(type(str(100)))

# Escape Sequence

# weather = 'It's sunny' # bad

weather = 'It\'s \'kinda\' sunny \n hope you have a good day! \t🐍'
print(weather)

# Formatted Strings

name = "Dasha"
age = 27

print(f"Hi {name} you are {age} yo")
print("hi {} you are {} yo".format("Mary", 18))

print("hi {} you are {} yo".format(name, age))

print("hi {1} you are {0} yo".format(age, name))

print("hi {new_name} you are {age} yo".format(new_name="Dustin", age=15))