# Full Name: Jit Lee S. Romero
# Section: IV-BSIT C
# Activity: P5 - Student Information File System
# Date: November 24, 2026

from pathlib import Path

# Katabi ng program ang data file kahit saan buksan ang terminal.
STUDENTS_FILE = Path(__file__).with_name("students.txt")


def find_student(records, student_id):
    for record in records:
        if record["id"].casefold() == student_id.casefold():
            return record
    return None


def load_records():
    records = []
    try:
        with open(STUDENTS_FILE, "r", encoding="utf-8") as file:
            for line_number, line in enumerate(file, 1):
                if not line.strip():
                    continue
                fields = line.strip().split("|")
                if len(fields) != 4 or any(not field.strip() for field in fields):
                    raise ValueError(f"Invalid student record on line {line_number}.")

                student_id, name, section, average_text = fields
                try:
                    average = float(average_text)
                except ValueError:
                    raise ValueError(f"Invalid average on line {line_number}.") from None
                if not 0 <= average <= 100:
                    raise ValueError(f"Average outside 0 to 100 on line {line_number}.")
                if find_student(records, student_id) is not None:
                    raise ValueError(f"Duplicate student ID on line {line_number}.")
                records.append({"id": student_id, "name": name,
                                "section": section, "average": average})
    except FileNotFoundError:
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


def record_line(record):
    return (f"{record['id']}|{record['name']}|"
            f"{record['section']}|{record['average']:.2f}\n")


def append_record(record):
    # a+ para magdagdag; lagyan muna ng newline kung kulang ang dating file.
    with open(STUDENTS_FILE, "a+", encoding="utf-8") as file:
        file.seek(0)
        contents = file.read()
        if contents and not contents.endswith("\n"):
            file.write("\n")
        file.write(record_line(record))


def save_records(records):
    # w para isulat muli ang buong list kapag may update.
    with open(STUDENTS_FILE, "w", encoding="utf-8") as file:
        for record in records:
            file.write(record_line(record))


def show_student(record):
    print(f"{record['id']} | {record['name']} | "
          f"{record['section']} | {record['average']:.2f}")


def display_students(records):
    if not records:
        print("No student records yet.")
    else:
        print("\nStudent ID | Full name | Course/section | Average")
        for record in records:
            show_student(record)
    print(f"Total records: {len(records)}")


def add_student(records):
    student_id = read_text("Student ID: ")
    if find_student(records, student_id) is not None:
        print("That student ID already exists.")
        return
    record = {"id": student_id, "name": read_text("Full name: "),
              "section": read_text("Course/section: "), "average": read_average()}
    try:
        append_record(record)
    except (OSError, UnicodeError) as error:
        print(f"Cannot save the record: {error}")
        return
    records.append(record)
    print(f"Saved: {record['id']} | {record['name']} | {record['average']:.2f}")
    print(f"Total saved records: {len(records)}")


def search_student(records):
    record = find_student(records, read_text("Student ID to search: "))
    if record is None:
        print("Student not found.")
    else:
        print("Student found:")
        show_student(record)


def update_student(records):
    record = find_student(records, read_text("Student ID to update: "))
    if record is None:
        print("Student not found.")
        return
    print("Current information:")
    show_student(record)
    print("Press Enter to keep a value. The student ID stays the same.")
    updated = {"id": record["id"],
               "name": read_text("Full name: ", record["name"]),
               "section": read_text("Course/section: ", record["section"]),
               "average": read_average(record["average"])}

    index = records.index(record)
    revised = records.copy()
    revised[index] = updated
    try:
        save_records(revised)
    except (OSError, UnicodeError) as error:
        print(f"Cannot save the update: {error}")
        return
    # Save muna bago baguhin ang nasa memory.
    records[index] = updated
    print("Student updated and saved:")
    show_student(updated)


def main():
    print("P5 - Student Information File System")
    print("Jit Lee S. Romero | IV-BSIT C")
    try:
        records = load_records()
    except (OSError, ValueError, UnicodeError) as error:
        print(f"Cannot load students.txt: {error}")
        return
    print(f"Loaded records: {len(records)}")

    while True:
        print("\n1. Add and save a student\n2. Display all students"
              "\n3. Search by student ID\n4. Update a student"
              "\n5. Save all records\n6. Exit")
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

# Sanggunian: Bro Code Python course at Python docs (file I/O).
