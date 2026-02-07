def print_cities(*cities: str):
    if not cities:
        print("No cities provided.")
    else:
        print("Cities:", ", ".join(cities))

def main():
    print_cities()
    print_cities("New York")
    print_cities("New York", "Los Angeles", "Chicago")

if __name__ == "__main__":
    main()

