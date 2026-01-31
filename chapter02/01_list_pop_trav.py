ages = [19, 34, 23, 55, 19]

print("Initial list of ages:", ages)

for age in ages:
    print(age, end=" ")
print()

# Challenge: Print the ages like print(ages), expecting the output to be [19, 34, 23, 55, 19]

# My solution:
print("[", end="")
for i in range(len(ages)):
    if i != len(ages) - 1:
        print(ages[i], end=", ")
    else:
        print(ages[i], end="]\n ")    

print("--------------------")
for index, value in enumerate(ages, 100):
    print(f"Index: {index}, Value: {value}")         