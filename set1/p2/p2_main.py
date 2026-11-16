# Full Name: Jit Lee S. Romero
# Section: IV-BSIT C
# Activity: P2 - Custom Module: student_utils
# Date: November 16, 2026


# Use the standard library to show when the report was generated.
from datetime import datetime

# Import style 1: import the whole module.
import student_utils

# Import style 2: import a specific function from the module.
from student_utils import determine_status


def accept_grades():
    while True:
        try:
            number_of_grades = int(input("How many grades will you enter? "))
            if number_of_grades > 0:
                break
            print("Enter a whole number greater than zero.")
        except ValueError:
            print("Enter a valid whole number.")

    grades = []

    for grade_number in range(1, number_of_grades + 1):
        while True:
            try:
                grade = float(input(f"Enter grade {grade_number}: "))
                if 0 <= grade <= 100:
                    grades.append(grade)
                    break
                print("The grade must be from 0 to 100.")
            except ValueError:
                print("Enter a valid number for the grade.")

    return grades


def main():
    print("P2 - Student Grade Report")
    print("Jit Lee S. Romero | IV-BSIT C")
    grades = accept_grades()

    report_time = datetime.now()

    print("\n--- Grade Report ---")
    print("Jit Lee S. Romero | IV-BSIT C")
    print(f"Generated: {report_time.strftime('%Y-%m-%d %H:%M:%S')}")

    # The module name is needed when using the first import style.
    print(f"Average: {student_utils.compute_average(grades):.2f}")
    print(f"Highest: {student_utils.get_highest_grade(grades):.2f}")
    print(f"Lowest: {student_utils.get_lowest_grade(grades):.2f}")

    # This function was imported directly, so the module name is not needed.
    print(f"Status: {determine_status(grades)}")


if __name__ == "__main__":
    main()
