import json

students = [
    {"name": "Артем", "grade": "5"},
    {"name": "Влад", "grade": "3"},
    {"name": "Макар", "grade": "4"},
    {"name": "Игорь", "grade": "4"},
    {"name": "Никита", "grade": "5"},
]

with open("students.txt", "w", encoding="utf-8") as file:
    for student in students:
        file.write(f"{student['name']}: {student['grade']}\n")

with open("students.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(content)
