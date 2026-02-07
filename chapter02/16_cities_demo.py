def print_cities(*cities: str, sep=", ", end="\n"):
    """
    Print a list of cities with a custom separator and end character.

    Parameters:
    *Cities (str): Cities wich are going to be printed.
    sep (str): Separator between cities. Default is ", ".
    end (str): End character after the last city. Default is "\n".
    """
    if not cities:
        print("No cities provided.", end=end)
    else:
        print("Cities:", sep.join(cities), end=end)

def main():
    print_cities()
    print_cities("New York")
    print_cities("New York", "Los Angeles", "Chicago")
    print("-" * 20)

    print_cities("New York", "Los Angeles", "Chicago", sep=" | ", end=".")
    print("\n" + "-" * 20)

if __name__ == "__main__":
    main()