# Question: Create a function that accepts a student's name and course.
# If the course is not provided, use "Python Programming" as the default value.

print("By sanskriti saxena")

def student_greeting(name, course="Python Programming"):
    print("Hello", name + "!")
    print("Welcome to", course)

student_greeting("Sanskriti")
student_greeting("Agrim", "Artificial Intelligence")