import random
import string

print("Welcome to the PyPassword Generator!")

def generate_password(length):
    all_characters = string.ascii_letters + string.digits + string.punctuation
    generated_password = ''.join(random.choices(all_characters, k=length))
    return generated_password

while True:
    try:
        length = int(input("Enter the length of password: "))
        if length <= 0:
            print("Please enter a positive integer.")
            continue
        password = generate_password(length)
        print(f"The generated password is: {password}")
        break
    except ValueError:
        print("Invalid input! Please enter a valid integer.")
