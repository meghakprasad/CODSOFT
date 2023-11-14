# To Do List Project
class ToDoList:
    def __init__(self):
        self.tasks = {}

    def add_task(self, task):
        task_id = len(self.tasks) + 1  # Unique identifier for the task
        self.tasks[task_id] = task

    def remove_task(self, task_id):
        if task_id in self.tasks:
            del self.tasks[task_id]
        else:
            print("Task not found.")

    def display_tasks(self):
        if len(self.tasks) != 0:
            for task_id, task in self.tasks.items():
                print(f"{task_id}. {task}")
        else:
            print("No tasks added yet.")

def run():
    to_do_list = ToDoList()

    while True:
        print("\n1. Add Task")
        print("2. Remove Task")
        print("3. Display Tasks")
        print("4. Quit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            task = input("Enter task: ")
            to_do_list.add_task(task)
            print('-------------------------------------')
        elif choice == "2":
            print("Your Tasks are:")
            to_do_list.display_tasks()
            task_id = input("Enter task ID to remove: ")
            if task_id.isdigit():
                to_do_list.remove_task(int(task_id))
            else:
                print("Invalid input. Task ID should be a number.")
            print('-------------------------------------')
        elif choice == "3":
            print("Your Tasks are:")
            to_do_list.display_tasks()
            print('-------------------------------------')
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    run()
