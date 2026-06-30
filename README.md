# 📝 To-Do List — Python CLI App

> **Internship Task 1** | A command-line To-Do List application built with core Python concepts.

---

## 📌 About the Project

This is a simple yet fully functional **To-Do List program** built in Python as part of my internship training.  
The goal was to understand how to store, manage, and display data using Python's built-in data structures and control flow tools — without relying on any external libraries.

Users can **add**, **view**, **complete**, and **delete** tasks — all from an interactive command-line menu that keeps running until they choose to exit.

---

## ✨ Features

- ➕ Add tasks with custom names
- 📋 View all tasks with their status (`Pending` / `Done`)
- ✔️ Mark any task as complete
- 🗑️ Delete tasks from the list
- ⚠️ Input validation and error handling (no crashes on bad input)
- 🔁 Continuous menu loop — runs until user exits

---

## 🐍 Python Concepts Covered

| Concept | How It's Used |
|---|---|
| **Lists** | Stores all tasks as a collection |
| **Dictionaries** | Each task holds a `name` and `done` status |
| **Functions** | Code split into reusable blocks (`add_task`, `view_tasks`, etc.) |
| **while loop** | Keeps the menu running continuously |
| **for loop + enumerate()** | Displays tasks with numbering |
| **if / elif / else** | Handles menu choices and validations |
| **try / except** | Prevents crashes on invalid (non-numeric) input |
| **f-strings** | Clean, readable string formatting |
| **`.append()` / `.pop()`** | Adding and removing items from the list |
| **`.strip()`** | Cleans up extra whitespace from user input |
| **`int()` type conversion** | Converts string input to integer |
| **`__name__ == "__main__"`** | Entry point best practice |

---

## 🚀 How to Run

Make sure you have **Python 3.x** installed.

```bash
# Clone the repository
git clone https://github.com/your-username/todo-list-python.git

# Navigate into the folder
cd todo-list-python

# Run the program
python todo_list.py
```

---

## 🖥️ Sample Output

```
===  To-Do List Program mein Khush Aamdeed!  ===

----------------------------------
     TO-DO LIST  MAIN MENU
----------------------------------
  1. Task Add Karo
  2. Tasks Dekho
  3. Task Complete Karo
  4. Task Delete Karo
  5. Exit
----------------------------------
  Apna choice enter karo (1-5): 1
  Task ka naam likho: Finish Python Assignment
  [+] Task add ho gayi: 'Finish Python Assignment'

=============================================
       TO-DO LIST
=============================================
  1. [Pending]  Finish Python Assignment
=============================================
```

---

## 📂 Project Structure

```
todo-list-python/
│
├── todo_list.py      # Main program file
└── README.md         # Project documentation
```

---

## 🎯 Key Takeaway

> This project demonstrates how **lists act as the foundation of databases** — storing structured records that can be created, read, updated, and deleted (CRUD). These are the same operations used in real-world applications and backend systems.

---

## 👨‍💻 Author

**Ashra**  
Internship Trainee | Python Fundamentals Track  

---

*Built with ❤️ and Python 🐍*
