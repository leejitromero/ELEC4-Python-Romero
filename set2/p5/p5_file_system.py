# Full Name: Jit Lee S. Romero
# Section: IV-BSIT C
# Activity: P5 - Student Information File System
# Date: November 24, 2026

from pathlib import Path


# The data stays beside this script even if the terminal is in another folder.
STUDENTS_FILE = Path(__file__).with_name("students.txt")


def load_records():
    records = []
    student_ids = set()

    try:
        with open(STUDENTS_FILE, "r", encoding="utf-8") as student_file:
            for line_number, line in enumerate(student_file, start=1):
                if not line.strip():
                    continue

                fields = line.strip().split("|")
                if len(fields) != 4 or any(not field.strip() for field in fields):
                    raise ValueError(f"Invalid student record on line {line_number}.")

                student_id, full_name, course_section, average_text = fields
                try:
                    average = float(average_text)
                except ValueError:
                    raise ValueError(f"Invalid average on line {line_number}.") from None

                if not 0 <= average <= 100:
                    raise ValueError(f"Average outside 0 to 100 on line {line_number}.")
                if student_id.casefold() in student_ids:
                    raise ValueError(f"Duplicate student ID on line {line_number}.")

                student_ids.add(student_id.casefold())
                records.append({
                    "id": student_id,
                    "name": full_name,
                    "section": course_section,
                    "average": average,
                })
    except FileNotFoundError:
        # The first run starts with no records; adding creates students.txt.
        return []

    return records


def read_text(prompt):
    while True:
        text = input(prompt).strip()
        if text and "|" not in text:
            return text
        print("Enter a non-empty value without the | symbol.")


def read_average():
    while True:
        try:
            average = float(input("General average (0-100): "))
            if 0 <= average <= 100:
                return average
            print("The average must be from 0 to 100.")
        except ValueError:
            print("Enter a numeric average.")


def append_record(record):
    # Append one record without replacing the students already saved.
    with open(STUDENTS_FILE, "a+", encoding="utf-8") as student_file:
        student_file.seek(0)
        contents = student_file.read()
        if contents and not contents.endswith("\n"):
            student_file.write("\n")

        student_file.write(
            f"{record['id']}|{record['name']}|{record['section']}|{record['average']:.2f}\n"
        )


def add_student(records):
    student_id = read_text("Student ID: ")
    if any(record["id"].casefold() == student_id.casefold() for record in records):
        print("That student ID already exists.")
        return

    record = {
        "id": student_id,
        "name": read_text("Full name: "),
        "section": read_text("Course/section: "),
        "average": read_average(),
    }

    try:
        append_record(record)
    except (OSError, UnicodeError) as error:
        print(f"Cannot save the record: {error}")
        return

    # Update memory only after the file was successfully written.
    records.append(record)
    print(f"Saved: {record['id']} | {record['name']} | {record['average']:.2f}")
    print(f"Total saved records: {len(records)}")


def main():
    print("P5 - Student Information File System")
    print("Jit Lee S. Romero | IV-BSIT C")

    try:
        records = load_records()
    except (OSError, ValueError, UnicodeError) as error:
        # Preserve the existing file if its contents cannot be loaded safely.
        print(f"Cannot load students.txt: {error}")
        return

    print(f"Loaded records: {len(records)}")
    while True:
        print("\n1. Add and save a student")
        print("2. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_student(records)
        elif choice == "2":
            print("Program closed. Saved records remain in students.txt.")
            return
        else:
            print("Invalid choice. Enter 1 or 2.")


if __name__ == "__main__":
    try:
        main()
    except (EOFError, KeyboardInterrupt):
        print("\nProgram closed. Previously saved records are kept.")


# Learning references:
# https://www.youtube.com/watch?v=ix9cRaBkVe0
# https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
