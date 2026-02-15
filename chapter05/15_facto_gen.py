def facto():
    n, result = 0, 1
    while True:
        yield result
        n += 1
        result *= n
        

def main():
    factorial = facto()

    for i in range(6):
        print(f"{i}! = {next(factorial)}")
        
    print(next(factorial))

    for i in range(8, 11):
        print(f"{i}! = {next(factorial)}")

    print(next(factorial))
    print(next(factorial))

if __name__ == "__main__":
    main() 