from functools import lru_cache

@lru_cache(maxsize=None)
def fibo(n: int) -> int:
   if n in (0,1): return n
   return fibo(n-1) + fibo(n-2) 

def fibo_with_logging(n):
   if fibo.cache_info().hits > 0:
      print(f"Cache hit for Fibo({n})")
   else:
      print(f"Calculating Fibo({n})")
   return fibo(n)

def main():
   fibo.cache_clear()

   fibo_nums = [fibo_with_logging(n) for n in range(21)]
   print(fibo_nums)

if __name__ == "__main__":
    main()

