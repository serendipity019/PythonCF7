numbers = list(range(1, 11))

# even numbers
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(type(even_numbers))
'''
for num in even_numbers: # Because filter is an iterator it can print one time and after unload. 
    print(num, end=" ")
print("\n","-" * 20)

for num in even_numbers: # Second none to print
    print(num, end=" ")
print("\n","-" * 20)
'''
print(*even_numbers) # Because filter is an iterator it can print one time and after unload. 
print(*even_numbers) # second time none to print

even_numbers_list = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers_list)
print(even_numbers_list) # Now can print and second because we have list, no iterator. 
print("\n","-" * 20)

def even_num_func(n) -> bool:
    return n % 2 == 0

my_even_list = list(filter(even_num_func, numbers))
print(my_even_list)