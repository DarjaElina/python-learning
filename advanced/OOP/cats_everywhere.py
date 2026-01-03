# Given the below class:
class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
mirri = Cat("Mirri", 5)
luna = Cat("Luna", 2)
fluffy = Cat("Fluffy", 10)


# 2 Create a function that finds the oldest cat
def find_oldest_cat(cats):
  oldest = cats[0]
  for cat in cats:
      if cat.age > oldest.age:
          oldest = cat
  return oldest




# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2

oldest_cat = find_oldest_cat([mirri, luna, fluffy])
print(f"The oldest cat is {oldest_cat.age} years old.")