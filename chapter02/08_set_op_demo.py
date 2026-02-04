bag = {"eggs", "oranges", "bananas"}
print("Initial bag:", bag)

# add an item
bag.add("apples")
print("Bag after adding apples:", bag)

bag.add("eggs")  # adding a duplicate item
print("Bag after adding eggs:", bag) 

# remove an item
bag.remove("oranges")
print("Bag after removing oranges:", bag)

# bag.remove("grapes")  # grapes not in the set, will raise KeyError
# print("Bag after removing grapes (not present):", bag)

# discard an item (no error if item not found)
bag.discard("grapes")  # grapes not in the set
print("Bag after discarding grapes (not present):", bag)

# Iteration

for item in bag:
    print(item, end=" ") 
print()