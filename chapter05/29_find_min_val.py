

def main():
    students = {
    'Alice' : 85, 
    'Bob' : 90, 
    'Charlie' : 90,
    'Diana' :95, 
    'Eve' :50, 
    #'Fiodor': None 
    }

    # Find the student name with the lowest alphabetical order.
    student_with_min_alphabetical_order = min(students)
    print(student_with_min_alphabetical_order) 

    # Find the student with the lowest grade
    student_with_min_grade = min(students.values()) # Mine thought
    print(student_with_min_grade)
    student_with_min_grade = min(students, key= students.get) # Teacher way
    print(student_with_min_grade)

    # Student with the shortest name length
    student_with_shortest_name = min(students, key= len)
    print(student_with_shortest_name)

    students2 = {
    'Alice' :[85, 92, 100],
    'Bob' :[90, 72, 80],
    'Charlie' :[90, 95, 94],
    'Diana' :[95, 98, 100],
    'Eve' :[50, 60, 55],
    'Fiodor': []
    }



if __name__ == "__main__":
    main()   