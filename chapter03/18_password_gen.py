import string
import random

# String to list
characters = list(string.ascii_letters + string.digits + "!@#$%^&*")
# print(characters)

def generate_password() -> str:
    """ 
    Generate a random password based on the user-specified length: """
    try:
        password_length = int(input("Give the password length: "))

        if password_length <= 0:
            print("Password length must be a positive number.")
            return
    except ValueError:
        print("Invalid input. Please provide a positive integer number.")  
        return
    
    random.shuffle(characters)

    password = []

    for i in range(password_length):
        password.append(random.choice(characters))

    random.shuffle(password)

    # list to string
    password = "".join(password)

    return password


def main():
    while True:
        option = input("\nDo you want to create a password? ('y' or 'n' for quit.)")

        if option.lower() == 'y':
            password = generate_password()
            print(password)
        elif option.lower() == 'n':
            print("Goodbye!")
            break
        else: 
            print("Wrong input.") 

if __name__ == "__main__":
    main()