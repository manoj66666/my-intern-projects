import random
import string

def generate_password(length=12):
    # Define character sets for the password
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Combine character sets to create the full character pool
    characters = lowercase_letters + uppercase_letters + digits + special_characters

    # Ensure the password contains at least one character from each character set
    password = (
        random.choice(lowercase_letters) +
        random.choice(uppercase_letters) +
        random.choice(digits) +
        random.choice(special_characters)
    )

    # Generate the remaining characters in the password
    for _ in range(length - 4):
        password += random.choice(characters)

    # Shuffle the password to make it more random
    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)

    return password

def generate_passwords(num_passwords, length=12):
    passwords = [generate_password(length) for _ in range(num_passwords)]
    return passwords

if __name__ == "__main__":
    num_passwords = int(input("Enter the number of passwords to generate: "))
    password_length = int(input("Enter the length of each password: "))

    generated_passwords = generate_passwords(num_passwords, password_length)

    for i, password in enumerate(generated_passwords, start=1):
        print(f"Password {i}: {password}")
