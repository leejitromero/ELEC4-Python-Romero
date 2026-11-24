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


def read_text(prompt, current_value=None):
    while True:
        text = input(prompt).strip()
        if not text and current_value is not None:
            return current_value
        if text and "|" not in text:
            return text
        print("Enter a non-empty value without the | symbol.")


def read_average(current_value=None):
    while True:
        try:
            text = input("General average (0-100): ").strip()
            if not text and current_value is not None:
                return current_value
            average = float(text)
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


def show_student(record):
    print(
        f"{record['id']} | {record['name']} | "
        f"{record['section']} | {record['average']:.2f}"
    )


def display_students(records):
    if not records:
        print("No student records yet.")
    else:
        print("\nStudent ID | Full name | Course/section | Average")
        for record in records:
            show_student(record)
    print(f"Total records: {len(records)}")


def find_student(records, student_id):
    for record in records:
        if record["id"].casefold() == student_id.casefold():
            return record
    return None


def search_student(records):
    student_id = read_text("Student ID to search: ")
    record = find_student(records, student_id)
    if record is None:
        print("Student not found.")
    else:
        print("Student found:")
        show_student(record)


def save_records(records):
    # Updating a record rewrites the file with the complete revised list.
    with open(STUDENTS_FILE, "w", encoding="utf-8") as student_file:
        for record in records:
            student_file.write(
                f"{record['id']}|{record['name']}|{record['section']}|{record['average']:.2f}\n"
            )


def update_student(records):
    student_id = read_text("Student ID to update: ")
    record = find_student(records, student_id)
    if record is None:
        print("Student not found.")
        return

    print("Current information:")
    show_student(record)
    print("Press Enter to keep a value. The student ID stays the same.")

    updated_record = {
        "id": record["id"],
        "name": read_text("Full name: ", record["name"]),
        "section": read_text("Course/section: ", record["section"]),
        "average": read_average(record["average"]),
    }

    index = records.index(record)
    revised_records = records.copy()
    revised_records[index] = updated_record
    try:
        save_records(revised_records)
    except (OSError, UnicodeError) as error:
        print(f"Cannot save the update: {error}")
        return

    # Keep the in-memory list unchanged until saving succeeds.
    records[index] = updated_record
    print("Student updated and saved:")
    show_student(updated_record)


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
        print("2. Display all students")
        print("3. Search by student ID")
        print("4. Update a student")
        print("5. Save all records")
        print("6. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_student(records)
        elif choice == "2":
            display_students(records)
        elif choice == "3":
            search_student(records)
        elif choice == "4":
            update_student(records)
        elif choice == "5":
            try:
                save_records(records)
            except (OSError, UnicodeError) as error:
                print(f"Cannot save the records: {error}")
            else:
                print(f"All {len(records)} records saved.")
        elif choice == "6":
            print("Program closed. Saved records remain in students.txt.")
            return
        else:
            print("Invalid choice. Enter a number from 1 to 6.")


if __name__ == "__main__":
    try:
        main()
    except (EOFError, KeyboardInterrupt):
        print("\nProgram closed. Previously saved records are kept.")


# Learning references:
# https://www.youtube.com/watch?v=ix9cRaBkVe0
# https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
