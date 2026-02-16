import time 
from functools import lru_cache

def timer_decorator(func):
    """ 
    Decorator to mesure the execution time of afunction.

    Params:
        func (function): The function to be decorated.

    Returns:
        function: The decorated function with added timing functionality.    
    """
    def inner_function(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time} seconds to run")
        return result
    
    return inner_function

# first function to compare
@lru_cache(1000000)
def fibo(n: int) -> int:
   if n in (0,1): return n
   return fibo(n-1) + fibo(n-2) 

# second function to compare
@timer_decorator
def fibonacci(num: int):
    if num in (0, 1): return num 

    a, b = 0, 1

    for _ in range(2, (num + 1)):
        a, b = b, (a + b)

    return b 


def main():
    my_fibo_func = timer_decorator(fibo)
    print(my_fibo_func(30))

    my_fibo_func2 = fibonacci(30)
    print(my_fibo_func2)

if __name__ == "__main__":
    main() 