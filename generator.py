import random
import string

def generate_password(length):
# Define the characters to be used in the password (letters, digits, and punctuation)
    characters = string.ascii_letters + string.digits + string.punctuation
# Generate the password by randomly selecting characters of the specified length
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    try:
# Prompt the user to enter the desired length of the password
        length = int(input("Enter the desired length of the password: "))
        if length <= 0:
            print("Please enter a valid length greater than 0.")
            return

# Generate the password
        password = generate_password(length)
        
# Display the generated password on the screen
        print("Generated Password:", password)

    except ValueError:
        print("Please enter a valid integer for the password length.")

if __name__ == "__main__":
# Execute the main function when the script is run
    main()