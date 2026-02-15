def fibo():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
        

def main():
    fib = fibo()

    for i in range(6):
        print(f"Fibo {i} = {next(fib)}")
        
    print(next(fib))

    for i in range(7, 11):
        print(f"Fib {i} = {next(fib)}")

    print(next(fib))
    print(next(fib))

    for num in fib:
        if num >= 1000:
            break
        print(num)

    fib = fibo()
    fibo_list = []
    for _ in range(15):
        fibo_list.append(next(fib))
    print(fibo_list)    

    # second way
    fib = fibo()
    new_fibo_list = [next(fib) for _ in range(15)]
    print(new_fibo_list)

if __name__ == "__main__":
    main() 