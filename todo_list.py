
# =============================================================
#  INTERNSHIP TASK 1 — TO-DO LIST PROGRAM
#  Concepts Used: Lists, Functions, Loops, Conditionals,
#                 String Methods, While Loop, User Input
# =============================================================

# ──────────────────────────────────────────────
# CONCEPT 1: LIST — yahan tasks store honge
# ──────────────────────────────────────────────
# List ek collection hoti hai jisme hum multiple items
# ek saath store kar sakte hain.
# Empty brackets [] se ek khali list banti hai.
tasks = []


# ══════════════════════════════════════════════
# CONCEPT 2: FUNCTIONS — har kaam ka alag function
# Functions woh blocks hote hain jo ek specific kaam karte hain.
# def keyword se function banta hai.
# ══════════════════════════════════════════════

def add_task(task_name):
    """
    Yeh function ek naya task list mein add karta hai.
    :param task_name: jo task add karni hai (string)
    """
    # CONCEPT 3: .strip() — extra spaces hatao input se
    task_name = task_name.strip()

    # CONCEPT 4: CONDITIONAL (if/else) — check karo task khali toh nahi
    if task_name == "":
        print("  [!] Task Name Cannot be Empty\n")
        return

    # CONCEPT 5: .append() — list mein item add karna
    # Hum task ko ek dictionary ke roop mein save karte hain
    tasks.append({
        "name": task_name,
        "done": False
    })
    print(f"  [+] Task added: '{task_name}'\n")


def view_tasks():
    """
    Yeh function saari tasks print karta hai.
    """
    print("\n" + "=" * 45)
    print("       TO-DO LIST")
    print("=" * 45)

    # CONCEPT 6: len() — list ki length check karna
    if len(tasks) == 0:
        print("  (No Task ! Add some tasks first.)")
    else:
        # CONCEPT 7: FOR LOOP + enumerate()
        # enumerate() se hume index bhi milta hai saath mein item bhi
        for index, task in enumerate(tasks, start=1):
            # CONCEPT 8: Ternary expression
            status = "Done   " if task["done"] else "Pending"
            # CONCEPT 9: f-string
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

    # CONCEPT 11: .pop() — list se kisi index ka item nikalna
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


# ══════════════════════════════════════════════
# CONCEPT 12: MAIN FUNCTION + WHILE LOOP
# Program tab tak chalta rahe jab tak user exit na kare
# ══════════════════════════════════════════════

def main():
    print("\n===  Welcome to To-Do List Program  ===")

    # CONCEPT 13: WHILE LOOP
    while True:
        show_menu()

        # CONCEPT 14: input() — user se data lena
        choice = input("  Enter your choice (1-5): ").strip()

        if choice == "1":
            task_name = input("   Enter Task name: ")
            add_task(task_name)

        elif choice == "2":
            view_tasks()

        elif choice == "3":
            view_tasks()
            try:
                # CONCEPT 15: int() — string ko integer mein convert karna
                num = int(input("  Which task to complete? (enter number): "))
                complete_task(num)
            except ValueError:
                # CONCEPT 16: try/except — errors handle karna
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
            break  # CONCEPT: break — loop band karna

        else:
            print("  [!] Invalid choice! Please enter a number between 1 and 5.\n")


# CONCEPT 17: if __name__ == "__main__"
# Yeh check karta hai ke yeh file directly run ho rahi hai
if __name__ == "__main__":
    main()
