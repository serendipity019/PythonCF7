from abc import ABC, abstractmethod

class AbstractStudentDAO(ABC):
    """
    Defines the student DAO API
    """

    @abstractmethod
    def insert(self, student):
        raise NotImplementedError()

    @abstractmethod
    def update(self, student_id, student):
        raise NotImplementedError()     
    
    @abstractmethod
    def delete(self, student_id):
        raise NotImplementedError() 
    
    @abstractmethod
    def get_one(self, student_id):
        raise NotImplementedError
    
class StudentImpl(AbstractStudentDAO):
    def __init__(self):
        self.students = {}

    def insert(self, student):
        student_id = student["id"]
        if student_id not in self.students:
            self.students[student_id] = student
            print(f"Inserted student with ID: {student_id}")
        else:
            print(f"Student with id: {student_id} already exists")    

    def update(self, student_id, student):
        if student_id in self.students:
            self.students[student_id] = student
            print(f"Updated student with id: {student_id}")
        else:
            print(f"Student with {student_id} id not found")       

    def delete(self, student_id):
        if student_id in self.students:
            del self.students[student_id]
            print(f"Student with id: {student_id} deleted")
        else:
            print(f"Student with {student_id} id not found") 

    def get_one(self, student_id):
        return self.students.get(student_id, "Student not found")
    
    def __repr__(self):
        return f"Students({self.students})"

class ABCInventory(ABC): # Or AbstractInvetory
    @abstractmethod
    def add_item(self, item):
        raise NotImplementedError # or Pass. But our teacher suggest raise ... 

    @abstractmethod
    def remove_item(self, item_name_to_remove):
        raise NotImplementedError
    
class InventoryImpl(ABCInventory):
        def __init__(self):
            self.items = []

        def add_item(self, item):
             self.items.append(item)
             print(f"Added item: {item}")     

        def remove_item(self, item_name_to_remove):
            for item in self.items:
                if item.name == item_name_to_remove:
                    self.items.remove(item)
                    print(f"Remove item: {item}")
                    return
            else: print(f"The item with name {item_name_to_remove} not found")

        def __repr__(self):
            return f"Items({self.items})"

class Item:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name
    
    __repr__ = __str__
    
    
    

def main():
    student_d = StudentImpl()
    student_d.insert({'id' : 1, 'name' : "Bob"})
    student_d.insert({'id' : 2, 'name' : "Anna"})
    student_d.insert({'id' : 3, 'name' : "Miltiadis"})
    student_d.insert({'id' : 1, 'name' : "Nick"})

    print(student_d)

    student_d.update(1, {'id' : 1, 'name' : "Costas"} )
    print(student_d)

    st2 =student_d.get_one(2)
    print(st2)

    student_d.delete(3)
    print(student_d)

    item1 = Item("PC")
    item2 = Item("Playstation")
    item3 = Item("X-box")

    Item_inv = InventoryImpl()
    Item_inv.add_item(item1)
    Item_inv.add_item(item2)
    Item_inv.add_item(item3)
    print(Item_inv)

    Item_inv.remove_item("PC")
    print(Item_inv)





if __name__ == "__main__":
    main()  
                    