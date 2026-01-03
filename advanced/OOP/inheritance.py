class User:
  def sign_in(self):
    print("Logged in.")

class Wizard(User):
  def __init__(self, name, power):
    self.name = name
    self.power = power

  def attack(self):
    print(f"Attacking with power of {self.power}")

class Archer(User):
  def __init__(self, name, num_of_arrows):
    self.name = name
    self.num_of_arrows = num_of_arrows

  def attack(self):
    self.num_of_arrows -= 1
    print(f"Attacking with arrows. Arrows left: {self.num_of_arrows}")

wizard = Wizard("Merlin", 50)
archer = Archer("Legolas", 100)

print(wizard.sign_in())

wizard.attack()
archer.attack()

# isinstance

print(isinstance(wizard, Wizard)) # True
print(isinstance(wizard, User)) # True
print(isinstance(wizard, object)) # True