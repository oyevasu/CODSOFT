class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task}' added.")

    def update_task(self, index, new_task):
        if 0 <= index < len(self.tasks):
            old_task = self.tasks[index]
            self.tasks[index] = new_task
            print(f"Task updated from '{old_task}' to '{new_task}'.")
        else:
            print("Invalid task index.")

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            task = self.tasks.pop(index)
            print(f"Task '{task}' deleted.")
        else:
            print("Invalid task index.")

    def display_tasks(self):
        if self.tasks:
            print("Your To-Do List:")
            for i, task in enumerate(self.tasks):
                print(f"{i+1}. {task}")
        else:
            print("Your To-Do List is empty.")

def main():
    todo_list = ToDoList()

    while True:
        print("\n1. Add task")
        print("2. Update task")
        print("3. Delete task")
        print("4. Display tasks")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == '2':
            todo_list.display_tasks()
            index = int(input("Enter the task number to update: ")) - 1
            new_task = input("Enter the new task: ")
            todo_list.update_task(index, new_task)
        elif choice == '3':
            todo_list.display_tasks()
            index = int(input("Enter the task number to delete: ")) - 1
            todo_list.delete_task(index)
        elif choice == '4':
            todo_list.display_tasks()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()