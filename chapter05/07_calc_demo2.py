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
    
    return {
        "add" : plus, 
        "subtract" : minus, 
        "multiply" : mult, 
        "division" : div 
    }

def main():
    list_of_ints = [26, 5, 4, 3, 2, 1]

    operations = calculate(list_of_ints)

    while True:
        print("\nChoose an operation")
        print("1. Addition")
        print("2. Substraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")
        try:
            choice = int(input("Please enter a number between 1 and 5: "))
        except ValueError:
            print("Invalid input.")
            continue
        match choice:
            case 1:
                print(f"\nThe sum of the numbers is: {operations["add"]()}")
            case 2:
                print(f"\nThe subtract of the numbers is: {operations["subtract"]()}")
            case 3:
                print(f"\nThe multiplication of the numbers is: {operations["multiply"]()}")
            case 4:
                print(f"\nThe division of the numbers is: {operations["division"]()}")
            case 5:
                print("\nGoodbye")
                break
            case _:
                print("\nInvalid input. Please try again!")


    
    
    
    

if __name__ == "__main__":
    main()
