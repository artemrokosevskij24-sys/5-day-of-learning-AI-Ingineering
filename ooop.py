class Student:
    def __init__(self, name):
        self.name = name
        self.__grades = []
    @property
    def grades(self):
        return list(self.__grades)

    def add_grade(self, grade):
        if 1 <= grade <= 5:
            self.__grades.append(grade)
            print(f"Оценка {grade} добавлена")
        else:
            print("Ошибка: оценка должна быть от 1 до 5!")

    def get_average(self):
        if len(self.__grades) == 0:
            return 0
        return sum(self.__grades) / len(self.__grades)

    def get_info(self):
        return f"{self.name} | Средний балл: {self.get_average():.2f}"

    def print_info(self):
        print(self.get_info())

class GraduateStudent(Student):
    def __init__(self, name, thesis_topic):
        super().__init__(name)
        self.thesis_topic = thesis_topic

    def get_info(self):
        return f"{super().get_info()} | Тема диссертации: {self.thesis_topic}"

student1 = Student("Artem")
student1.add_grade(5)
student1.add_grade(4)
student1.add_grade(5)

student2 = GraduateStudent("Makar", "Разработка AI-агентов")
student2.add_grade(5)
student2.add_grade(5)

student1.print_info()

student2.print_info()

student1.__grades = [10, 20, 30]
student1.print_info()

print(f"Оценки через @property: {student1.grades}")

student1.grades = [10, 20, 30]