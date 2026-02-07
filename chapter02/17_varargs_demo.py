def my_average(*numbers: float):
    """
    Docstring for my_average
    
    :param numbers: Description
    :type numbers: float
    """
    if not numbers:
        return "No numbers provided"
    
    average = sum(numbers) / len(numbers)
    return "The average is: {:.2f}".format(average)
    # return "{:.2f}".format(average)

def main():
    nums = [10, 20, 30, 40]

    average = my_average(*nums)

    print(average)

if __name__ == "__main__":
    main()

