# Full Name: Jit Lee S. Romero
# Section: IV-BSIT C
# Activity: P7 - Student Management System with Classes
# Date: November 24, 2026


class Student:
    def __init__(self, student_id, full_name, average):
        self.student_id = student_id
        self.full_name = full_name
        self.set_average(average)

    def get_average(self):
        return self.__average

    def set_average(self, average):
        # I-check muna ang value bago baguhin ang private average.
        average = float(average)
        if not 0 <= average <= 100:
            raise ValueError("Average must be from 0 to 100.")
        self.__average = average

    def update_information(self, full_name, average):
        self.set_average(average)
        self.full_name = full_name

    def display(self):
        print(f"{self.student_id} | {self.full_name} | Average: {self.get_average():.2f}")


class Subject:
    def __init__(self, code, title):
        self.code = code
        self.title = title

    def display(self):
        print(f"Subject: {self.code} - {self.title}")


class Section:
    def __init__(self, name, subject):
        # May isang Subject at listahan ng Student objects ang Section.
        self.name = name
        self.subject = subject
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def display_students(self):
        print(f"Section: {self.name}")
        self.subject.display()
        for student in self.students:
            student.display()
        print(f"Total students: {len(self.students)}")


def main():
    print("P7 - Student Management System with Classes")
    print("Jit Lee S. Romero | IV-BSIT C")

    # Bawat Student object ay may sariling information at average.
    students = [
        Student("2026-001", "Jit Lee S. Romero", 80),
        Student("2026-002", "Juan Cruz", 85),
        Student("2026-003", "Maria Santos", 90),
    ]

    subject = Subject("ELEC4", "Python Programming")
    section = Section("IV-BSIT C", subject)
    for student in students:
        section.add_student(student)

    print("\nBefore update:")
    section.display_students()

    students[0].update_information("Jit Lee S. Romero", 92)
    try:
        students[0].set_average(110)
    except ValueError as error:
        print(f"\nRejected invalid average: {error}")

    print("\nAfter update:")
    section.display_students()


if __name__ == "__main__":
    main()

# Sanggunian: Bro Code Python course at Python docs (classes).
