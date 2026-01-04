class User():
  def sign_in(self):
    print("Logged in!")

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

  def check_arrows(self):
    print(f"Arrows: {self.num_of_arrows} remaining!")

  def run(self):
    print("Running really fast!")


# We want HybridBorg to have all the methods from Archer and Wizard
class HybridBorg(Wizard, Archer):
  def __init__(self, name, power, arrows):
    Archer.__init__(self, name, arrows)
    Wizard.__init__(self, name, power)

hb = HybridBorg("Borgie", 100, 200)

hb.run()
print(hb.check_arrows())
print(hb.attack())
print(hb.sign_in())