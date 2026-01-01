# Scope - what variables do I have access to?

# Global scope
total = 100

# Function scope
def greet(name):
  greeting = "Hello 💙"
  print(f"{greeting}, {name}")

# print(greeting) ❌ name 'greeting' is not defined

# ‼️ NOT the same with if blocks

if True:
  x = 10

print(x) # ✅ 10