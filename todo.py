tasks = []

try:
    with open("tasks.txt", "r") as file:
        for line in file:
            tasks.append(line.strip())
except FileNotFoundError:
    pass

while True:
    print("\n=== TO-DO APP ===")
    print("1. Add task")
    print("2. View tasks")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter a new task: ")
        tasks.append(task)
        print("Task added!")

    elif choice == "2":
        print("\nYour Tasks:")
        for task in tasks:
            print("-", task)

    elif choice == "3":
     with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")
     print("Tasks saved. Goodbye!")
     break
