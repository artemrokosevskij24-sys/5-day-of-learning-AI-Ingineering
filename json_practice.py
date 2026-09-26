import json

students = [
    {"name": "Артем", "grade": "5"},
    {"name": "Влад", "grade": "3"},
    {"name": "Макар", "grade": "4"},
    {"name": "Игорь", "grade": "4"},
    {"name": "Никита", "grade": "5"},
]

with open("students.json", "w", encoding="utf-8") as file:
    json.dump(students, file, ensure_ascii=False, indent=4)

with open("students.json", "r", encoding="utf-8") as file:
    loaded_students = json.load(file)

for student in loaded_students:
    print(f"{student['name']}: {student['grade']}")