class Student:
    """
    A class that represents a student with a firstname and lastname

    Attrs:
        firstname (str): The firstname of the student.
        lastname (str): The lastname of the student.
    """

    def __init__(self, firstname: str, lastname: str): # This is like the constructor in Java
        """ ... """
        self.firstname = firstname
        self.lastname = lastname
        

def main():
    st = Student("Bob", "Marley")
    print(f"First name: {st.firstname}")
    print(f"Last name: {st.lastname}")

if __name__ == "__main__":
    main()

