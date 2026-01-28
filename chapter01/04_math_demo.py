import math

name = "Alice"
age = 20

print("CF7")
print("PI:", math.pi)

print("String Concatenation")
#print(name + " is " + age + " years old.")  # This will raise a TypeError
print(name + " is " + str(age) + " years old.") # Corrected version using str() to convert age to string
print(name, "is", age, "years old.")  # Using comma-separated values in print function is also valid

# Python2 style formatting
print()
print("Python2 Style Formatting")
print("%s is %d years old." % (name, age))
print("{} is {} years old.".format(name, age))
print("PI = %6.2f" % math.pi) # Width 6, 2 decimal places

# Python3 formatting
print("\nPython3 Style Formatting (f-strings)")
print("Age is {0:2d}".format(age)) # Width 2 for integer
print("PI is {0:.3f}".format(math.pi)) # 3 decimal places
# To understand what is the 0 in {0:2d} and {0:.3f} look this:
print("PI = {1:.3f}, Name = {0}, Age = {2}".format(name, math.pi, age))

# This print : Alice is 20 years old**
print("\n{0} is {1} years old".format(name, age), end="**\n")

# f-string examples
print(f"{name} is {age} years old.") # The best and recommended way in Python 3.6+
print(f"PI is {math.pi:.4f}") # 4 decimal places using f-string