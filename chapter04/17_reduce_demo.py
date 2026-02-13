from functools import reduce

# list of nums (ints)
my_ints = list(range(1, 6))

result_sum = reduce(lambda x, y: x + y, my_ints)
print(result_sum)

result_mult = reduce(lambda x, y: x * y, my_ints)
print(result_mult)