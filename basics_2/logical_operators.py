is_magician = input("Are you a magician? (y/n) ")
is_expert = input("Are you an expert? (y/n) ")

is_magician = True if is_magician == "y" else False
is_expert = True if is_expert == "y" else False

# Check if magician AND expert: "You are a master magician. 🧙‍♂️"
# If magician but not expert: "At least you're getting there! 💪"
# If not a magician: "You gonna need some magic powers... 🪄"

if is_magician and is_expert:
  print("You are a master magician. 🧙‍♂️")
elif is_magician and not is_expert:
  print("At least you're getting there! 💪")
elif not is_magician:
  print("You gonna need some magic powers... 🪄")