def fibo(n: int) -> int:
   # fibo(n) = fibo(n-1) + fibo(n-2)
   # fibo(0) = 0
   # fibo(1) = 1
   if n in (0,1): return n
   return fibo(n-1) + fibo(n-2) 


def main():
   n = int(input("Please enter an integer: "))
   print(f"fibo {n} = {fibo(n)}")

if __name__ == "__main__":
   main() 