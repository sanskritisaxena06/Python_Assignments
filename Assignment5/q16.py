# Q16. Find names of students who scored 60 or more.
print("By sanskriti Saxena")
students = [
    {"name": "Amit", "marks": 75},
    {"name": "Rahul", "marks": 45},
    {"name": "Neha", "marks": 90},
    {"name": "Rohit", "marks": 55}
]
result = [student["name"] for student in students if student["marks"] >= 60]
print(result)
print("saxenasanskriti")