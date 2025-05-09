class Task:
    def __init__(self, task_name):
        self.task_name = task_name
        self.status = "pending"

    def mark_completed(self):
        self.status = "completed"

    def __str__(self):
        return f"Task: {self.task_name}, Status: {self.status}"


class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task.task_name}' added to the todo list.")

    def remove_task(self, remove_task):
        if remove_task in self.tasks:
            self.tasks.remove(remove_task)
            print(f"Task '{remove_task.task_name}' removed from the todo list.")
        else:
            print(f"Task '{remove_task.task_name}' not found in the todo list.")

    def view_tasks(self):
        print("\nYour Todo List:")
        for task in self.tasks:
            print(task)

    def mark_task_completed(self, task):
        if task in self.tasks:
            task.mark_completed()
            print(f"Task '{task.task_name}' marked as completed.")
        else:
            print(f"Task '{task.task_name}' not found in the todo list.")


# Create a todo list
todo_list = TodoList()

# Create tasks
task1 = Task("Learn Python OOP")
task2 = Task("Build Todo List App")
task3 = Task("Read a Book")

# Add tasks to the todo list
todo_list.add_task(task1)
todo_list.add_task(task2)
todo_list.add_task(task3)

# View tasks
todo_list.view_tasks()

# Mark a task as done
todo_list.mark_task_completed(task1)

# View tasks again to see updated status
todo_list.view_tasks()

# Remove a task
todo_list.remove_task(task2)

# View tasks again after removing one
todo_list.view_tasks()
