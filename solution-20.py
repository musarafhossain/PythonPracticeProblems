#20. Create a program that generates a random password of a specified length.
import string
import secrets
def generateRandomPass(length):
    characters = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password
n=int(input("Enter your password length : "))
print("Your random password :",generateRandomPass(n))