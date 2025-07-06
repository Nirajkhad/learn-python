def display_menu():
    print("===== Todo list manager =====")
    print("1. Add task")
    print("2. View tasks")
    print("3. Edit task")
    print("4. Delete task")
    print("5. Exit")

def add_task(tasks):
    task = input("Enter task: ").strip()
    if not task:
        print("Task cannot be empty!")
        return
    tasks.append(task)
    print("Task added successfully!")

def view_tasks(tasks):
    if(len(tasks) == 0):
        print("No tasks found!")
        return
    for task in tasks:
        print(task)

def edit_task(tasks, old_task, new_task):
    if task_not_found(old_task, tasks):
        return
    index = tasks.index(old_task)
    tasks[index] = new_task
    print("Task updated successfully!")

def remove_task(tasks, task):    
    if task_not_found(task, tasks):
        return
    tasks.remove(task)
    print("Task removed successfully!")

def task_not_found(task, tasks):
    if task not in tasks:
        print("Task not found!")
        return True
    return False

tasks = []

while True:
    choice = input("Enter your choice: ")
    match(choice):
        case "1":
            add_task(tasks)
        case "2":
            view_tasks(tasks)
        case "3":
            old_task = input("Enter old task: ")
            new_task = input("Enter new task: ")
            edit_task(tasks, old_task, new_task)
        case "4":
            task = input("Enter task: ")
            remove_task(tasks, task)
        case "5":
            break
        case _:
            print("Invalid choice")