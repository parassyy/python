import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Calculator")
root.geometry("410x520")
root.configure(bg="#f0f0f0")
root.resizable(False, False)

# Entry field
entry = tk.Entry(root, font=("Arial", 24), borderwidth=2, relief="solid", justify="right")
entry.grid(row=0, column=0, columnspan=4, ipady=15, padx=10, pady=20)

# Global expression string
expression = ""

# Button click handler
def on_click(symbol):
    global expression
    expression += str(symbol)
    entry.delete(0, tk.END)
    entry.insert(tk.END, expression)

# Equal (=) button handler
def calculate():
    global expression
    try:
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
        expression = str(result)
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")
        expression = ""

# Clear (C) button handler
def clear():
    global expression
    expression = ""
    entry.delete(0, tk.END)

# Button layout
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
]

for (text, row, col) in buttons:
    if text == "=":
        btn = tk.Button(root, text=text, width=5, height=2, font=("Arial", 18), bg="#4CAF50", fg="white", command=calculate)
    else:
        btn = tk.Button(root, text=text, width=5, height=2, font=("Arial", 18), command=lambda t=text: on_click(t))
    btn.grid(row=row, column=col, padx=5, pady=5)

# Clear button (separate row)
clear_btn = tk.Button(root, text="C", width=22, height=2, font=("Arial", 18), bg="#f44336", fg="white", command=clear)
clear_btn.grid(row=5, column=0, columnspan=4, padx=10, pady=10)

# Start the app
root.mainloop()
