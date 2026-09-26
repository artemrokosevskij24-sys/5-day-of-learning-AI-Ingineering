class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        if 1 <= grade <= 5:
            self.grades.append(grade)
            print(f"Оценка {grade} добавлена")
        else:
            print("Ошибка: оценка должна быть от 1 до 5!")

    def get_average(self):
        if len(self.grades) == 0:
            return 0
        return sum(self.grades) / len(self.grades)



student1 = Student("Artem")

student1.add_grade(5)
student1.add_grade(4)
student1.add_grade(5)

avg = student1.get_average()
print(f"Средний балл Артёма: {avg:.2f}")