# Full Name: Jit Lee S. Romero
# Section: IV-BSIT C
# Activity: P8 - Inheritance and Polymorphism
# Date: November 24, 2026


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"I am {self.name}, {self.age} years old.")


class Student(Person):
    def __init__(self, name, age, section):
        # Gamitin ang parent constructor para sa name at age.
        super().__init__(name, age)
        self.section = section

    def introduce(self):
        # Sariling introduction ng Student ang gagamitin.
        print(f"I am {self.name}, {self.age} years old, a student from {self.section}.")


def main():
    print("P8 - Inheritance and Polymorphism")
    print("Jit Lee S. Romero | IV-BSIT C")
    print()

    person = Person("Carlo Santos", 40)
    student = Student("Juan Cruz", 21, "IV-BSIT C")
    person.introduce()
    student.introduce()


if __name__ == "__main__":
    main()

# Sanggunian: Bro Code Python course at Python docs (inheritance).
