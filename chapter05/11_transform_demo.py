

def main():
   grades = [7, 5, 9, 10, 3]

   upscaled_grades = [grade + 1 if grade <= 9 else grade for grade in grades]
   print(f"Upscaled grades: {upscaled_grades}")

    # using map()
   upscaled_grades_map = list(map(lambda grade: grade + 1 if grade <= 9 else grade, grades))
   print(f"Upscaled grades using map(): {upscaled_grades_map}")

   # filter using list compr
   passed_grades = [grade for grade in grades if grade >= 5]
   print(f"Passed grades: {passed_grades}")

   # filter using filter()
   passed_grades_filter = list(filter(lambda grade: grade >= 5, grades))
   print(f"Passed grades using filter(): {passed_grades_filter}")

if __name__ == "__main__":
    main()