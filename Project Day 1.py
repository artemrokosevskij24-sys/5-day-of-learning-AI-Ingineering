import json
students = [
    {"name": "Артем", "grade": 5},
    {"name": "Влад", "grade": 3},
    {"name": "Макар", "grade": 4},
    {"name": "Игорь", "grade": 4},
    {"name": "Никита", "grade": 5},
]
def get_status(grade):
    if grade == 5:
        return "Отлично"
    elif grade == 4:
        return "Хорошо"
    elif grade == 3:
        return "Удовлитворительно"
    else:
        return "Плохо"
for student in students:
    status = get_status(student["grade"])
    student["status"] = status 
    print (f"{student["name"]}: {student["grade"]} - {status}")
with open("report.json", "w", encoding="utf-8") as file:
    json.dump(students, file, ensure_ascii=False, indent=4)
with open("report.json", "r", encoding="utf-8") as file:
    loaded_students = json.load(file)
for student in loaded_students:
    if student["status"] == "Отлично":
        print(student["name"])