import tkinter as tk

def on_click(btn_text):
    current_text = display_var.get()

    if btn_text == "=":
        try:
            result = eval(current_text)
            display_var.set(str(result))
        except Exception as e:
            display_var.set("Error")
    elif btn_text == "C":
        display_var.set("")
    else:
        display_var.set(current_text + btn_text)

# Create the main application window
app = tk.Tk()
app.title("Simple Calculator")
app.geometry("300x400")
app.resizable(False, False)

# Variable to hold the current expression
display_var = tk.StringVar()

# Entry widget to display the expression
entry_display = tk.Entry(app, textvariable=display_var, font=("Arial", 20), bd=5, relief=tk.RIDGE, justify=tk.RIGHT)
entry_display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Define the button texts
button_texts = [
    ("7", "8", "9", "/"),
    ("4", "5", "6", "*"),
    ("1", "2", "3", "-"),
    ("C", "0", "=", "+")
]

# Create and place the buttons
for row_idx, button_row in enumerate(button_texts):
    for col_idx, button_text in enumerate(button_row):
        button = tk.Button(app, text=button_text, font=("Arial", 18), bd=3, relief=tk.RIDGE, width=5, height=2,
                           command=lambda text=button_text: on_click(text))
        button.grid(row=row_idx + 1, column=col_idx, padx=5, pady=5)

# Start the main event loop
app.mainloop()
