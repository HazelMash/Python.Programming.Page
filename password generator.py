import random
import string
import tkinter as tk

def generate_password():
    length = int(length_entry.get())
    complexity = complexity_var.get()

    characters = ''

    if complexity == '1':
        characters = string.ascii_letters + string.digits
    elif complexity == '2':
        characters = string.ascii_letters + string.digits + string.punctuation
    elif complexity == '3':
        characters = string.ascii_letters + string.digits + string.punctuation + ' '

    password = ''.join(random.choice(characters) for _ in range(length))
    password_label.config(text="Generated Password: " + password)

# Create the Tkinter window
window = tk.Tk()
window.title("Password Generator")

# Create the input labels and entry fields
length_label = tk.Label(window, text="Password Length:")
length_label.pack()
length_entry = tk.Entry(window)
length_entry.pack()

complexity_label = tk.Label(window, text="Password Complexity:")
complexity_label.pack()

# Create the complexity radio buttons
complexity_var = tk.StringVar()
complexity_var.set("1")

radio_button_1 = tk.Radiobutton(window, text="Letters and Digits", variable=complexity_var, value="1")
radio_button_1.pack()

radio_button_2 = tk.Radiobutton(window, text="Letters, Digits, and Symbols", variable=complexity_var, value="2")
radio_button_2.pack()

radio_button_3 = tk.Radiobutton(window, text="Letters, Digits, Symbols, and Spaces", variable=complexity_var, value="3")
radio_button_3.pack()

# Create the generate button
generate_button = tk.Button(window, text="Generate Password", command=generate_password)
generate_button.pack()

# Create the result label
password_label = tk.Label(window, text="")
password_label.pack()

# Start the Tkinter event loop
window.mainloop()