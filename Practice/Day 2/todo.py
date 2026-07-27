tasks = []

while True:

    print("\nTODO APP")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)

    elif choice == "2":

        if len(tasks) == 0:
            print("No Tasks")

        else:
            for i, task in enumerate(tasks, 1):
                print(i, task)

    elif choice == "3":

        for i, task in enumerate(tasks, 1):
            print(i, task)

        index = int(input("Task Number: "))
        tasks.pop(index - 1)

    elif choice == "4":
        break

    else:
        print("Invalid Choice")