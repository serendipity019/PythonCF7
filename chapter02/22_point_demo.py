class Point:
    __count = 0 # We use duble underscore for "private"

    def __init__(self, x = 0, y = 0):
        self.__x = x
        self.__y = y
        Point.__count += 1

    def __str__(self):
        return f"({self.__x}, {self.__y})"    
        
    def __repr__(self): # This is for debugging representation
        return f"Point(x={self.__x}, y={self.__y})"

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.__x == other.__x and self.__y == other.__y
        else:
            return False
    
    # def __lt__, __gt__
    @classmethod
    def get_count(cls):
        return cls.__count    

    @property
    def x(self): # This work as getter in Java
        return self.__x

    @x.setter
    def x(self, x): # This work as setter in Java
        self.__x = x
        
    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = y

def main():
    p1 = Point(10, 20)
    p2 = Point(11, 20)

    print(p1)
    print(p2)

    print(f"p1 == p2: {p1 == p2}")

    p2.x = 10
    print(p1.x, p1.y)
    print(f"p1 == p2: {p1 == p2}")

    print(Point.get_count)

if __name__ == "__main__":
    main()
    


