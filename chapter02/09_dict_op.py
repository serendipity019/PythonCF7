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