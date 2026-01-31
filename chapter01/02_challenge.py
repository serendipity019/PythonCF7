str1 = "Factory"

for i in range(len(str1)):
    print(str1[i] * (i + 1), end="*" * (len(str1) - i - 1))
    print()
print()    