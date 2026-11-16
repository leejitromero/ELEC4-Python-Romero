# Full Name: Jit Lee S. Romero
# Section: IV-BSIT C
# Activity: P4 - Safe Menu Program
# Date: November 16, 2026


def divide_numbers():
    try:
        first_number = float(input("Enter the first number: "))
        second_number = float(input("Enter the second number: "))
        result = first_number / second_number
    except ValueError:
        print("Invalid number. Please enter numeric values.")
    except ZeroDivisionError:
        print("Cannot divide by zero.")
    else:
        # The else block runs only when the try block succeeds.
        print(f"Result: {first_number:g} / {second_number:g} = {result:g}")
    finally:
        # The finally block runs whether the operation succeeds or fails.
        print("Division attempt finished.")


def open_text_file():
    try:
        file_name = input("Enter the text file name or path: ").strip()
        with open(file_name, "r", encoding="utf-8") as text_file:
            contents = text_file.read()
    except FileNotFoundError:
        print("File not found. Please check the file name or path.")
    except UnicodeDecodeError:
        print("Cannot read this file as UTF-8 text.")
    except (OSError, ValueError):
        # Also handle other file errors, such as a folder or an invalid path.
        print("Cannot open this file. Check the path and permissions.")
    else:
        print("\n--- File Contents ---")
        print(contents)
    finally:
        print("File opening attempt finished.")


def main():
    print("P4 - Safe Menu Program")

    while True:
        print("\nJit Lee S. Romero | IV-BSIT C | P4")
        print("1. Divide two numbers")
        print("2. Open a text file")
        print("3. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            divide_numbers()
        elif choice == "2":
            open_text_file()
        elif choice == "3":
            print("Thank you for using the safe menu program!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
