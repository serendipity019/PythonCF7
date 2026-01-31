a = 10
b = 20

sum = a + b
print("The sum of", a, "and", b, "is", sum)
print("--------------------")
print("Type of a:", type(a))
print(f"Type of b: {type(b)}")

magic_result = a.__add__(b)
print("Magic method result:", magic_result)