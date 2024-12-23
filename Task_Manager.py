def task():
    tasks = []  # empty list
    print("WELCOME TO THE TASK MANAGEMENT APP")

    while True:
        try:
            total_task = int(input("Enter how many tasks you want to add: "))
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")

    for i in range(1, total_task + 1):
        task_name = input(f"Enter task {i}: ")
        tasks.append(task_name)

    print(f"Today's tasks are:\n{tasks}")

    while True:
        try:
            operation = int(input("Enter 1-Add\n2-Update\n3-Delete\n4-View\n5-Exit/Stop\n"))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")
            continue

        if operation == 1:
            add = input("Enter the task you want to add: ")
            tasks.append(add)
            print(f"Task '{add}' has been successfully added...")

        elif operation == 2:
            updated_val = input("Enter the task name you want to update: ")
            if updated_val in tasks:
                up = input("Enter new task: ")
                index = tasks.index(updated_val)
                tasks[index] = up
                print(f"Updated task to '{up}'")
            else:
                print("Task not found.")

        elif operation == 3:
            del_val = input("Which task do you want to delete: ")
            if del_val in tasks:
                index = tasks.index(del_val)
                del tasks[index]
                print(f"Task '{del_val}' has been deleted...")
            else:
                print("Task not found.")

        elif operation == 4:
            print(f"Total tasks: {tasks}")

        elif operation == 5:
            print("Closing the program...")
            break

        else:
            print("Invalid input. Please enter a number between 1 and 5.")

# Call the function to test it
task()

