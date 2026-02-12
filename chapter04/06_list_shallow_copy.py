my_list = [ 1, 2, "Hello", [3, 4, 5]]

# shallow copy using slicing
new_list = my_list[:]

print(f"Are new_list and my_list the same object: {my_list is new_list}")
print(id(my_list))
print(id(new_list))

my_list[0] = 100

print(f"original list: {my_list}")
print(f"shallow copy list: {new_list}")

my_list[3][0] = 300
print(f"original list: {my_list}")
print(f"shallow copy list: {new_list}")