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
        print("3. Exit")
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
            print("Recursion toolkit closed.")
            return
        else:
            print("Invalid choice. Enter 1, 2, or 3.")


if __name__ == "__main__":
    try:
        main()
    except (EOFError, KeyboardInterrupt):
        print("\nRecursion toolkit closed.")


# Learning references:
# https://www.youtube.com/watch?v=ix9cRaBkVe0
# https://docs.python.org/3/tutorial/controlflow.html#defining-functions
# https://docs.python.org/3/library/sys.html#sys.getrecursionlimit
