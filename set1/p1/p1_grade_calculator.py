# Full Name: Jit Lee S. Romero
# Section: IV-BSIT C
# Activity: P1 - Student Grade Calculator
# Date: November 16, 2026


PASSING_AVERAGE = 75


def accept_grades():
    # Ask again until the user enters a positive whole number.
    while True:
        try:
            number_of_grades = int(input("How many grades will you enter? "))
            if number_of_grades > 0:
                break
            print("Enter a whole number greater than zero.")
        except ValueError:
            print("Enter a valid whole number.")

    grades = []

    # Only add a grade after it passes both input checks.
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


def compute_average(grades):
    return sum(grades) / len(grades)


def get_highest_grade(grades):
    return max(grades)


def get_lowest_grade(grades):
    return min(grades)


def determine_status(grades):
    average = compute_average(grades)
    if average >= PASSING_AVERAGE:
        return "PASS"
    else:
        return "FAIL"


def main():
    grades = []

    print("Student Grade Calculator")
    print("Jit Lee S. Romero | IV-BSIT C | P1")

    while True:
        print("\n1. Enter grades")
        print("2. View results")
        print("3. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            grades = accept_grades()
            print("Grades saved. Choose option 2 to view the results.")

        elif choice == "2":
            # Check for grades before calling the computing functions.
            if not grades:
                print("Please enter grades first using option 1.")
            else:
                print("\n--- Grade Results ---")
                print("Jit Lee S. Romero | IV-BSIT C")
                print(f"Average: {compute_average(grades):.2f}")
                print(f"Highest: {get_highest_grade(grades):.2f}")
                print(f"Lowest: {get_lowest_grade(grades):.2f}")
                print(f"Status: {determine_status(grades)}")

        elif choice == "3":
            print("Thank you for using the calculator!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()


# A local variable is created inside a function and can only be used there.
# For example, grade_number in accept_grades() is local to that function.
# A global variable is defined outside all functions and can be read inside them.
# In this program, PASSING_AVERAGE is a global constant read by determine_status().
# The grades parameter of each computing function is local, even when main() passes its grades list to it.
