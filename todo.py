import os
import json
from datetime import datetime

class TodoList:
    def __init__(self):
        self.tasks = []
        self.file_path = "todolist.json"

    def load_data(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, "r") as file:
                self.tasks = json.load(file)

    def save_data(self):
        with open(self.file_path, "w") as file:
            json.dump(self.tasks, file, indent=2)

    def display_tasks(self):
        if not self.tasks:
            print("No tasks in the to-do list.")
        else:
            print("To-Do List:")
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. {task['description']} - {'Done' if task['done'] else 'Not Done'}")

    def add_task(self, description):
        new_task = {"description": description, "done": False, "created_at": str(datetime.now())}
        self.tasks.append(new_task)
        print(f"Task '{description}' added to the to-do list.")

    def mark_task_as_done(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            self.tasks[task_index - 1]["done"] = True
            print(f"Task '{self.tasks[task_index - 1]['description']}' marked as done.")
        else:
            print("Invalid task index.")

    def run(self):
        self.load_data()

        while True:
            print("\n1. Display Tasks")
            print("2. Add Task")
            print("3. Mark Task as Done")
            print("4. Exit")

            choice = input("Enter your choice (1-4): ")

            if choice == "1":
                self.display_tasks()
            elif choice == "2":
                description = input("Enter task description: ")
                self.add_task(description)
            elif choice == "3":
                task_index = int(input("Enter the task index to mark as done: "))
                self.mark_task_as_done(task_index)
            elif choice == "4":
                self.save_data()
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    todo_app = TodoList()
    todo_app.run()