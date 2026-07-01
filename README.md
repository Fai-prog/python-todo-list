# 📝 To-Do List — Python CLI App

> A command-line To-Do List application built with core Python concepts.

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


## 🖥️ Sample Output

```
===  Welcome TO-DO list Programm!  ===

----------------------------------
     TO-DO LIST  MAIN MENU
----------------------------------
  1. Add Task 
  2. View Task
  3. Complete Task
  4. Task Delete
  5. Exit
----------------------------------
  Enter Your Choice (1-5): 1
  Enter the name of Task: Finish Python Assignment
  [+] Task added: 'Finish Python Assignment'

=============================================
       TO-DO LIST
=============================================
  1. [Pending]  Finish Python Assignment
=============================================
```



---

## 🎯 Key Takeaway

> This project demonstrates how **lists act as the foundation of databases** — storing structured records that can be created, read, updated, and deleted (CRUD). These are the same operations used in real-world applications and backend systems.

---

## 👨‍💻 Author

Faiza Ashraf 
Internship Trainee | Python Fundamentals Track  

---

*Built with ❤️ and Python 🐍*
