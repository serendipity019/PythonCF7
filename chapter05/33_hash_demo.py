class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def __eq__(self, other):
        return isinstance(other, Point) and self._x == other._x and self._y == other._y

    def __hash__(self):
        return hash((self._x, self._y))

    def __repr__(self):
        return f"Point({self._x}, {self._y})"

def main():
    p1 = Point(1, 2)   
    p2 = Point(3, 4)   
    p3 = Point(1, 2)

    print(f"p1 == p2: {p1 == p2}")
    print(f"p1 == p3: {p1 == p3}")   

    print("Hash values")
    print(f"Hash(p1): {hash(p1)}")
    print(f"Hash(p2): {hash(p2)}")
    print(f"Hash(p3): {hash(p3)}")

    point_dict = {
        p1 : "Point 1", 
        p2 : "Point 2",  
        p3 : "Point 3" # Because is hashable the dict look it as it make update
    }

    for key, value in point_dict.items():
        print(f"{key} : {value}")

if __name__ == "__main__":
    main()           
