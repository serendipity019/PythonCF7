my_num = 10
my_float = 3.14
my_string = "Hello CF7!"

print("Printing comma separated values")
print(my_num, my_float, my_string)

print("-------------------------")

print(my_num, my_float, my_string, sep="\t")  # Tab separator

print("-------------------------")

print(my_num, my_float, my_string, sep="\t", end="***\n")  # Tab separator with custom end