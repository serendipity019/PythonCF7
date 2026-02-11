from typing import Sequence, TypeVar, List, Any, Optional

# A generic type variable
T = TypeVar('T')

Number = TypeVar('Number', int, float)

def first(seq: Sequence[T]) -> T:
    """
    Returns the first element of a sequence.
    If sequence is empty, raises a ValueError.

    Args:
        seq (Sequence[T]): The sequence from which to get the first element.

    Returns:
        T: The first element of the sequence.     
    """
    if not seq:
        raise ValueError("Sequence is empty.")
    return seq[0]

def last(seq: Sequence[T]) -> T:
    """
    Returns the last element of a sequence.
    If sequence is empty, raises a ValueError.

    Args:
        seq (Sequence[T]): The sequence from which to get the last element.

    Returns:
        T: The last element of the sequence.     
    """
    if not seq:
        raise ValueError("Sequence is empty.")
    return seq[-1]

def count_truthy(elements: List[Any]) -> int:
    """
    Counts how many elements in the list are truthy.

    Args:
        elements (List[Any]): A list of elements.

    Returns:
        int: The count of truthy elements in the list.    
    """
    if not isinstance(elements, list):
        raise ValueError("Value error. Please provide a list.")

    if elements:
        # count = 0

        # for elem in elements:
        #     if elem:
        #         count += 1

        # return count
        return sum(1 for elem in elements if elem) # Above mine way. this line teacher's way.  

def len_str(s: Optional[str] = None) -> int:
       return len(s) if s is not None else 0   

def main():
    numbers = [10, 20, 30, 40, 50]
    print(f"First number: {first(numbers)}")
    print(f"Last number: {last(numbers)}")

    try:
        print("First element of []:", first([]))
    except ValueError as e:
        print(e)

    mixed_values = [0, True, False, 'Hello', '', None, 17]
    print("Truthy values are:", count_truthy(mixed_values))

    print("Length of 'Hello World':", len_str("Hello World"))
    print("Length of None:", len_str(None))

    print(first("Hello CF!"))

if __name__ == "__main__":
    main()


