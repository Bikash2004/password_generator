

import random
import string

def generate_password(length, use_uppercase, use_lowercase, use_digits, use_specials):
    
    # Character pools
    upper = string.ascii_uppercase  # A-Z
    lower = string.ascii_lowercase  # a-z
    digits = string.digits          # 0-9
    specials = string.punctuation   # Special characters like !, @, #

    # Combine pools based on user preferences
    character_pool = ""
    if use_uppercase:
        character_pool += upper
    if use_lowercase:
        character_pool += lower
    if use_digits:
        character_pool += digits
    if use_specials:
        character_pool += specials

    # Ensure at least one character from each selected category is included
    password = []
    if use_uppercase:
        password.append(random.choice(upper))
    if use_lowercase:
        password.append(random.choice(lower))
    if use_digits:
        password.append(random.choice(digits))
    if use_specials:
        password.append(random.choice(specials))

    # Fill the remaining length with random characters from the pool
    if len(password) < length:
        password += random.choices(character_pool, k=length - len(password))

    # Shuffle to avoid predictable patterns
    random.shuffle(password)

    return ''.join(password)

def main():
    """
    Main function to handle user input and generate passwords.
    """
    # Get user preferences
    try:
        length = int(input("Enter the minimum password length: "))
        if length < 4:
            print("Password length must be at least 4 to include all character types.")
            return
        
        use_uppercase = input("Include uppercase letters? (y/n): ").strip().lower() == 'y'
        use_lowercase = input("Include lowercase letters? (y/n): ").strip().lower() == 'y'
        use_digits = input("Include digits? (y/n): ").strip().lower() == 'y'
        use_specials = input("Include special characters? (y/n): ").strip().lower() == 'y'
        num_passwords = int(input("How many passwords would you like to generate? "))

        # Validate at least one character type is selected
        if not (use_uppercase or use_lowercase or use_digits or use_specials):
            print("You must select at least one character type!")
            return

        # Generate and display passwords
        print("\nGenerated Passwords:")
        for i in range(num_passwords):
            print(f"{i + 1}: {generate_password(length, use_uppercase, use_lowercase, use_digits, use_specials)}")

    except ValueError:
        print("Invalid input! Please enter numeric values where required.")

if __name__ == "__main__":
    main()
