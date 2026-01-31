name = input("Please enter your name: ")

age = int(input("Please enter your age: "))

height = float(input("Please enter your height in meters (e.g., 1.75): "))

is_student = input("Are you a student? (Yes/No):").strip().lower() == 'yes' #(YES, Yes, yES, yes)

print(f"Hello, {name}!")

if is_student:
    print("It's great to meet a fellow student!")
else:
    print("You are not a student, nice to meet you!")

print("Your age is {} and your height is {:.2f} meters".format(age, height))        
