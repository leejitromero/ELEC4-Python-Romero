# Full Name: Jit Lee S. Romero
# Section: IV-BSIT C
# Activity: P6 - Recursion Toolkit
# Date: November 24, 2026


# Base case: factorial(0) returns 1.
# Recursive call: multiply n by factorial(n - 1).
def factorial(n):
    if n < 0:
        raise ValueError("Factorial needs a non-negative integer.")
    if n == 0:
        return 1
    return n * factorial(n - 1)


# Base cases: fibonacci(0) returns 0; fibonacci(1) returns 1.
# Recursive calls: add fibonacci(n - 1) and fibonacci(n - 2).
def fibonacci(n):
    if n < 0:
        raise ValueError("Fibonacci needs a non-negative integer.")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


# Base case: sum_numbers(0) returns 0.
# Recursive call: add n to sum_numbers(n - 1).
def sum_numbers(n):
    if n < 0:
        raise ValueError("The sum needs a non-negative integer.")
    if n == 0:
        return 0
    return n + sum_numbers(n - 1)


# Base cases: an empty list returns False; a matching first item returns True.
# Recursive call: search the remaining items after removing the first item.
def search(items, target):
    if not items:
        return False
    if items[0] == target:
        return True
    return search(items[1:], target)


def read_number(maximum):
    while True:
        try:
            number = int(input(f"Enter n (0-{maximum}): "))
            if 0 <= number <= maximum:
                return number
            print(f"Enter a whole number from 0 to {maximum}.")
        except ValueError:
            print("Invalid input. Enter a whole number.")


def main():
    print("P6 - Recursion Toolkit")
    print("Jit Lee S. Romero | IV-BSIT C")

    while True:
        print("\n1. Factorial")
        print("2. Fibonacci")
        print("3. Sum from 1 to n")
        print("4. Recursive search")
        print("5. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            number = read_number(100)
            print(f"Factorial of {number} = {factorial(number)}")
        elif choice == "2":
            # A small limit keeps the simple recursive calculation responsive.
            number = read_number(30)
            print(f"Fibonacci({number}) = {fibonacci(number)}")

            # This display loop is outside the recursive functions.
            terms = []
            for position in range(number):
                terms.append(fibonacci(position))
            print(f"First {number} terms, starting at F(0): {terms}")
        elif choice == "3":
            number = read_number(100)
            print(f"Sum from 1 to {number} = {sum_numbers(number)}")
        elif choice == "4":
            text = input("Enter items separated by commas: ")
            items = [item.strip() for item in text.split(",") if item.strip()]
            if len(items) > 100:
                print("Enter at most 100 items.")
                continue
            target = input("Enter the target (case-sensitive): ").strip()
            print(f"Found: {search(items, target)}")
        elif choice == "5":
            print("Recursion toolkit closed.")
            return
        else:
            print("Invalid choice. Enter a number from 1 to 5.")


if __name__ == "__main__":
    try:
        main()
    except (EOFError, KeyboardInterrupt):
        print("\nRecursion toolkit closed.")


# Learning references:
# https://www.youtube.com/watch?v=ix9cRaBkVe0
# https://docs.python.org/3/tutorial/controlflow.html#defining-functions
# https://docs.python.org/3/library/sys.html#sys.getrecursionlimit
