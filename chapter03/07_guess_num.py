import random

def get_user_guess():
    while True:
        try:
            return int(input("Please give an integer number: "))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            return
        

def check_guess(secret, guess) -> bool:
    if guess == secret:
        print("Bingo! Secret number:", secret)
        return True
    elif abs(secret - guess) <= 5:
        print("Hot")
    else:
        print("cold")
    return False        


def main():
    secret_number = random.randint(1, 20)
    MAX_TRIES = 10
    tries = 0

    while tries < MAX_TRIES:
        guess = get_user_guess()

        if check_guess(secret=secret_number, guess=guess):
            break

        tries += 1

        if tries == MAX_TRIES:
            print("You reached the max number of tries.")

if __name__ == "__main__":
    main()