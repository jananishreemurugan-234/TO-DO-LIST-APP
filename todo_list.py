import tkinter as tk
from tkinter import messagebox
import json
import os

# ------------------ File Name ------------------
TASKS_FILE = "tasks.json"

# ------------------ Functions ------------------
def load_tasks():
    """Load tasks from JSON file"""
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as f:
            return json.load(f)
    return []

def save_tasks():
    """Save tasks to JSON file"""
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f)

def refresh_listbox():
    """Refresh listbox display"""
    listbox.delete(0, tk.END)
    for index, task in enumerate(tasks):
        status = "✔" if task["completed"] else "✗"
        listbox.insert(tk.END, f"{index+1}. {task['title']} [{status}]")

def add_task():
    """Add a new task"""
    title = entry.get().strip()
    if title == "":
        messagebox.showwarning("Warning", "Task cannot be empty!")
        return
    tasks.append({"title": title, "completed": False})
    entry.delete(0, tk.END)
    refresh_listbox()
    save_tasks()

def delete_task():
    """Delete selected task"""
    selected = listbox.curselection()
    if not selected:
        messagebox.showwarning("Warning", "Select a task to delete!")
        return
    index = selected[0]
    tasks.pop(index)
    refresh_listbox()
    save_tasks()

def mark_complete():
    """Mark selected task as complete"""
    selected = listbox.curselection()
    if not selected:
        messagebox.showwarning("Warning", "Select a task to mark complete!")
        return
    index = selected[0]
    tasks[index]["completed"] = True
    refresh_listbox()
    save_tasks()

def edit_task():
    """Edit selected task"""
    selected = listbox.curselection()
    if not selected:
        messagebox.showwarning("Warning", "Select a task to edit!")
        return
    index = selected[0]
    new_title = entry.get().strip()
    if new_title == "":
        messagebox.showwarning("Warning", "Task cannot be empty!")
        return
    tasks[index]["title"] = new_title
    entry.delete(0, tk.END)
    refresh_listbox()
    save_tasks()

# ------------------ GUI Setup ------------------
root = tk.Tk()
root.title("To-Do List App")
root.geometry("400x400")
root.resizable(False, False)

# Entry Box
entry = tk.Entry(root, width=30, font=("Arial", 12))
entry.pack(pady=10)

# Buttons
frame = tk.Frame(root)
frame.pack(pady=5)

add_btn = tk.Button(frame, text="Add Task", width=12, command=add_task)
add_btn.grid(row=0, column=0, padx=5)

edit_btn = tk.Button(frame, text="Edit Task", width=12, command=edit_task)
edit_btn.grid(row=0, column=1, padx=5)

delete_btn = tk.Button(frame, text="Delete Task", width=12, command=delete_task)
delete_btn.grid(row=1, column=0, padx=5, pady=5)

mark_btn = tk.Button(frame, text="Mark Complete", width=12, command=mark_complete)
mark_btn.grid(row=1, column=1, padx=5, pady=5)

# Task List
listbox = tk.Listbox(root, width=50, height=15, font=("Arial", 12))
listbox.pack(pady=10)

# ------------------ Load Initial Data ------------------
tasks = load_tasks()
refresh_listbox()

# ------------------ Main Loop ------------------
root.mainloop()