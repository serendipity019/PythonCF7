def enroll_student(*students, min_grade=50, department="Computer Science", **kwargs):
    print(f"Min grade: {min_grade}")
    print(f"Department: {department}")
    
    print("\nEnrolled Students")
    for student in students:
        print(f" - {student}")

    if kwargs:
        print("\nAdditional Informations")    
        for key, value in kwargs.items():
            print(f"{key} : {value}")
    print("---End of enrollment---")    

def main():
    enroll_student("Chris", "Marinos")
    print("-" * 20)

    enroll_student("Helen", "Nick", "Jack", min_grade=70, academic_year=2026, semeter="Fall")
    print("-" * 20)

if __name__ == "__main__":
    main()