# Student Marks Analyzer

def get_marks():
    n = int(input("Enter number of students: "))

    students = {}

    for i in range(n):
        name = input(f"Enter student {i+1} name: ")
        marks = float(input(f"Enter marks of {name}: "))
        students[name] = marks

    return students


def highest_marks(students):
    highest = max(students.values())
    topper = [name for name, mark in students.items() if mark == highest]
    return topper, highest


def lowest_marks(students):
    lowest = min(students.values())
    student = [name for name, mark in students.items() if mark == lowest]
    return student, lowest


def average_marks(students):
    return sum(students.values()) / len(students)


def above_average(students, avg):
    print("\nStudents Scoring Above Average")

    for name, marks in students.items():
        if marks > avg:
            print(name, "-", marks)


def main():

    students = get_marks()

    topper, high = highest_marks(students)
    low_student, low = lowest_marks(students)
    avg = average_marks(students)

    print("\n------ RESULT ------")
    print("Highest Marks :", high)
    print("Topper :", ", ".join(topper))

    print("Lowest Marks :", low)
    print("Lowest Scorer :", ", ".join(low_student))

    print("Average Marks :", round(avg, 2))

    above_average(students, avg)


main()