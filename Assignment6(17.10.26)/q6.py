# Question: A training institute needs a function that calculates the average
# marks of a student. Reject invalid marks and empty input.

print("By sanskriti saxena")

def calculate_average(*marks):
    if not marks:
        print("Invalid Input: No marks provided")
        return

    for mark in marks:
        if not isinstance(mark, (int, float)) or isinstance(mark, bool):
            print("Invalid Input: Marks must be numeric")
            return

        if mark < 0 or mark > 100:
            print("Invalid Marks:", mark)
            return

    total = sum(marks)
    average = total / len(marks)

    print("Marks:", marks)
    print("Total Marks:", total)
    print("Average Marks:", average)


calculate_average(85, 90, 78, 92, 88)
calculate_average(70, 80, 95)
calculate_average()
calculate_average(80, 110, 90)
calculate_average(80, "abc", 90)