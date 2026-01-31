message = "Coding Factory"

print(message[0])
print(message[1])
print(message[2])
print(message[3])
print(message[4])
print(message[5])

# message[0] = "c" # This will raise an error because strings are immutable
message = "c" + message[1:]  # Correct way to change the first character
print(message)
print(f"Length of {message} is {len(message)} characters")

for char in message:
    print(char)

for char in message:
    print(char, end=' ')    
print()  # for newline

print("-" * 20  )  # separator line
# enchanced for loop with index
for i in range(10):
    print(i)
print("-" * 10  )

print(i) # i is still accessible here and will print 9

# for indexing based loop
message = "Coding Factory"
for i in range(len(message)):
    print(message[i], end=' ')

my_num = 123456789
# result: the sum of first and last digit
'''result = int(my_num[0]) + int(my_num[-1])  # This will raise an error because integers are not subscriptable
print("The result is:", result) '''

result = int(str(my_num)[0]) + int(str(my_num)[-1]) 
print("\nThe result is:", result) 