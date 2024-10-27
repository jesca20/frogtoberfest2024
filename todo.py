def add_task(tasks):
    task = input("Enter a new task: ")
    tasks.append(task)
    print("Task added.")

def view_tasks(tasks):
    print("Your tasks:")
    for idx, task in enumerate(tasks, start=1):
        print(f"{idx}. {task}")

tasks = []
while True:
    action = input("Enter 'add' to add a task, 'view' to view tasks, or 'quit' to exit: ").lower()
    if action == 'add':
        add_task(tasks)
    elif action == 'view':
        view_tasks(tasks)
    elif action == 'quit':
        break
    else:
        print("Invalid input.")
