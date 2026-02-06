# Falsy - Truthy Values
# In Python, certain values are considered "falsy," meaning they evaluate to False in a boolean context. These include: 0, 0.0, 0j, '', [], {}, set(), None, and False itself. All other values are considered "truthy," meaning they evaluate to True in a boolean context. This includes non-empty strings, non-zero numbers, non-empty collections, and any other objects. Understanding which values are falsy and which are truthy is important for writing effective conditional statements and controlling the flow of your program.

empty_dict = {}
print(type(empty_dict), bool(empty_dict))  # Output: <class 'dict'> False

a = 5

if a > 0 and a < 10:
    print("a is between 0 and 10")

if 0 < a < 10:
    print("a is between 0 and 10")    