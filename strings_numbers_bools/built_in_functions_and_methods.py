print(len("hello!!!"))

greet = "hellooooo!!"
print(greet[0:len(greet)])

# Python String Methods

quote = "to be or not to be"

print(quote.upper()) # all uppercase

print(quote.capitalize()) # only 1st letter uppercase

print(quote.find("be")) # 3, the first occurence of a string or a character

print(quote.replace("be", "meow"))

print(quote) # to be or not to be, because strings are immutable

quote = quote.replace("be", "meow")

print(quote) # to meow or not to meow, because we reassigned