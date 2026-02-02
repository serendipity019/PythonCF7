items = [1, 2, 3.14, True, "Hello CF7 friends!"]

for item in items:
    print(item, end=" ")
print()

nested_list = [
    [1, 2],
    [3, 4],
    [5, 6]
    ]

# nest_list = [[1, 2], [3, 4], [5, 6]]

print(f"first list item: {nested_list[0]}")

# I want to take from the list above the number 3
print(nested_list[1][0])

# challenge: print the second item and the first item of the nested list
print(f"{nested_list[1]}, {nested_list[0]}")

# challenge for the home. Make the above with slicing
# TODO: Your code here
