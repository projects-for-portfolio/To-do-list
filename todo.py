import os

class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

    def mark_as_completed(self):
        self.completed = True

    def __str__(self):
        status = "✓" if self.completed else "✗"
        return f"[{status}] {self.description}"

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        self.tasks.append(Task(description))

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]

    def mark_task_as_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_as_completed()

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the to-do list.")
        for i, task in enumerate(self.tasks):
            print(f"{i + 1}. {task}")

def main():
    todo_list = ToDoList()

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("To-Do List Application")
        print("----------------------")
        print("1. Add a task")
        print("2. Remove a task")
        print("3. Mark a task as completed")
        print("4. View tasks")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            description = input("Enter the task description: ")
            todo_list.add_task(description)
        elif choice == '2':
            index = int(input("Enter the task number to remove: ")) - 1
            todo_list.remove_task(index)
        elif choice == '3':
            index = int(input("Enter the task number to mark as completed: ")) - 1
            todo_list.mark_task_as_completed(index)
        elif choice == '4':
            todo_list.view_tasks()
            input("Press Enter to continue...")
        elif choice == '5':
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
