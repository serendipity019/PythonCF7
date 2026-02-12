def add(a: int, b: int = 20, c: int = 30 ) -> int: # Here the a, is positional value, and the other are optional with default value
    return a + b + c

def full_opt_add(a: int, b: int = 0, c: int = 0 ) -> int: # Optional with default values
    return a + b + c


def main():
    print(add(10, 20))
    print(add(10, 50))
    print(add(10, c=20))

    print(full_opt_add(3, 10, 4))
    print(full_opt_add(c=3, a=10, b=4))

if __name__ == "__main__":
    main()