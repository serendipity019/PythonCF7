class SimpleIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index < len(self.data):
            result = self.data[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration

def main():
    numbers = list(range(10, 90, 10)) 

    # create an instance of SimpleIterator (an iterator)
    my_iter = SimpleIterator(numbers)

    # for item in my_iter:
    #     print(item)

    # print("-" * 20)

    a = next(my_iter) # This is the perpuse of iterator    
    b = next(my_iter)

    print("a is:", a)
    print("b is:", b)

    for item in my_iter:
        print(item)

    print("-" * 20)

    # a = next(numbers) # We can't make this because the lists aren't iterator    
    # b = next(numbers)
    for item in numbers:
        print(item)

    print("-" * 20)
    print(my_iter)

if __name__ == "__main__":
    main()            
