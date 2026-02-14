import functools

def calculate(args: int) -> int| float | str:
    def plus():
        """ Return the sum of the numbers"""
        return functools.reduce(lambda x, y: x + y, args)
    
    def minus():
        return functools.reduce(lambda x, y: x - y, args)
    
    def mult():
        return functools.reduce(lambda x, y: x * y, args)
    
    def div():
        if not 0 in args[1:]:
            return functools.reduce(lambda x, y: x / y, args)
        else: return "divide with 0"
    
    return plus, minus, mult, div

def main():
    list_of_ints = [26, 5, 4, 3, 2, 1]

    plus_func, minus_func, mul_func, div_func = calculate(list_of_ints)

    print(f"The sum of the list is: {plus_func()}")
    print(f"The abstract of the list is: {minus_func()}")
    print(f"The multiplication of the list is: {mul_func()}")
    print(f"The division of the list is: {div_func()}")

if __name__ == "__main__":
    main()
