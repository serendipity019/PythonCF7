def memoize(func):
    """  
    A simple memoization decorator to cache results of the function.

    Param:
        func (function): The import function 
    """
    cache = {}
    #cache_stats = {"hits": 0, "misses": 0}

    def wrapper(n):
        if n in cache:
            #cache_stats["hits"] += 1
            print(f"Cache hit for Fibo({n})")
        else:
            #cache_stats["misses"] += 1
            print(f"Calculating Fibo({n})")
            cache[n] = func(n)
        return cache[n]
    
    return wrapper

def fibo(n: int) -> int:
   if n in (0,1): return n
   return fibo(n-1) + fibo(n-2) 

@memoize
def fibo2(n: int) -> int:
   if n in (0,1): return n
   return fibo2(n-1) + fibo2(n-2) 

def main():
    print([fibo(n) for n in range(20)])
    print([fibo2(n) for n in range(20)])

if __name__ == "__main__":
    main() 