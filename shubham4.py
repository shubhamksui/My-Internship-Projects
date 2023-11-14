import os

# File to store the tasks
todo_file = "todo.txt"
completed_file = "completed.txt"

# Check if the task files exist, if not, create them
if not os.path.exists(todo_file):
    with open(todo_file, "w") as f:
        pass

if not os.path.exists(completed_file):
    with open(completed_file, "w") as f:
        pass


def add_task():
    description = input("Enter the task description: ")
    due_date = input("Enter due date of the task (optional): ")
    priority = input("Enter the priority of the task (optional): ")

    task = (f"{description} | Due: {due_date} | Priority: {priority}\n")

    with open(todo_file, "a") as f:
        f.write(task)
    print("Task added successfully.")


def display_tasks():
    print("\nTasks:")
    with open(todo_file, "r") as f:
        tasks = f.readlines()
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task.strip()}")
    print("\nCompleted Tasks:")
    with open(completed_file, "r") as f:
        completed_tasks = f.readlines()
        for i, task in enumerate(completed_tasks, start=1):
            print(f"{i}. {task.strip()}")


def mark_completed():
    display_tasks()
    task_number = int(input("Enter the number of the task to mark as completed: ")) - 1

    with open(todo_file, "r") as f:
        tasks = f.readlines()

    if 0 <= task_number < len(tasks):
        completed_task = tasks.pop(task_number)
        with open(todo_file, "w") as f:
            f.writelines(tasks)
        with open(completed_file, "a") as f:
            f.write(completed_task)
        print("Task marked as completed.")
    else:
        print("Invalid task number.")


def update_task():
    display_tasks()
    task_number = int(input("Enter the number of the task to be updated: ")) - 1

    with open(todo_file, "r") as f:
        tasks = f.readlines()

    if 0 <= task_number < len(tasks):
        description = input("Enter the updated task description: ")
        due_date = input("Enter the updated due date (optional): ")
        priority = input("Enter the updated priority (optional): ")

        updated_task = f"{description} | Due: {due_date} | Priority: {priority}\n"
        tasks[task_number] = updated_task

        with open(todo_file, "w") as f:
            f.writelines(tasks)
        print("Task updated successfully.")
    else:
        print("Invalid task number.")


def remove_task():
    display_tasks()
    task_number = int(input("Enter the number of the task to remove: ")) - 1

    with open(todo_file, "r") as f:
        tasks = f.readlines()

    if 0 <= task_number < len(tasks):
        removed_task = tasks.pop(task_number)

        with open(todo_file, "w") as f:
            f.writelines(tasks)
        print("Task removed successfully.")
    else:
        print("Invalid task number.")


# Main loop
while True:
    print("\nTo-Do List Application")
    print("1. Add Task")
    print("2. Display Tasks")
    print("3. Mark Task as Completed")
    print("4. Update Task")
    print("5. Remove Task")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        display_tasks()
    elif choice == "3":
        mark_completed()
    elif choice == "4":
        update_task()
    elif choice == "5":
        remove_task()
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
