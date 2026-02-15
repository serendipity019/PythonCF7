class FactoIterator:
    def __init__(self, num):
        if num < 0:
            raise ValueError("Factorial is not defined for negative numbers")
        self.num = num
        self.result = 1
        self.order = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.order > self.num:
            raise StopIteration
        
        if self.order == 0:
            # 0! = 1
            self.order +=1
            return 1
                
        self.result *= self.order
        self.order += 1
        return self.result
    
def main():
    facto_iter = FactoIterator(10)

    # get the first factorial using next() func
    a = next(facto_iter)
    print("The Zero facto is:", a)

    for facto in facto_iter:
        print(facto)

    print("-" * 20)
    new_facto_iter = FactoIterator(5)
    
    for index, factorial in enumerate(new_facto_iter):
        print(f"Factorial of {index} = {factorial}")    
        
if __name__ == "__main__":
    main()      