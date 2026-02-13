# Console-based To-Do List Application
# Tasks stored in list and saved to text file

FILE_NAME = "tasks.txt"


# Load tasks from file
def load_tasks():
    tasks = []
    try:
        with open(FILE_NAME, "r") as file:
            tasks = [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        pass
    return tasks


# Save tasks to file
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")


# View tasks
def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks found.")
        return
    print("\nYour Tasks:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")


# Add task
def add_task(tasks):
    task = input("Enter new task: ").strip()
    if task:
        tasks.append(task)
        save_tasks(tasks)
        print("Task added.")
    else:
        print("Empty task not added.")


# Remove task
def remove_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        num = int(input("Enter task number to remove: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            save_tasks(tasks)
            print(f"Removed: {removed}")
        else:
            print("Invalid number.")
    except ValueError:
        print("Enter a valid number.")


# Main menu loop
def main():
    tasks = load_tasks()

    while True:
        print("\n==== TO-DO LIST ====")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
