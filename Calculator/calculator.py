import tkinter as tk

def click(event):
    current = str(entry.get())
    entry.delete(0, tk.END)
    entry.insert(0, current + str(event.widget["text"]))

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

root = tk.Tk()
root.title("Simple Calculator")
root.geometry("400x400")

entry = tk.Entry(root, font=("Arial", 20), bd=10, relief=tk.RIDGE, justify="right")
entry.pack(fill=tk.BOTH, ipadx=8, pady=10, padx=10)

buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "%", "+"],
    ["C", "="]
]

for row in buttons:
    frame = tk.Frame(root)
    frame.pack(expand=True, fill="both")
    for btn in row:
        button = tk.Button(frame, text=btn, font=("Arial", 18), bd=5)
        button.pack(side="left", expand=True, fill="both")
        if btn == "C":
            button.config(command=clear)
        elif btn == "=":
            button.config(command=calculate)
        else:
            button.bind("<Button-1>", click)

#for keyboard
def key_input(event):
    key = event.char
    if key in '0123456789+-*/.':
        entry.insert(tk.END, key)
    elif key == '\r':  # Enter key
        calculate()
    elif key == '\x08':  # Backspace
        current = entry.get()[:-1]
        entry.delete(0, tk.END)
        entry.insert(0, current)

root.bind("<Key>", key_input)

#theme
dark_mode = False

def toggle_theme():
    global dark_mode
    dark_mode = not dark_mode
    bg_color = "#333333" if dark_mode else "#ffffff"
    fg_color = "#ffffff" if dark_mode else "#000000"
    entry.config(bg=bg_color, fg=fg_color, insertbackground=fg_color)
    for frame in root.winfo_children():
        if isinstance(frame, tk.Frame):
            for widget in frame.winfo_children():
                if isinstance(widget, tk.Button):
                    widget.config(bg=bg_color, fg=fg_color)

theme_btn = tk.Button(root, text="Toggle Dark Mode", command=toggle_theme)
theme_btn.pack(pady=5)

#history check
history = []

def calculate():
    try:
        expr = entry.get()
        result = eval(expr)
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
        history.append(f"{expr} = {result}")
        update_history()
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def update_history():
    listbox.delete(0, tk.END)
    for item in history[-5:][::-1]:  # show last 5
        listbox.insert(tk.END, item)

listbox = tk.Listbox(root, height=5)
listbox.pack(pady=5, fill=tk.BOTH)


root.mainloop()
