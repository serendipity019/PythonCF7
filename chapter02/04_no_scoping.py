import random

# No scoping example
random_numbers = []

for i in range(10):
    num = random.randint(1, 100)
    random_numbers.append(num)

print(random_numbers)

# The next for find the last even number in the list
# Accessing the variable 'even' outside the loop
for num in random_numbers:
    if num % 2 == 0:
        even = num
print(f"Last even number of the list is: {even}")        