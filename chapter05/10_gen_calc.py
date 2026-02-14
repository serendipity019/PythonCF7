def calculator(n1, n2, operation) -> int | str:
    try:
        return operation(n1, n2)
    except TypeError as e:
        print(f"Error: {e}. Ensure the 'operation' argument is a function which takes 2 ints as args")

def add(no1, no2) -> int | float:
    return no1 + no2

def sub(no1, no2) -> int | float:
    return no1 - no2

def mult(no1, no2) -> int | float:
    return no1 * no2

def div(no1, no2) -> int | float | str:
    if no2 != 0:
        return no1 / no2
    elif no1 > 0:
        return "infinity" 
    elif no1 < 0:
        return "negative infinity"
    else:
        return "Division with 0"

def main():
    print("Addition:", calculator(7, 9, add))
    print("Multiplication:", calculator(7, 9, mult))
    print("Division:", calculator(7, 0, div))

if __name__ == "__main__":
    main()