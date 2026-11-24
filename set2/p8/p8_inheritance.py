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


class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def introduce(self):
        print(f"I am {self.name}, {self.age} years old, a teacher of {self.subject}.")


def main():
    print("P8 - Inheritance and Polymorphism")
    print("Jit Lee S. Romero | IV-BSIT C")
    print()

    people = [
        Person("Carlo Santos", 40),
        Student("Juan Cruz", 21, "IV-BSIT C"),
        Teacher("Ana Reyes", 35, "Python Programming"),
    ]

    # Parehong method ang tawag, pero depende sa object ang output.
    for person in people:
        person.introduce()


if __name__ == "__main__":
    main()

# Sanggunian: Bro Code Python course at Python docs (inheritance).
# Ang Student at Teacher ay nagmana ng name at age mula sa Person.
# Ginamit ang super().__init__() para ma-set ang common attributes sa parent.
# Bawat child class ay may sariling attribute at sariling introduce() method.
# Sa isang list, tinatawag ang introduce() pero iba ang output bawat class, kaya may polymorphism.
