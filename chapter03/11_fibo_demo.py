def main():
    """ Simple version of Fibonazzi"""
    try:
        n = int(input("Please insert an integer number: "))
    except ValueError:
        print("Invalid input. Please insert a positive integer.")
        return
    
    a = 0
    b = 1

    for i in range(2, n + 1):
        temp = a
        a = b
        b += temp
    
    print(f"The {n}th Fibo number is {b}")

if __name__ == "__main__":
    main()