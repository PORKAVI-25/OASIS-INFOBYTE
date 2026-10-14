def main():
    tasks = []
    while True:
        print("\\n=== To-Do List Manager ===")
        print("1. Add task")
        print("2. View tasks")
        print("3. Remove task")
        print("4. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            task = input("Enter task: ").strip()
            if task:
                tasks.append(task)
                print("Task added.")
            else:
                print("Task cannot be empty.")
        elif choice == "2":
            if not tasks:
                print("No tasks yet.")
            else:
                for index, task in enumerate(tasks, start=1):
                    print(f"{index}. {task}")
        elif choice == "3":
            if not tasks:
                print("There are no tasks to remove.")
                continue
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")
            try:
                number = int(input("Task number to remove: "))
                removed = tasks.pop(number - 1)
                print(f"Removed: {removed}")
            except (ValueError, IndexError):
                print("Please enter a valid task number.")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Choose 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
