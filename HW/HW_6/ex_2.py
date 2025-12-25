"""
Група вимог 2
формування резюме для будь-якої персони
"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_resume(self):
        return f"Ім'я: {self.name}, Вік: {self.age}"

class Student(Person):
    def __init__(self, name, age, university):
        super().__init__(name, age)
        self.university = university

    def make_resume(self):
        return f"Студент: {self.name}, {self.age} років, ВНЗ: {self.university}"

class Worker(Person):
    def __init__(self, name, age, job):
        super().__init__(name, age)
        self.job = job

    def make_resume(self):
        return f"Працівник: {self.name}, {self.age} років, Посада: {self.job}"

if __name__ == "__main__":
    people = [
        Student("Маргарита", 20, "ХНУРЕ"),
        Worker("Іван", 35, "Інженер")

    ]

    for p in people:
        print(p.make_resume())