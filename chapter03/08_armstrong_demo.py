def is_armstrong_number(num: int) -> bool:
    digits = str(num)
    power = len(digits)
    total = 0

    for digit in digits:
        total += int(digit) ** power
    
    return num == total    

def main():
    try:
        num = int(input("Please insert an integer number: "))
    except ValueError:
        print("Invalid input.")
        return
    
    # if is_armstrong_number(num):
    #     print(f"{num} is Armstrong number")
    # else:
    #     print(f"{num} isn't Armstrong number")

    # ternary operator 
    print(f"{num} is Armstrong number" if is_armstrong_number(num) else f"{num} isn't Armstrong number")   

    # more pythonial
    print(f"{num} {'is' if is_armstrong_number(num) else 'is not'} an Armstrong number") 

if __name__ == "__main__":
    main()
