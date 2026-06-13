import json
import os

FILE = "todo.json"

# Load tasks
def load_tasks():
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r") as f:
        return json.load(f)

# Save tasks
def save_tasks(tasks):
    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=4)

# Show tasks
def show_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return

    for i, task in enumerate(tasks, start=1):
        status = "Done" if task["done"] else "Not Done"
        print(f"{i}. {task['task']} [{status}]")

# Add task
def add_task(tasks):
    task = input("Enter task: ")
    tasks.append({"task": task, "done": False})
    print("Task added!")

# Delete task
def delete_task(tasks):
    show_tasks(tasks)
    try:
        index = int(input("Enter task number to delete: ")) - 1
        if index < 0 or index >= len(tasks):
            print("Task does not exist.")
            return
        tasks.pop(index)
        print("Task deleted!")
    except:
        print("Invalid input!")

# Mark completed
def mark_done(tasks):
    show_tasks(tasks)
    try:
        index = int(input("Enter task number to mark done: ")) - 1
        if index < 0 or index >= len(tasks):
            print("Task does not exist.")
            return
        tasks[index]["done"] = True
        print("Task marked as done!")
    except:
        print("Invalid input!")

# Main program
def main():
    tasks = load_tasks()

    while True:
        print("\n--- TO DO LIST ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Mark Task as Done")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            mark_done(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("Saved & Exiting...")
            break
        else:
            print("Invalid choice!")

        save_tasks(tasks)

main()