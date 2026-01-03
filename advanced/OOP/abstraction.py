class PlayerCharacter:
  def __init__(self, name, age):
    # There is no `private` keyword in Python
    # But we can indicate an internal variable with underscore
    # Saying "please don't touch it" to other devs 😅
    self._name = name