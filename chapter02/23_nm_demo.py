class Point:
    __count = 0 # We use duble underscore for "private"

    def __init__(self, x = 0, y = 0):
        self._x = x
        self.__y = y
        Point.__count += 1

    def __str__(self):
        return f"({self._x}, {self.__y})"    
        

def main():
    p1 = Point(10, 20)
    p2 = Point(11, 20)
    print(p1)
    print(p2)

    print(p1._x)
    # p1.__y = 100 # Variable name  p1.__y
    # print(p1.__y) # This is variable no the y from the Point class.
    print(p1._Point__y) # For this reason don't is really private _functionName


if __name__ == "__main__":
    main()
    


