# Question: Create a student result function that accepts the student's name,
# any number of subject marks, and additional information such as roll number
# and semester.

print("By sanskriti saxena")

def student_result(name, *marks, **details):
    print("Student Name:", name)

    if marks:
        total = sum(marks)
        average = total / len(marks)

        print("Subject Marks:", marks)
        print("Total Marks:", total)
        print("Average Marks:", average)
    else:
        print("No subject marks provided")

    print("Additional Details:")

    for key, value in details.items():
        print(key.capitalize() + ":", value)


student_result(
    "Sanskriti",
    85, 90, 88, 92, 95,
    roll_number=101,
    semester=3
)

student_result(
    "Agrim",
    78, 82, 89,
    roll_number=102,
    semester=5
)