import tkinter as tk

def click(event):
    global expression
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(expression)
            input_var.set(result)
            expression = str(result)
        except Exception as e:
            input_var.set("Error")
            expression = ""
    elif text == "C":
        expression = ""
        input_var.set("")
    else:
        expression += text
        input_var.set(expression)

# Initialize main window
root = tk.Tk()
root.title("Calculator")
root.geometry("600x600")

expression = ""
input_var = tk.StringVar()

# Entry widget for display
entry = tk.Entry(root, textvar=input_var, font="Arial 20", bd=12, relief=tk.SUNKEN, justify=tk.RIGHT)
entry.pack(fill=tk.BOTH, ipadx=18, pady=18, padx=18)

# Button frame
button_frame = tk.Frame(root)
button_frame.pack()

# Button layout
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"]
]

for row in buttons:
    frame = tk.Frame(button_frame)
    frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    for btn_text in row:
        btn = tk.Button(frame, text=btn_text, font="Arial 15", relief=tk.RAISED, bd=3)
        btn.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        btn.bind("<Button-1>", click)

root.mainloop()