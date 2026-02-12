def my_power(base: int, exp: int) -> int:
   return base ** exp


def main():
   print(my_power(2, 10))

   power_to = lambda base, exp: base ** exp # lambda function
   print(power_to(2, 10))

if __name__ == "__main__":
   main() 