def compare_lists(list1: list, list2: list) -> None:
    """ 
    Compares two lists for identity and equality.

    Args:
        list1 (list): The first list to compare.
        list2 (list): The second list to compare.

    Return:
        None        
    """
    # Identity check -> list1 is list2
    print(f"{list1} is {list2}: {list1 is list2}")

    # Equality check -> list1 == list2
    print(f"{list1} == {list2}: {list1 == list2}")

def main():
    first_list = [1, 2, 3]
    second_list = [1, 2, 3]

    third_list = first_list

    #compare lists
    compare_lists(first_list, second_list)
    print(id(first_list))
    print(id(second_list))
    print(id(third_list))

if __name__ == "__main__":
    main()
