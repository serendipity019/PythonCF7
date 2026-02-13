list_of_ints = list(range(1, 8))

# 1. compute the square of the nums using list compr
sq_nums_compr = [num ** 2 for num in list_of_ints]
print(sq_nums_compr)

# 2. compute the square of the nums using map function
sq_nums_map = list(map(lambda num: num ** 2 , list_of_ints))
print(sq_nums_map)

# 3. squard nums using a function
def square_function(num: int) -> int:
    return num ** 2

sq_nums_func = [square_function(num) for num in list_of_ints]
print(sq_nums_func)

# We can put and filter
sq_nums_func_filter_evens = [square_function(num) for num in list_of_ints if not num % 2]
print(sq_nums_func_filter_evens)
# 4. use 'square_function" and map
sq_map_func = list(map(square_function, list_of_ints))
print(sq_map_func)

# 5. filter and square only with list compr
filtered_sq_list_compr = [num ** 2 for num in list_of_ints if num % 2]
print(filtered_sq_list_compr)

map_filter_sq_list = list(map(lambda num: num ** 2, filter(lambda num: not num % 2, list_of_ints)))
print(map_filter_sq_list)

