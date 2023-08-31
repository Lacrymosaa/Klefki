import bcrypt

password = input("Password: ").encode()

salt = bcrypt.gensalt()

hashed = bcrypt.hashpw(password, salt)

print("Hashed")
print(hashed)
