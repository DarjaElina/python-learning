# import utility # a module
from shopping import buy # a package
from utility import multiply, divide

print(divide(10, 5)) # we can access functions from imported files using dot
print(multiply(8, 8))

print(buy("Apple"))

print(print(f"main __name__: {__name__}"))
# no matter how we call our file,
# if we run it directly, the __name__ will be always __main__ 😻

if __name__ == '__main__':
  print("Run it only if it's our main file!")