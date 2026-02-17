

def main():
    students = {
    'Alice' :[85, 92, 100],
    'Bob' :[70, 68, 99],
    'Charlie' :[90, 95, 94],
    'Diana' :[95, 98, 100],
    'Eve' :[50, 60, 55],
    'Fiodor': []
}
    
    while True:
        try:
            threshold = int(input("Please insert a threshold (int) or 100 to quit: "))
            if threshold == 100:
                break
        except ValueError:
            print("Invalid input.")
            continue

        average_grades = {student: round(sum(grades) / len(grades), 2) for student, grades in students.items() if grades and round(sum(grades) / len(grades), 2) > threshold}

        for student, avg_grade in average_grades.items():
            print(f"{student}: {avg_grade}")


if __name__ == "__main__":
    main()   