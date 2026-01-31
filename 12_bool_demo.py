# Booleans
a = True
b = False

print(type(a), a, sep=", ")
print(type(b), b, sep=", ")

# Short circuit 
result_or = a or b
print("Result of a or b:", result_or)

print("True + True=", True + True) # True is treated as 1
print(True * 5)  # Because True is treated as 1, this evaluates to 5
