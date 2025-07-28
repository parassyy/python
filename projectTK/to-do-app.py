import tkinter as tk
from tkinter import messagebox, ttk
import mysql.connector
from datetime import datetime

# Database Connection
cn=mysql.connector.connect(database="todo_db",
                           user="root",
                           password="system",
                           host="localhost",
                           port="3306")
cursor = cn.cursor()

# Main Window
root = tk.Tk()
root.title("To-Do List")
root.geometry("600x500")
root.config(bg="#f2f2f2")

# Title
tk.Label(root, text="To-Do List App", font=("Arial", 24, "bold"), bg="#f2f2f2", fg="green").pack(pady=20)

# Entry Frame
entry_frame = tk.Frame(root, bg="#f2f2f2")
entry_frame.pack(pady=10)

tk.Label(entry_frame, text="Task Name:", font=("Arial", 14), bg="#f2f2f2").grid(row=0, column=0, padx=10, pady=5)
task_entry = tk.Entry(entry_frame, width=30, font=("Arial", 14))
task_entry.grid(row=0, column=1, padx=10)

tk.Label(entry_frame, text="Due Date (YYYY-MM-DD):", font=("Arial", 14), bg="#f2f2f2").grid(row=1, column=0, padx=10, pady=5)
date_entry = tk.Entry(entry_frame, width=30, font=("Arial", 14))
date_entry.grid(row=1, column=1, padx=10)

# Treeview for Tasks
tree = ttk.Treeview(root, columns=("ID", "Task", "Due Date", "Done"), show="headings", height=10)
tree.heading("ID", text="ID")
tree.heading("Task", text="Task")
tree.heading("Due Date", text="Due Date")
tree.heading("Done", text="Completed")
tree.pack(pady=20)

# Scrollbar
scrollbar = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.place(x=580, y=180, height=225)

# Functions
def load_tasks():
    tree.delete(*tree.get_children())
    cursor.execute("SELECT * FROM todo_tasks")
    for row in cursor.fetchall():
        tree.insert("", tk.END, values=(row[0], row[1], row[2], "Yes" if row[3] else "No"))

def add_task():
    task = task_entry.get()
    due = date_entry.get()
    if not task or not due:
        messagebox.showwarning("Input Error", "All fields are required!")
        return
    try:
        datetime.strptime(due, '%Y-%m-%d')  # Validate date
        cursor.execute("INSERT INTO todo_tasks (task_name, due_date) VALUES (%s, %s)", (task, due))
        cn.commit()
        messagebox.showinfo("Success", "Task added!")
        task_entry.delete(0, tk.END)
        date_entry.delete(0, tk.END)
        load_tasks()
    except Exception as e:
        messagebox.showerror("Error", str(e))

def mark_done():
    selected = tree.selection()
    if not selected:
        messagebox.showwarning("Select Task", "Please select a task to mark as done.")
        return
    task_id = tree.item(selected[0])["values"][0]
    cursor.execute("UPDATE todo_tasks SET is_done=1 WHERE id=%s", (task_id,))
    cn.commit()
    load_tasks()

def delete_task():
    selected = tree.selection()
    if not selected:
        messagebox.showwarning("Select Task", "Please select a task to delete.")
        return
    task_id = tree.item(selected[0])["values"][0]
    cursor.execute("DELETE FROM todo_tasks WHERE id=%s", (task_id,))
    cn.commit()
    load_tasks()

# Buttons
button_frame = tk.Frame(root, bg="#f2f2f2")
button_frame.pack(pady=10)

tk.Button(button_frame, text="Add Task", font=("Arial", 14), bg="#4CAF50", fg="white", command=add_task).grid(row=0, column=0, padx=10)
tk.Button(button_frame, text="Mark as Done", font=("Arial", 14), bg="#2196F3", fg="white", command=mark_done).grid(row=0, column=1, padx=10)
tk.Button(button_frame, text="Delete Task", font=("Arial", 14), bg="#f44336", fg="white", command=delete_task).grid(row=0, column=2, padx=10)

# Initial Load
load_tasks()

root.mainloop()
