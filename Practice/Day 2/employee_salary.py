employees = []


def add_employee():
    emp = {}

    emp["id"] = input("Employee ID: ")
    emp["name"] = input("Employee Name: ")
    emp["salary"] = float(input("Employee Salary: "))

    employees.append(emp)


def display_employee():

    print("\nEmployee Details")

    for emp in employees:
        print(emp)


def highest_salary():

    if len(employees) == 0:
        return

    highest = max(employees, key=lambda x: x["salary"])

    print("\nHighest Salary Employee")
    print(highest)


while True:

    print("\nEmployee Salary Management")
    print("1. Add Employee")
    print("2. Display Employee")
    print("3. Highest Salary")
    print("4. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_employee()

    elif choice == "2":
        display_employee()

    elif choice == "3":
        highest_salary()

    elif choice == "4":
        break

    else:
        print("Invalid Choice")