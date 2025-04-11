import random
import string
length=int(input("enter the lenth of the password you want "))
def generate_password(length):

    all_characters = string.ascii_letters + string.digits

    password = ''.join(random.choice(all_characters) for _ in range(length))

    return password

password = generate_password(length)
print("Generated password:", password)