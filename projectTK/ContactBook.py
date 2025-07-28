import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector

# MySQL Connection
conn=mysql.connector.connect(database="db1",
                           user="root",
                           password="system",
                           host="localhost",
                           port="3306")
cursor = conn.cursor()

# Window Setup
root = tk.Tk()
root.title("Contact Book")
root.geometry("700x500")
root.config(bg="#f0f0f0")

# Title
tk.Label(root, text="Contact Book", font=("Arial", 24, "bold"), bg="#f0f0f0", fg="green").pack(pady=10)

# Entry Frame
frame = tk.Frame(root, bg="#f0f0f0")
frame.pack(pady=10)

tk.Label(frame, text="Name", font=("Arial", 14), bg="#f0f0f0").grid(row=0, column=0, padx=10, pady=5)
tk.Label(frame, text="Phone", font=("Arial", 14), bg="#f0f0f0").grid(row=1, column=0, padx=10, pady=5)
tk.Label(frame, text="Email", font=("Arial", 14), bg="#f0f0f0").grid(row=0, column=2, padx=10, pady=5)
tk.Label(frame, text="Address", font=("Arial", 14), bg="#f0f0f0").grid(row=1, column=2, padx=10, pady=5)

name_entry = tk.Entry(frame, font=("Arial", 14), width=20)
phone_entry = tk.Entry(frame, font=("Arial", 14), width=20)
email_entry = tk.Entry(frame, font=("Arial", 14), width=20)
address_entry = tk.Entry(frame, font=("Arial", 14), width=20)

name_entry.grid(row=0, column=1)
phone_entry.grid(row=1, column=1)
email_entry.grid(row=0, column=3)
address_entry.grid(row=1, column=3)

# Treeview for contacts
tree = ttk.Treeview(root, columns=("ID", "Name", "Phone", "Email", "Address"), show="headings", height=10)
tree.heading("ID", text="ID")
tree.heading("Name", text="Name")
tree.heading("Phone", text="Phone")
tree.heading("Email", text="Email")
tree.heading("Address", text="Address")
tree.pack(pady=20)

# Scrollbar
scroll = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
tree.configure(yscrollcommand=scroll.set)
scroll.place(x=680, y=170, height=230)

# Functions
def clear_fields():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()
    if not name or not phone or not email:
        messagebox.showwarning("Input Error", "Name, Phone, and Email are required.")
        return
    try:
        cursor.execute("INSERT INTO contacts (name, phone, email, address) VALUES (%s, %s, %s, %s)",
                       (name, phone, email, address))
        conn.commit()
        messagebox.showinfo("Success", "Contact Added Successfully!")
        clear_fields()
        show_contacts()
    except Exception as e:
        messagebox.showerror("Error", str(e))

def delete_contact():
    selected = tree.selection()
    if not selected:
        messagebox.showwarning("Select Contact", "Please select a contact to delete.")
        return
    contact_id = tree.item(selected[0])["values"][0]
    cursor.execute("DELETE FROM contacts WHERE id=%s", (contact_id,))
    conn.commit()
    show_contacts()

def show_contacts():
    tree.delete(*tree.get_children())
    cursor.execute("SELECT * FROM contacts")
    for row in cursor.fetchall():
        tree.insert("", tk.END, values=row)

# Button Frame
btn_frame = tk.Frame(root, bg="#f0f0f0")
btn_frame.pack()

tk.Button(btn_frame, text="Add Contact", font=("Arial", 14), bg="#4CAF50", fg="white", command=add_contact).grid(row=0, column=0, padx=10)
tk.Button(btn_frame, text="Delete Contact", font=("Arial", 14), bg="#f44336", fg="white", command=delete_contact).grid(row=0, column=1, padx=10)
tk.Button(btn_frame, text="Clear Fields", font=("Arial", 14), bg="#2196F3", fg="white", command=clear_fields).grid(row=0, column=2, padx=10)

# Load data on start
show_contacts()

root.mainloop()
