import random
import string

# Define a function to generate a random password
def generate_password(length):
    # Define the possible characters for the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a random password by choosing characters from the possible set
    password = ''
    for i in range(length):
        password += random.choice(characters)

    return password

# Prompt the user for the desired password length
length = int(input("Enter the desired password length: "))

# Generate and output the random password
password = generate_password(length)
print(f"Your random password is: {password}")
