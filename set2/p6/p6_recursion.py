# Full Name: Jit Lee S. Romero
# Section: IV-BSIT C
# Activity: P6 - Recursion Toolkit
# Date: November 24, 2026


# Base case: kapag n=0, return 1. Recursive call: n * factorial(n-1).
def factorial(n):
    if n < 0:
        raise ValueError("Factorial needs a non-negative integer.")
    if n == 0:
        return 1
    return n * factorial(n - 1)


# Base cases: kapag n=0 o 1, return n. Recursive calls: F(n-1) + F(n-2).
def fibonacci(n):
    if n < 0:
        raise ValueError("Fibonacci needs a non-negative integer.")
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


# Base case: kapag n=0, return 0. Recursive call: n + sum_numbers(n-1).
def sum_numbers(n):
    if n < 0:
        raise ValueError("The sum needs a non-negative integer.")
    if n == 0:
        return 0
    return n + sum_numbers(n - 1)


# Base cases: empty=False, unang item na match=True. Recursive call: search sa natira.
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
        print("\n1. Factorial\n2. Fibonacci\n3. Sum from 1 to n"
              "\n4. Recursive search\n5. Exit")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            number = read_number(100)
            print(f"Factorial of {number} = {factorial(number)}")
        elif choice == "2":
            number = read_number(30)
            print(f"Fibonacci({number}) = {fibonacci(number)}")
            # Nasa labas ng recursive function ang loop na pang-display.
            terms = []
            for position in range(number):
                terms.append(fibonacci(position))
            print(f"First {number} terms, starting at F(0): {terms}")
        elif choice == "3":
            number = read_number(100)
            print(f"Sum from 1 to {number} = {sum_numbers(number)}")
        elif choice == "4":
            text = input("Enter items separated by commas: ")
            items = []
            for item in text.split(","):
                item = item.strip()
                if item:
                    items.append(item)
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

# Sanggunian: Bro Code Python course at Python docs (functions at recursion).
