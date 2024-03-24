class Task:
    def __init__(self, name, description, status='Pending'):
        self.name = name
        self.description = description
        self.status = status

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def view_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        else:
            print("To-Do List:")
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. {task.name} - {task.description} - Status: {task.status}")

    def update_task_status(self, index, new_status):
        if 0 < index <= len(self.tasks):
            self.tasks[index - 1].status = new_status
            print("Task status updated successfully.")
        else:
            print("Invalid task index.")

    def delete_task(self, index):
        if 0 < index <= len(self.tasks):
            del self.tasks[index - 1]
            print("Task deleted successfully.")
        else:
            print("Invalid task index.")

def main():
    todo_list = ToDoList()

    while True:
        print("\n=== To-Do List Application ===")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task Status")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter task name: ")
            description = input("Enter task description: ")
            task = Task(name, description)
            todo_list.add_task(task)
            print("Task added successfully.")

        elif choice == '2':
            todo_list.view_tasks()

        elif choice == '3':
            index = int(input("Enter index of task to update status: "))
            new_status = input("Enter new status (e.g., Completed, In Progress, Pending): ")
            todo_list.update_task_status(index, new_status)

        elif choice == '4':
            index = int(input("Enter index of task to delete: "))
            todo_list.delete_task(index)

        elif choice == '5':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
