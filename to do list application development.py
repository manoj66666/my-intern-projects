# To-Do List Application

# Define data structures to store tasks and completed tasks
tasks = []
completed_tasks = []

# Function to add a task
def add_task():
    description = input("Enter task description: ")
    due_date = input("Enter due date (optional): ")
    priority = input("Enter priority (optional): ")

    task = {
        "description": description,
        "due_date": due_date,
        "priority": priority
    }
    tasks.append(task)
    print("Task added successfully!")

# Function to display tasks
def display_tasks():
    if not tasks:
        print("No tasks in the to-do list.")
    else:
        print("To-Do List:")
        for index, task in enumerate(tasks):
            print(f"{index + 1}. {task['description']} (Due: {task['due_date']}, Priority: {task['priority']})")

# Function to mark a task as completed
def mark_completed():
    display_tasks()
    task_index = int(input("Enter the task number to mark as completed: ")) - 1

    if 0 <= task_index < len(tasks):
        completed_task = tasks.pop(task_index)
        completed_tasks.append(completed_task)
        print("Task marked as completed!")
    else:
        print("Invalid task number.")

# Function to update a task
def update_task():
    display_tasks()
    task_index = int(input("Enter the task number to update: ")) - 1

    if 0 <= task_index < len(tasks):
        task = tasks[task_index]
        print("Current Task Details:")
        print(f"Description: {task['description']}")
        print(f"Due Date: {task['due_date']}")
        print(f"Priority: {task['priority']}")

        description = input("Enter new task description (press Enter to keep current): ")
        due_date = input("Enter new due date (press Enter to keep current): ")
        priority = input("Enter new priority (press Enter to keep current): ")

        if description:
            task['description'] = description
        if due_date:
            task['due_date'] = due_date
        if priority:
            task['priority'] = priority

        print("Task updated successfully!")
    else:
        print("Invalid task number.")

# Function to remove a task
def remove_task():
    display_tasks()
    task_index = int(input("Enter the task number to remove: ")) - 1

    if 0 <= task_index < len(tasks):
        removed_task = tasks.pop(task_index)
        print("Task removed successfully!")
    else:
        print("Invalid task number.")

# Main loop
while True:
    print("\nTo-Do List Menu:")
    print("1. Add Task")
    print("2. Display Tasks")
    print("3. Mark Task as Completed")
    print("4. Update Task")
    print("5. Remove Task")
    print("6. Quit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_task()
    elif choice == '2':
        display_tasks()
    elif choice == '3':
        mark_completed()
    elif choice == '4':
        update_task()
    elif choice == '5':
        remove_task()
    elif choice == '6':
        break
    else:
        print("Invalid choice. Please try again.")
