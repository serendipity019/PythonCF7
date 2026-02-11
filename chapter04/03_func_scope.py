a = 10
b = 20

def add_numbers(x: int, y: int) -> int:
    x = 100
    return x + y

def main():
    try:
        result = add_numbers(a, b)
        print(f"result: {result}")

        print(f"a: {a}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()