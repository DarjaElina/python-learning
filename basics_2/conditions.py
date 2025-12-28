is_adult = True
has_license = True

if is_adult:
  print("Your are old enough to drive.")
elif has_license:
  print("You have a license...")
else:
  print("You are not old enough to drive nor you have a license!!")
print("This is not part of `if` block!")

if is_adult and has_license:
  print("You can drive!!! 🎉")

# Note on Truthy and Falsy values

bool("hello") # True
bool(1) # True

bool(0) # False
bool("") # False

password = "12345"
username = "john"

if password and username:
  print("Let's sign you in! :)")