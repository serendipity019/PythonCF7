import copy

def main():
    ages = [1 ,[2, 3, 4], 5]

    # Method 1: Shallow copy using list slicing
    ages_slice = ages[:]
    # Method 2: Shallow using copy() of lists
    ages_cp = ages.copy()
    # Method 3: Shallow copy using list() constructor
    ages_list = list(ages)
    # Method 4: Deep copy using 'copy' module
    ages_deep_copy = copy.deepcopy(ages)

    ages[0] = 100 # change a non-nested item
    ages[1][0] = 200# change a nested item

    print(f"ages: {ages}")
    print(f"ages_slice: {ages_slice}")
    print(f"ages_cp: {ages_cp}")
    print(f"ages_list: {ages_list}")
    print(f"ages_deep_copy: {ages_deep_copy}")

if __name__ == "__main__":
    main() 