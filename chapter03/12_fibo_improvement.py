def fibonacci(num: int):
    #if num == 0: return 0
    #if num == 1: return 1

    if num in (0, 1): return num # more pythonial than above

    a, b = 0, 1

    for _ in range(2, (num + 1)):
        a, b = b, (a + b)

    return b    

def main():
    try:
        n = int(input("Please insert an integer number: "))
        if n < 0:
            raise ValueError
    except ValueError:
        print("Invalid input. Please insert a positive integer.")
        return
    
    print(f"The {n}th Fibo number is {fibonacci(num=n)}")

if __name__ == "__main__":
    main()