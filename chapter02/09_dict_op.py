# Populate a dictionary
products = { 1: "apple",
             2: "banana",
             3: "cherry",
             4: "honey" 
}

print(f"Initial products: {products}")

# insert a new key-value pair
products[5] = "orange"
print(f"Products after adding orange: {products}")

# update an existing key-value pair
products[3] = "orange"
print(f"Products after updating key 3 to orange: {products}")

# Read a value by key
product_2 = products[2]
print(product_2)

#product_20 = products[20]
#print(product_20)  # This will raise a KeyError since key 20 does not exist

# Safe way to read a value by key using get()
product_20 = products.get(20, "Product not Found")
print(product_20)  # This will print "Product not Found" since key 20 does not exist

# Delete a key-value pair
del products[4]
print(f"Products after deleting key 4: {products}")

removed_item = products.pop(4, "Item not found")
print(f"Removed item: {removed_item}")

# del products[4]  # This will raise a KeyError since key 4 has already been deleted

# Delete: remove the 'last' inserted item with popitem()
key, value = products.popitem()
print(f"key: {key}, value: {value}")
print(f"Products after popitem: {products}")

key_to_check = 3

if key_to_check in products:
    print(f"Key {key_to_check} exists in products with value: {products[key_to_check]}")
else:
    print(f"Key {key_to_check} does not exist in products.")

# Iterate 
for key in products:
    print(f"Key: {key}, Value: {products[key]}")

print("-" * 20) 
for key in products.keys(): # This is for readability, but it is the same as the above loop 
    print(f"Key: {key}, Value: {products[key]}")

print("-" * 20) 
for value in products.values():
    print(value)

print("-" * 20)
for key, value in products.items():
    print(f"Key: {key}, Value: {value}")

