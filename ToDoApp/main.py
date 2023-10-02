import tkinter as tk
from tkinter import messagebox

LIGHT_MODE = {
    "BG_COLOR": "white",
    "TEXT_COLOR": "black",
    "BTN_COLOR": "#d3d3d3"
}

DARK_MODE = {
    "BG_COLOR": "black",
    "TEXT_COLOR": "white",
    "BTN_COLOR": "#444444"
}

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        
        # Start by initializing the theme.
        self.current_mode = self.load_theme()

        # Create a listbox to display tasks
        self.tasks_listbox = tk.Listbox(root, width=100, height=20, selectmode=tk.SINGLE)
        self.tasks_listbox.pack(pady=0)

        # Create entry to add tasks
        self.task_entry = tk.Entry(root, width=100)
        self.task_entry.pack(pady=5)

        # Buttons to manage tasks
        self.add_button = tk.Button(root, text="Add Task", width=20, command=self.add_task)
        self.add_button.pack(pady=5)

        self.delete_button = tk.Button(root, text="Delete Task", width=20, command=self.delete_task)
        self.delete_button.pack(pady=5)

        self.clear_button = tk.Button(root, text="Clear All Tasks", width=20, command=self.clear_tasks)
        self.clear_button.pack(pady=5)

        self.theme_button = tk.Button(root, text="Switch Theme", width=20, command=self.toggle_theme)
        self.theme_button.pack(pady=5)

        self.load_tasks()

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
            self.save_tasks()
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def delete_task(self):
        try:
            selected_task_index = self.tasks_listbox.curselection()[0]
            self.tasks_listbox.delete(selected_task_index)
            self.save_tasks()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to delete.")

    def clear_tasks(self):
        self.tasks_listbox.delete(0, tk.END)
        self.save_tasks()

    def save_tasks(self):
        tasks = self.tasks_listbox.get(0, tk.END)
        with open("tasks.txt", "w") as f:
            for task in tasks:
                f.write(task + "\n")

    def load_tasks(self):
        try:
            with open("tasks.txt", "r") as f:
                tasks = f.readlines()
                for task in tasks:
                    self.tasks_listbox.insert(tk.END, task.strip())
        except FileNotFoundError:
            pass

    def apply_theme(self, theme):
        self.root.configure(bg=theme["BG_COLOR"])
        self.tasks_listbox.configure(bg=theme["BG_COLOR"], fg=theme["TEXT_COLOR"])
        self.task_entry.configure(bg=theme["BG_COLOR"], fg=theme["TEXT_COLOR"])
        self.add_button.configure(bg=theme["BTN_COLOR"], fg=theme["TEXT_COLOR"])
        self.delete_button.configure(bg=theme["BTN_COLOR"], fg=theme["TEXT_COLOR"])
        self.clear_button.configure(bg=theme["BTN_COLOR"], fg=theme["TEXT_COLOR"])
        self.theme_button.configure(bg=theme["BTN_COLOR"], fg=theme["TEXT_COLOR"])
        
    def save_theme(self):
        with open("theme_pref.txt", "w") as file:
            if self.current_mode == LIGHT_MODE:
                file.write("LIGHT_MODE")
            else:
                file.write("DARK_MODE")

    def load_theme(self):
        try:
            with open("theme_pref.txt", "r") as file:
                theme = file.read().strip()
                if theme == "LIGHT_MODE":
                    return LIGHT_MODE
                else:
                    return DARK_MODE
        except FileNotFoundError:
            # Default theme if no preference is found
            return LIGHT_MODE

    def toggle_theme(self):
        if self.current_mode == LIGHT_MODE:
            self.apply_theme(DARK_MODE)
            self.current_mode = DARK_MODE
        else:
            self.apply_theme(LIGHT_MODE)
            self.current_mode = LIGHT_MODE
            
        self.save_theme()
    
if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
