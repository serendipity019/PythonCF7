print()
print("Hello CF7 friends!")
print("Hello", "CF7 friends!")

print("We haven't overloaded functions in Python like in Java or C#.")
print("But we can use optional parameters to achieve similar results.")

def get_formatted_date(day: int = 1, month: int = 1, year: int = 2000, separator: str = "/") -> str:
    """
    Return a formatted date string in the format DD/MM/YYYY or DD-MM-YYYY etc.
    
    Args:
        day (int): The day of the month. Default is 1.
        month (int): The month of the year. Default is 1.
        year (int): The year. Default is 2000.
        separator (str, optional): The separator to use between date components. Default is "/".
    
    Returns:
        str: A formatted date string.
    """
    return f"{day:02d}{separator}{month:02d}{separator}{year}"

def main():
    print(get_formatted_date())  # Uses all default values
    print(get_formatted_date(15, 8, 2021))  # Uses default separator
    print(get_formatted_date(15, 8, 2021, "-"))  # Uses custom separator
    print(get_formatted_date(10)) # 10/01/2000
    print(get_formatted_date(10, 2)) # 10/02/2000

    #01/01/2025
    print(get_formatted_date(year=2025)) # 01/01/2025
    
    print(get_formatted_date(month=12, day=25, year=2025))

if __name__ == "__main__":
    main()
