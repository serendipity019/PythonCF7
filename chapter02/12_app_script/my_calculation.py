
num1 = 100

def my_add_function(n: int, m: int):
    return n + m

def main():
    print("Value of num1:", num1)
    result = my_add_function(50, num1)
    print(f"result: {result}")
    print(__name__)

if __name__ == "__main__":
    main()