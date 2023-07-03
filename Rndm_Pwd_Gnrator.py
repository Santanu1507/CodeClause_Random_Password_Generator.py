import random
import string

def generate_password(length=16):
    # Define the character sets for different types of characters
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Ensure at least one character from each set is included
    password = random.choice(lowercase_letters) + random.choice(uppercase_letters) + random.choice(digits) + random.choice(special_characters)

    # Fill the remaining length with random characters from all sets
    password += ''.join(random.choice(lowercase_letters + uppercase_letters + digits + special_characters) for _ in range(length - 4))

    # Shuffle the characters to increase randomness
    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)

    return password

# Generate a random password with default length of 16 characters
password = generate_password()
print("Randomly Generated Password:", password)
