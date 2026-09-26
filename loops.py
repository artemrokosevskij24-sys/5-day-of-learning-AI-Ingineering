students = [
    {"name": "Артём", "grade": "5"},
    {"name": "Влад", "grade": "3"},
    {"name": "Макар", "grade": "4"},
    {"name": "Игорь", "grade": "4"},
    {"name": "Никита", "grade": "5"},
]

def print_student(student):
    print(f"{student['name']}: {student['grade']}")

for student in students:
    print_student(student)