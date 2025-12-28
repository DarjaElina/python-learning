username = input("Enter your username: ")
password = input("Enter your password: ")

password_length = len(password)

secured_password = '*' * password_length

print(f"Hey {username}, your password {secured_password} is {password_length} letters long")