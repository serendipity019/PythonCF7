
def compare_integers(a: int, b: int):
    if a == b:
        print("The numbers are equals.")
    elif a > b:
        print("The first number is greater than the second number.")
    else:
        print("The first number is smaller than the second number.")

def main():
    try:
        a = int(input("Please enter the first integer number: "))
        b = int(input("Please enter the second integer number: "))
    except ValueError:
        print("Invalid input. Please enter an integer")
        return

    compare_integers(a, b)

    # 1. simple example (ternary operator)
    if a > 0:
        print("positive")
    else:
        print("negative")

    result = "positive" if a > 0 else "negative"  # This is the ternary operator
    print(result)
    # print("positive" if a > 0 else "negative"  )  

    # 2. extended example 
    result = (
        "The numbers are equals." if a == b else
        "The first number is greater than the second number." if a > b else 
        "The first number is smaller than the second number."
    )    
    print(result)

if __name__ == "__main__":
    main()