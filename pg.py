import random
import string

def generate_password(length=12, include_uppercase=True, include_lowercase=True, include_numbers=True, include_special_chars=True):
    if length < 1:
        raise ValueError("Password length must be at least 1.")

    character_pools = []
    if include_uppercase:
        character_pools.append(string.ascii_uppercase)
    if include_lowercase:
        character_pools.append(string.ascii_lowercase)
    if include_numbers:
        character_pools.append(string.digits)
    if include_special_chars:
        character_pools.append(string.punctuation)

    if not character_pools:
        raise ValueError("At least one character type must be included.")

    password = [random.choice(pool) for pool in character_pools]

    all_characters = ''.join(character_pools)
    password += [random.choice(all_characters) for _ in range(length - len(password))]

    random.shuffle(password)

    return ''.join(password)

try:
    length = int(input("Enter the desired password length: "))
    include_uppercase = input("Include uppercase letters? (y/n): ").strip().lower() == 'y'
    include_lowercase = input("Include lowercase letters? (y/n): ").strip().lower() == 'y'
    include_numbers = input("Include numbers? (y/n): ").strip().lower() == 'y'
    include_special_chars = input("Include special characters? (y/n): ").strip().lower() == 'y'

    password = generate_password(length, include_uppercase, include_lowercase, include_numbers, include_special_chars)
    print(f"Generated password: {password}")

except ValueError as e:
    print(f"Error: {e}")
