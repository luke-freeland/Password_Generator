import string
import random

special_char = "!@#$%^&*()_-"

def generate_password(length):
    chars = string.ascii_letters + string.digits + special_char
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

if __name__ == "__main__":
    password_length = 10
    rand_password = generate_password(password_length)
    print(f"Generated Password: {rand_password}")
