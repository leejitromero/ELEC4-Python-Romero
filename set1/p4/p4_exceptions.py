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
