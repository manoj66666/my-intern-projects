# my-intern-projects

import random
import string

def generate_password(length=12):
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters
    password = [random.choice(lowercase_letters),
                random.choice(uppercase_letters),
                random.choice(digits),
                random.choice(special_characters)]
    for _ in range(length - 4):
        password.append(random.choice(all_characters))
    random.shuffle(password)
    return ''.join(password)
def generate_multiple_passwords(number_of_passwords, password_length=12):
    passwords = [generate_password(password_length) for _ in range(number_of_passwords)]
    return passwords
if __name__ == "__main__":
    num_passwords = int(input("Enter the number of passwords to generate: "))
    password_length = int(input("Enter the length of each password: "))
    generated_passwords = generate_multiple_passwords(num_passwords, password_length)
    for i, password in enumerate(generated_passwords, start=1):
        print(f"Password {i}: {password}")
