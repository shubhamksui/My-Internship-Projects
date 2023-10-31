class Task:
    def __init__(self, description, completed=False):
        self.description = description
        self.completed = completed

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)

    def mark_task_as_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].completed = True
        else:
            print("Invalid task index.")

    def update_task_description(self, index, new_description):
        if 0 <= index < len(self.tasks):
            self.tasks[index].description = new_description
        else:
            print("Invalid task index.")

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
        else:
            print("Invalid task index.")

    def list_tasks(self):
        for i, task in enumerate(self.tasks):
            status = "[X]" if task.completed else "[ ]"
            print(f"{i+1}. {status} {task.description}")

def main():
    todo_list = ToDoList()

    while True:
        print("\n===== To-Do List =====")
        todo_list.list_tasks()

        print("\nOptions:")
        print("1. Add Task")
        print("2. Mark Task as Completed")
        print("3. Update Task Description")
        print("4. Remove Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            description = input("Enter task description: ")
            todo_list.add_task(description)
        elif choice == "2":
            index = int(input("Enter the task index to mark as completed: ")) - 1
            todo_list.mark_task_as_completed(index)
        elif choice == "3":
            index = int(input("Enter the task index to update description: ")) - 1
            new_description = input("Enter the new description: ")
            todo_list.update_task_description(index, new_description)
        elif choice == "4":
            index = int(input("Enter the task index to remove: ")) - 1
            todo_list.remove_task(index)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()