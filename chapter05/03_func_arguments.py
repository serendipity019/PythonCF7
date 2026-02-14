def test_args_func(pos_arg1, pos_arg2, opt_arg1=None, opt_arg2=None, *args, **kwargs):
    """
    Function to demonstrate the usage of positional, optional, additional (*args) 
    and additional keyword arguments (**kwargs).

    Parameters:
        pos_arg1 (Any): The first positional argument.
        pos_arg2 (Any): The second positional argument.
        opt_arg1 (Any): The first optional argument. Defaults to None.
        opt_arg2 (Any): The second optional argument. Defaults to None.
        *args (Any): Additional positional arguments.
        **kwargs (Any): Additional keyword arguments.  
    """
    # Print possitional arguments
    print("Pos arg1:", pos_arg1)
    print("Pos arg2:", pos_arg2)

    # Print optional arguments
    print("Opt arg1:", opt_arg1)
    print("Opt arg2:", opt_arg2)

    # Print additional pos arguments
    if args:
        print("Additioal pos args:")
        for arg in args:
            print(arg)

    if kwargs:
        print("Additioal keyword args:")
        for key, value in kwargs.items():
            print(f"Key: {key}, Value: {value}")        


def main():
    test_args_func("Hello", "CF7")
    print("-" * 20)

    test_args_func("Hello", "CF7", 100)
    print("-" * 20)

    test_args_func("Hello", "CF7", opt_arg2=100)
    print("-" * 20)
     
    test_args_func("Hello", "CF7", name="Panagiotis", age="38")
    print("-" * 20) 

    test_args_func("Hello", "CF7", # pos_arg1, pos_arg2
                    100, 200, #opt_arg1, opt_arg2
                    300, "Bob", # *args
                    name="Panagiotis", age="38" # **kwargs 
                    )
    print("-" * 20)

if __name__ == "__main__":
    main()