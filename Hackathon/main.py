# main.py
# This is the main file for the CLI Todo App.
# Handles menu, task operations, and uses storage.py for saving/loading.

from storage import load_tasks, save_tasks
import datetime

# Global task list and next ID
tasks = []
next_id = 1

# ================= Menu =================
def show_menu():
    print("\n==================== TODO APP ====================")
    print("1. Add Task")
    print("2. List Tasks")
    print("3. Update Task")
    print("4. Mark Task as Done/Undone")
    print("5. Delete Task")
    print("6. Exit")
    print("===================================================")

# ================= Add Task =================
def add_task():
    global next_id
    title = input("Enter task title: ").strip()
    if title:
        task = {
            "id": next_id,
            "title": title,
            "status": "pending",
            "created_at": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # readable format
        }
        tasks.append(task)
        next_id += 1
        save_tasks(tasks, next_id)
        print(f'Task "{title}" added successfully!')
    else:
        print("Title cannot be empty. Task not added.")

# ================= List Tasks =================
def list_tasks():
    print("\n--- Your Tasks ---")
    if not tasks:
        print("No tasks found. Add your first task!")
        return
    for task in tasks:
        status_display = "Done" if task['status'] == "done" else "Not Done"
        created_at_display = f" (Created: {task.get('created_at')})" if task.get('created_at') else ""
        print(f"[{task['id']}] \"{task['title']}\" [{status_display}]{created_at_display}")

# ================= Update Task =================
def update_task():
    try:
        task_id = int(input("Enter the ID of the task to update: "))
        task_to_update = None
        for task in tasks:
            if task['id'] == task_id:
                task_to_update = task
                break

        if task_to_update:
            print(f'Current title: "{task_to_update["title"]}"')
            new_title = input("Enter the new title (or press Enter to keep the current one): ").strip()
            if new_title:
                task_to_update['title'] = new_title
                save_tasks(tasks, next_id)
                print(f'Task updated successfully to "{new_title}"!')
            else:
                print("No changes made.")
        else:
            print("Task not found.")
    except ValueError:
        print("Invalid ID. Please enter a number.")

# ================= Mark Task Done/Undone =================
def mark_task_done():
    try:
        task_id = int(input("Enter the ID of the task to mark as done/undone: "))
        task_to_toggle = None
        for task in tasks:
            if task['id'] == task_id:
                task_to_toggle = task
                break

        if task_to_toggle:
            if task_to_toggle['status'] == "pending":
                task_to_toggle['status'] = "done"
                print(f'Task "{task_to_toggle["title"]}" marked as Done!')
            else:
                task_to_toggle['status'] = "pending"
                print(f'Task "{task_to_toggle["title"]}" marked as Pending!')
            save_tasks(tasks, next_id)
        else:
            print("Task not found.")
    except ValueError:
        print("Invalid ID. Please enter a number.")

# ================= Delete Task =================
def delete_task():
    global next_id
    try:
        task_id = int(input("Enter the ID of the task to delete: "))

        for task in tasks:
            if task['id'] == task_id:
                tasks.remove(task)

                # Reassign IDs to remaining tasks
                for index, task in enumerate(tasks, start=1):
                    task['id'] = index

                # Update next_id
                next_id = len(tasks) + 1

                save_tasks(tasks, next_id)
                print(f'Task deleted successfully! IDs updated.')
                return

        print("Task not found.")

    except ValueError:
        print("nvalid ID. Please enter a number.")

# ================= Main Function =================
def main():
    global tasks, next_id
    # Load tasks from storage
    tasks, next_id = load_tasks()

    while True:
        show_menu()
        choice = input("Choose an option: ").strip()

        if choice == '1':
            add_task()
        elif choice == '2':
            list_tasks()
        elif choice == '3':
            update_task()
        elif choice == '4':
            mark_task_done()
        elif choice == '5':
            delete_task()
        elif choice == '6':
            print("Exiting To-Do List. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Entry point
if __name__ == "__main__":
    main()
