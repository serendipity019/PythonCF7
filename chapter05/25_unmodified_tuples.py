
def main():
    nums = 1, 2, 3, 4, 5
    print(f"Type of nums: {type(nums)}")

    mixed_tuple = (1, 2, [3, 'CF7'], "Hello")

    try:
        nums[0] = 100
    except TypeError as e:
        print(f"Error: {e}")

    mixed_tuple[2][0] = 300
    print(mixed_tuple)

if __name__ == "__main__":
    main() 