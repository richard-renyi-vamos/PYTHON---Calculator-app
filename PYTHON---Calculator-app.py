import tkinter as tk

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def clear():
    entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Blue Calculator")

# Configure background color
root.configure(bg="blue")

# Create entry widget for input and display
entry = tk.Entry(root, width=25, font=('Arial', 14))
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Button labels
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

# Create and place calculator buttons
row = 1
col = 0
for button in buttons:
    if button == '=':
        tk.Button(root, text=button, width=5, command=calculate).grid(row=row, column=col)
    elif button == '0':
        tk.Button(root, text=button, width=12, command=lambda b=button: entry.insert(tk.END, b)).grid(row=row, column=col, columnspan=2)
    else:
        tk.Button(root, text=button, width=5, command=lambda b=button: entry.insert(tk.END, b)).grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Clear button
tk.Button(root, text="C", width=5, command=clear).grid(row=row, column=0, columnspan=2)

root.mainloop()
