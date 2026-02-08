
class Base:
    def __init__(self):
        self.pub = "I am public"

    def __private_method(self):
        return "This is a private"    
    
    def get_private(self):
        return self.__private_method()
    
class Derived(Base): # With this way we inherit the Base method
    def __init__(self):
        super().__init__()
        self.__pri = "I am new private var"  # This is the extra variable where we want to add in Base class.  

    def get_new_private_var(self):
        return self.__pri
    
def main():
    base = Base()
    print(base.pub)
    print(base.get_private())

    derived = Derived()
    print(derived.pub)
    print(derived.get_private())
    print(derived.get_new_private_var())


if __name__ == "__main__":
    main()
