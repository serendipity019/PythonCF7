# range(10) creates an iterable object

a = range(10)
print(f"Type of a: {type(a)}")
print("Range a:", a)

for i in range(10):
    if i == 5:
        break
    print(i, end=" ")
print()

for i in range(10):
    if i == 5:
        continue
    print(i, end=" ")
print("-" * 20)

for i in range(10):
    if i == 5:
        break
    print(i, end=" ")
else:
    print("Loop ended normally") # The else block will not execute because the loop was terminated by a break

for i in range(10):
    if i == 5:
        continue
    print(i, end=" ")
else:
    print("Loop ended normally") # The else block executes because the loop was not terminated by a break   

# List of fruits
fruits = ["Apple", "Banana", "Cherry", "Orange"]    

fruit_to_check = "Banana"

for fruit in fruits:
    if fruit == fruit_to_check:
        print(f"{fruit_to_check} found in the list!")
        break
else:
    print(f"{fruit_to_check} not found in the list.")    

# Happy hour
print("Why do Python devs never get lost?")
print("Because they always know where 'in' is!")

fruit_to_check = "Melon"
if fruit_to_check in fruits:
    print(f"{fruit_to_check} found in the list!")
else:
    print(f"{fruit_to_check} not found in the list.")    

# Challenge
print("One line example")
print(f"{fruit_to_check} is {'in' if fruit_to_check in fruits else 'not in'} the list.")    