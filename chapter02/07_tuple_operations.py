# Define a tuple of student names
students = ("Alice", "Bob", "Charlie", "Diana")
print(f"{students}: Type: {type(students)}")

# iteration
for student in students:
    print(student, end=" ")
print("\nenumerate example:")

for index, student in enumerate(students, start=1):
    print(f"Student {index}: {student}")
print("-" * 20)    

# Unpacking tuples
first_st, second_st, *rest_students = students[0], students[1], students[2:]
print(f"First student: {first_st}")
print(f"Second student: {second_st}")
print(f"Rest of the students: {rest_students}")

print("-" * 20)
# Unpacking example second
first_st, second_st, *rest_students = students
print(f"First student: {first_st}")
print(f"Second student: {second_st}")
print(f"Rest of the students: {rest_students}")

# Update an element in a tuple (tuples are immutable, so we create a new tuple or convert to a list)
students = list(students)  # Convert to list
students[0] = "Helen"        # Update the first element
students = tuple(students)  # Convert back to tuple

print(f"{students}: Type: {type(students)}") 