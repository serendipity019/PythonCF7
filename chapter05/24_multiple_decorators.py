import time

def log_calls(func):
    """ 
    A Decorator that logs the function call.
    """
    def wrapper(*args, **kwargs):
        print(f"Calling function '{func.__name__}' with args {args} and kwargs {kwargs}")
        return func(*args, **kwargs)
    
    return wrapper

def measure_time(func):
    """ 
    A decorator that measures the execution time of the function.
    """
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        print(f"Execution time of '{func.__name__}': {end_time - start_time:.7f}")
        return result
    
    return wrapper

# The decorators are applied bottom to top. (@measure_time : first, @log_calls : second)
# Execution is top to bottom (@log_calls : first, @measure_time : second)

# first function to compare
@log_calls
@measure_time
def fibo(n: int) -> int:
   if n in (0,1): return n
   return fibo(n-1) + fibo(n-2) 

# second function to compare
@log_calls
@measure_time
def fibonacci(num: int):
    #time.sleep(1)
    if num in (0, 1): return num 

    a, b = 0, 1

    for _ in range(2, (num + 1)):
        a, b = b, (a + b)

    return b 

def main():
    print(fibonacci(4))
    print(fibo(4))

if __name__ == "__main__":
    main() 