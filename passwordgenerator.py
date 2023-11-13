# Password Generator

import random
import string

def generate_password(length):
    if length < 8:
        print("Length should be at least 8 characters for a strong password.")
        return None
    
    # Generating a password
    password_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(password_characters) for i in range(length))
    return password

def main():
    while True:
        # Asking user to specify length of the password
        length = input("Enter the desired password length (or type 'quit' to exit): ")
        
        if length.lower() == 'quit':
            break
        
        # Convert the length to an integer and generate the password
        try:
            length = int(length)
            password = generate_password(length)
            
            if password is not None:
                print("Generated password: ", password)
            else:
                print("Invalid input. Please enter a number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()