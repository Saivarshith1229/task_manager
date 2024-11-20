from task import Task

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description=""):
        task = Task(title, description)
        self.tasks.append(task)
        return len(self.tasks) - 1  # Return task index

    def view_tasks(self):
        if not self.tasks:
            print("\nNo tasks found!")
            return
        
        print("\nYour Tasks:")
        for i, task in enumerate(self.tasks):
            print(f"{i}. {task}")

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_complete()
            print(f"Task '{self.tasks[index].title}' marked as complete!")
        else:
            print("Invalid task index!")

def main():
    manager = TaskManager()
    
    while True:
        print("\n=== Task Manager ===")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Exit")
        
        choice = input("\nEnter your choice (1-4): ")
        
        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description (optional): ")
            manager.add_task(title, description)
            print("Task added successfully!")
            
        elif choice == "2":
            manager.view_tasks()
            
        elif choice == "3":
            manager.view_tasks()
            try:
                index = int(input("\nEnter task number to mark as complete: "))
                manager.complete_task(index)
            except ValueError:
                print("Please enter a valid number!")
                
        elif choice == "4":
            print("\nGoodbye!")
            break
            
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main() 