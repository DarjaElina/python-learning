class User():
  def __init__(self, email):
    self.email = email
  
  def sign_in(self):
    print("Logged in.")

class Wizard(User):
  def __init__(self, name, power, email):
    User.__init__(self, email)
    self.name = name
    self.power = power

wizard = Wizard("Merlin", 50, "merlin@gmail.com")
print(wizard.email)


# Same with `super` keyword

class User():
  def __init__(self, email):
    self.email = email
  
  def sign_in(self):
    print("Logged in.")

class Wizard(User):
  def __init__(self, name, power, email):
    # Note how we don't need to use `self` anymore
    # so our code looks cleaner
    super().__init__(email)
    self.name = name
    self.power = power

wizard = Wizard("Merlin", 50, "merlin@gmail.com")
print(wizard.email)