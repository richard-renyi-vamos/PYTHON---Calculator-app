

User
create a calculator app in python with a blue GUI
ChatGPT
Sure, I can guide you through creating a simple calculator app with a blue graphical user interface (GUI) using Python and the Tkinter library. Here's an example:

Firstly, make sure you have Tkinter installed. It usually comes pre-installed with Python, but if you need to install it separately, you can use pip:

bash
Copy code
pip install tk
Now, here's a basic structure for your calculator app:

python
Copy code
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
This code creates a simple calculator interface with blue background color. Run this Python script, and it will open a calculator window with a basic GUI. You can extend and customize it further according to your preferences.

Remember, this is a basic calculator; in production, you'd want to handle various edge cases and errors more gracefully. Also, using eval() for calculation might have security implications, so be cautious when using it, especially in scenarios that involve user input.

Feel free to tweak the design, layout, or functionality to suit your preferences!





