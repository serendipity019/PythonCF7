# List of fruits
fruits = ["Apple", "Banana", "Cherry", "Apple"]   

print(f"Initial fruits list: {fruits}")

# Adding an item to the end of the list
fruits.append("Orange")
print(f"After appending Orange: {fruits}")

# Adding two items to the end of the list
fruits.extend(["Grapes", "Mango"])
print(f"After extending with Grapes and Mango: {fruits}")

# Inserting an item at a specific position
fruits.insert(1, "Coconut")
print(f"After inserting Coconut at position 1: {fruits}")

# Update an item at a specific position (here the first element)
fruits[0] = "Melon"
print(f"After updating first item to Melon: {fruits}")

# Update a part of list (two elements)
fruits[1:3] = ["Pineapple", "Kiwi", "Papaya"]
print(f"After slicing: {fruits}")

# pop()
removed_item = fruits.pop() # removes the last item
print(f"Removed item: {removed_item}")
print(f"List after popping: {fruits}")
removed_item_at_index = fruits.pop(2) # removes item at index 2
print(f"Removed item at index 2: {removed_item_at_index}")
print(f"List after popping index 2: {fruits}")

# remove 
fruits.remove("Apple") # removes the first occurrence of "Apple"
print(f"List after removing Apple: {fruits}")

''' fruits.remove("Dog") # removes Dog from the list 
print(f"List after removing Dog: {fruits}") # This will raise a ValueError since "Dog" is not in the list '''

item_to_remove = "Banana"
if item_to_remove in fruits:
    fruits.remove(item_to_remove)
    print(f"{item_to_remove} removed from the list.")
else:
    print(f"{item_to_remove} not found in the list.")    