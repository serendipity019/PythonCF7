from functools import reduce

n = int(input("Please give an integer: "))

facto = reduce(lambda x, y: x * y, range(1, n + 1))
print(f"{n}! = {facto}")

def print_and_mul(x, y) -> int:
    result = x * y
    print(f"{x} * {y} = {result}")
    return result

new_res = reduce(lambda x, y: print(f"{x} * {y} = {x * y}") or (x * y), range(1, n + 1))