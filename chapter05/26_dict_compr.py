numbers = list(range(1, 8))

squared_nums = {number : number**2 for number in numbers}
print(squared_nums)

even_sq_nums = {number : number**2 for number in numbers if number % 2 == 0}
print(even_sq_nums)

def square(n):
    return n ** 2

sq_dict = {number: square(number) for number in numbers}
print(sq_dict)