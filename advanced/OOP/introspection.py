# Introspection = ability to determine type of an object at runtime

class User():
  def __init__(self, email):
    self.email = email
  
  def sign_in(self):
    print("Logged in.")

class Wizard(User):
  def __init__(self, name, power, email):
    super().__init__(email)
    self.name = name
    self.power = power

wizard = Wizard("Merlin", 50, "merlin@gmail.com")
print(dir(wizard)) # see what we have access to
