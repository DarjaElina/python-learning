class Toy():
  def __init__(self, color, age):
    self.color = color
    self.age = age
    self.my_dict = {
      'name': "Beth",
      "plays_chess": True
    }

  # Customizing dunder methods
  def __str__(self):
    return self.color

  def __len__(self):
    return 0

  # ⚠️ We should avoid using __del__ in real life
  # and rely on Python's garbage collector
  def __del__(self):
    print("Deleted!")

  def __call__(self):
    return "Yes, friend?"

  def __getitem__(self, i):
    return self.my_dict[i]


action_figure = Toy('red', 0)
print(action_figure.__str__())
print(str(action_figure))

print(len(action_figure))

# del action_figure

print(action_figure())

print(action_figure['name']) # Beth 🤯