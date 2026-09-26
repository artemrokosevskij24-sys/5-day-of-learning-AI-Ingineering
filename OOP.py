class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def print_info(self):
        print(f"{self.name}: {self.grade}")

    def update_grade(self, new_grade):
        if 1 <= new_grade <= 5:
            self.grade = new_grade
            print("Оценка была успешно обновлена")
        else:
            print("Ошибка: Оценка должна быть от 1 до 5")

student1 = Student("Artem", 5)
student2 = Student("Nikita", 3)
student3 = Student("Vlad", 4)

student2.update_grade(10)
student2.update_grade(4)

student1.print_info()
student2.print_info()
student3.print_info()