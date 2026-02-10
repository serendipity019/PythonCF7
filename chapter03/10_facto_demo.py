def calculate_factorial(n: int) -> int:
    factorial = 1
    
    for i in range(1, n+1):
        factorial *= i

    return factorial     

def main():
    try:
        n = int(input("Please insert an integer number: "))
        if n < 0:
            raise ValueError
        print(f"The factor of {n}, {n}! is: {calculate_factorial(n)}")
    except ValueError:
        print("Invalid input. Please insert a positive integer.")
        return

if __name__ == "__main__":
    main()