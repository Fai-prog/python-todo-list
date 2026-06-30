tasks = []
def add_task(task_name):
    task_name = task_name.strip()
    if task_name == "":
        print("  [!] Task Name Cannot be Empty\n")
        return
    tasks.append({
        "name": task_name,
        "done": False
    })
    print(f"  [+] Task added: '{task_name}'\n")


def view_tasks():
    print("\n" + "=" * 45)
    print("       TO-DO LIST")
    print("=" * 45)
    if len(tasks) == 0:
        print("  (No Task ! Add some tasks first.)")
    else:
        for index, task in enumerate(tasks, start=1):
            status = "Done   " if task["done"] else "Pending"
            print(f"  {index}. [{status}]  {task['name']}")

    print("=" * 45 + "\n")


def complete_task(task_number):
    """
    Yeh function kisi task ko done mark karta hai.
    """
    # CONCEPT 10: Validation — number range check
    if task_number < 1 or task_number > len(tasks):
        print("  [!] Invalid task number!\n")
        return

    task = tasks[task_number - 1]
    if task["done"]:
        print(f"  [i] '{task['name']}' Already complete!\n")
    else:
        task["done"] = True
        print(f"  [*] Congratulation! Task complete: '{task['name']}'\n")

def delete_task(task_number):
    """
    Yeh function kisi task ko list se hata deta hai.
    """
    if task_number < 1 or task_number > len(tasks):
        print("  [!] Invalid task number!\n")
        return
    removed = tasks.pop(task_number - 1)
    print(f"  [-] Task deleted: '{removed['name']}'\n")


def show_menu():
    print("\n----------------------------------")
    print("     TO-DO LIST  MAIN MENU")
    print("----------------------------------")
    print("  1. Add Task")
    print("  2. View Tasks")
    print("  3. Complete Task")
    print("  4. Delete Task")
    print("  5. Exit")
    print("----------------------------------")
def main():
    print("\n===  Welcome to To-Do List Program  ===")
    while True:
        show_menu()
        choice = input("  Enter your choice (1-5): ").strip()

        if choice == "1":
            task_name = input("   Enter Task name: ")
            add_task(task_name)

        elif choice == "2":
            view_tasks()

        elif choice == "3":
            view_tasks()
            try:
                num = int(input("  Which task to complete? (enter number): "))
                complete_task(num)
            except ValueError:
                print("  [!] Please enter a valid number!\n")

        elif choice == "4":
            view_tasks()
            try:
                num = int(input("  Which task to delete? (enter number): "))
                delete_task(num)
            except ValueError:
                print("  [!] Please enter a valid number!\n")

        elif choice == "5":
            print("\n  Great Work! Take care.\n")
            break  

        else:
            print("  [!] Invalid choice! Please enter a number between 1 and 5.\n")
if __name__ == "__main__":
    main()
