# Full Name: Jit Lee S. Romero
# Section: IV-BSIT C
# Activity: P3 - Student Record Manager
# Date: November 16, 2026


def add_student(students, student_names):
    name = input("Enter the student's full name: ").strip()

    if not name:
        print("The name cannot be empty.")
        return

    # Lowercase names let the set detect duplicates regardless of capitalization.
    normalized_name = name.lower()
    if normalized_name in student_names:
        print("This student already exists. No duplicate was added.")
    else:
        students.append(name)
        student_names.add(normalized_name)
        print(f"Added: {name}")


def remove_student(students, student_names):
    name = input("Enter the full name to remove: ").strip()

    if not name:
        print("The name cannot be empty.")
        return

    normalized_name = name.lower()
    if normalized_name not in student_names:
        print("Student not found.")
        return

    # Remove the same student from both collections to keep them consistent.
    for student in students:
        if student.lower() == normalized_name:
            students.remove(student)
            student_names.remove(normalized_name)
            print(f"Removed: {student}")
            break


def search_students(students):
    search_text = input("Enter a name or part of a name to search: ").strip()

    if not search_text:
        print("The search cannot be empty.")
        return

    matches = []
    for student in students:
        if search_text.lower() in student.lower():
            matches.append(student)

    if not matches:
        print("No matching students found.")
    else:
        print("\n--- Search Results ---")
        display_students(matches)


def display_students(students):
    # Sort a copy for display while keeping the original list unchanged.
    sorted_students = sorted(students, key=str.lower)

    if not sorted_students:
        print("No students to display.")
    else:
        for number, student in enumerate(sorted_students, start=1):
            print(f"{number}. {student}")

    print(f"Total students: {len(students)}")


def main():
    students = []
    student_names = set()

    print("P3 - Student Record Manager")

    while True:
        # Keep the author's name visible when taking screenshots of each operation.
        print("\nJit Lee S. Romero | IV-BSIT C | P3")
        print("1. Add student")
        print("2. Remove student")
        print("3. Search students")
        print("4. Display all students")
        print("5. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_student(students, student_names)
        elif choice == "2":
            remove_student(students, student_names)
        elif choice == "3":
            search_students(students)
        elif choice == "4":
            print("\n--- Student Records ---")
            display_students(students)
        elif choice == "5":
            print("Thank you for using the record manager!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, 4, or 5.")


if __name__ == "__main__":
    main()


# A list keeps items in order and can contain duplicates.
# In this program, students is a list that stores names using the capitalization entered by the user.
# A set stores unique values and does not guarantee an order.
# The student_names set stores lowercase names so Juan Cruz and juan cruz count as the same name.
# Displaying uses a sorted copy of the list, while adding and removing students keeps both collections updated.
