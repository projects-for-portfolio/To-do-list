# Import the tkinter module for GUI applications and messagebox for displaying warnings
import tkinter as tk
from tkinter import messagebox
import json  # Import the json module to handle saving and loading tasks from a file

# Define a class to manage the to-do list
class TodoList: 
    def __init__(self, filename="tasks.json"):
        self.filename = filename  # Name of the file where tasks are stored
        self.tasks = self.load_tasks()  # Load existing tasks from the file
        # self.remove_task1 = self.remove_task()

    def load_tasks(self):
        # Try to open the file and load tasks, if file not found return an empty list
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)# loads json file and reads from it
        except FileNotFoundError:
            return []

    def save_tasks(self):
        # Save the current tasks to the file
        with open(self.filename, 'w') as file:
            json.dump(self.tasks, file, indent=4)

    def add_task(self, task):
        self.tasks.append(task)  # Add a new task to the list
        self.save_tasks()  # Save the updated list to the file

    def remove_task(self, task):
        # Remove a task from the list if it exists
        if task in self.tasks:
            self.tasks.remove(task)
            self.save_tasks()  # Save the updated list to the file

# Define the main application class for the to-do list GUI
class TodoApp:
    def __init__(self, root):
        self.root = root  # Reference to the root Tkinter window
        self.root.title("To-Do List Application")  # Set the window title
        root.config(bg='lightblue')
        self.todo_list = TodoList()  # Create an instance of TodoList to manage tasks

        

        # Create a frame to hold the widgets
        self.frame = tk.Frame(root)
        self.frame.pack(pady=10)
        self.frame.config(bg='#368f5f')

        # Create an entry widget for inputting new tasks
        self.task_entry = tk.Entry(self.frame, width=35)
        self.task_entry.grid(row=0, column=0, padx=10)
        self.task_entry.config(bg='#eeeae1')


        # Create a button to add the task entered in the entry widget
        self.add_task_button = tk.Button(self.frame, text="Add Task", command=self.add_task)
        self.add_task_button.grid(row=0, column=1)
        self.add_task_button.config(bg='gray')

        # Create a listbox to display the tasks
        self.tasks_listbox = tk.Listbox(self.frame, width=50, height=15)
        self.tasks_listbox.grid(row=1, column=0, columnspan=2, pady=10)
        self.tasks_listbox.config(bg='#f1ac85')


        # Create a button to remove the selected task from the listbox
        self.remove_task_button = tk.Button(self.frame, text="Remove Task", command=self.remove_task)
        self.remove_task_button.grid(row=2, column=0, columnspan=2, pady=5)

        # Load existing tasks into the listbox
        self.load_tasks()

    def add_task(self):
        task = self.task_entry.get()  # Get the task from the entry widget
        if task:  # Check if the task is not empty
            self.todo_list.add_task(task)  # Add the task to the list
            self.tasks_listbox.insert(tk.END, task)  # Insert the task into the listbox
            self.task_entry.delete(0, tk.END)  # Clear the entry widget
        else:
            messagebox.showwarning("Warning", "You must enter a task.")  # Show a warning if the entry is empty

    def remove_task(self):
        try:
            selected_task_index = self.tasks_listbox.curselection()[0]  # Get the index of the selected task
            selected_task = self.tasks_listbox.get(selected_task_index)  # Get the task text
            self.todo_list.remove_task(selected_task)  # Remove the task from the list
            self.tasks_listbox.delete(selected_task_index)  # Remove the task from the listbox
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task to remove.")  # Show a warning if no task is selected

    def load_tasks(self):
        # Load tasks from the TodoList instance and insert them into the listbox
        for task in self.todo_list.tasks:
            self.tasks_listbox.insert(tk.END, task)

# Run the application
if __name__ == "__main__":
    root = tk.Tk()  # Create the root Tkinter window
    app = TodoApp(root)  # Create an instance of the TodoApp class
    root.mainloop()  # Start the Tkinter event loop
