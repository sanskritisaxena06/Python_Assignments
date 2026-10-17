# Question: Create a function that accepts any number of employee details,
# such as department, salary, city, and experience.

print("By sanskriti saxena")

def employee_details(**kwargs):
    print("Employee Details:")

    for key, value in kwargs.items():
        print(key.capitalize() + ":", value)


employee_details(
    name="Sanskriti",
    department="AI/ML",
    salary=50000,
    city="Bareilly",
    experience=2
)

employee_details(
    name="Agrim",
    department="IT",
    salary=60000,
    city="Noida"
)