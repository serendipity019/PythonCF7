def upscale_grades(students_grades: dict) -> dict:
    return {name: (grade + 1 if grade <= 9 else grade) for name, grade in students_grades.items()}

def filter_passed(students_grades: dict) -> dict:
    return {name: grade for name, grade in students_grades.items() if grade >=5 }
    # return {name: (grade >=5) for name, grade in students_grades.items()} # This return: name : True or False

def categorize_grades(students_grades: dict)-> dict:
    passed = {name: grade for name, grade in students_grades.items() if 5 <= grade < 10 }
    failed = {name: grade for name, grade in students_grades.items() if grade < 5}
    honors = {name: grade for name, grade in students_grades.items() if grade == 10}

    return {
        "Passed": passed,
        "Failed": failed,
        "Honors": honors  
    }  

def calculate_average(students_grades: dict)-> int | float:
    #return sum(grades) / len(grades) if grades else 0
    return sum(students_grades.values()) / len(students_grades.values()) if students_grades else 0

def main():
   students_grades = {
       "Alice": 7,
       "Bob": 5,
       "Charlie": 9,
       "David": 10,
       "Eve": 3,
       "Frank": 6,
       "Grace": 8,
       "Heidi": 4,
       "Ivan": 10,
       "Judy": 2
   }
   
   print(f"Initial grades: {students_grades}")

   upscaled_grades = upscale_grades(students_grades)
   # print(f"Upscaled grades: {upscaled_grades}")
   print("Upscaled grades")
   for name, grade in upscaled_grades.items():
       print(f"{name}: {grade}")

   categorized_grades = categorize_grades(upscaled_grades)

   print(f"Passed Students: {categorized_grades['Passed']}")
   print(f"Failed Students: {categorized_grades['Failed']}")
   print(f"Honored Students: {categorized_grades['Honors']}")



if __name__ == "__main__":
    main()