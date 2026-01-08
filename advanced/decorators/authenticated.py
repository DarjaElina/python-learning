# Create an @authenticated decorator that only allows the function to run is valid is True
user = {
    'name': 'Anna',
    'valid': True
}

user2 = {
    'name': 'Mike',
    'valid': False
}

def authenticated(fn):
  def wrapper(*args, **kwargs):
    user = args[0]
    if user and user['valid']:
      return fn(*args, **kwargs)
    else:
      print("Invalid user.")
  return wrapper

@authenticated
def message_friends(user):
    print('Message has been sent!')

message_friends(user)