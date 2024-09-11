import tkinter as tk

# Function to update the input field with the button press
def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(number))

# Function to perform the calculation
def calculate():
    expression = entry.get()
    try:
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Create the main window
window = tk.Tk()
window.title("Casio Calculator")

# Create the input field
entry = tk.Entry(window, width=25, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Create buttons for digits
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+"
]

# Add the buttons to the grid
row = 1
col = 0
for button in buttons:
    button = tk.Button(window, text=button, padx=20, pady=10, font=("Arial", 12, "bold"), bd=4,
                       command=lambda button=button: button_click(button))
    button.grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Create the equal button
equal_button = tk.Button(window, text="=", padx=20, pady=10, font=("Arial", 12, "bold"), bd=4,
                         command=calculate)
equal_button.grid(row=row, column=col, padx=5, pady=5)

# Start the main event loop
window.mainloop()