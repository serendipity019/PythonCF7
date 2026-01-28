# The Input accept string from user
name = input("Please enter your name: ")
print(f"Hello, {name}!")

#year_of_birth = input("Please enter your year of birth: ")
#print("You are" 2026 - year_of_birth "years old.") # This will raise an error because year_of_birth is a string

# To fix the above error, we need to convert the input string to an integer
year_of_birth = int(input("Please enter your year of birth: "))
print("You are", 2026 - year_of_birth, "years old.") # Corrected version using int() to convert year_of_birth to integer
# print("You are", 2026 - int(input("Please enter your year of birth: ")), "years old.") # This is also valid but less readable

