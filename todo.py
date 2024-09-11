from tkinter import Tk, Entry, Button, Frame, Label
from tkinter import ttk

def add_task():
    task = entry.get()
    if task:
        todo_table.insert("", "end",values=(task,"Incomplete") )
        entry.delete(0, "end")

def delete_task():
    selected_item = todo_table.selection()
    if selected_item:
        todo_table.delete(selected_item)

def update_task():
    selected_item = todo_table.selection()
    if selected_item:
        task = entry.get()
        if task:
            todo_table.item(selected_item, text="", values=(task,"Incomplete"))
            entry.delete(0, "end")


# Creating the main window
window = Tk()
window.title("To-Do List")
window.geometry("400x500")
window.configure(bg="purple")

# Creating a label for the task entry field
entry_label = Label(window, text="Task:")
entry_label.pack()

# Creating the task entry field
entry = Entry(window)
entry.pack()

# Creating the buttons
button_frame = Frame(window)
button_frame.pack()

add_button = Button(button_frame, text="Add Task", command=add_task, bg="purple", fg="white")
add_button.grid(row=0, column=0, padx=5, pady=5)

delete_button = Button(button_frame, text="Delete Task", command=delete_task,  bg="purple", fg="white")
delete_button.grid(row=0, column=1, padx=5, pady=5)

update_button = Button(button_frame, text="Update Task", command=update_task,  bg="purple", fg="white")
update_button.grid(row=0, column=2, padx=5, pady=5)

# Creating the table
table_frame = Frame(window)
table_frame.pack(pady=10)

columns = ("Task", "State")
todo_table = ttk.Treeview(table_frame, columns=columns, show="headings")
todo_table.column("Task", width=200)
todo_table.column("State", width=200)
todo_table.heading("Task", text="Task")
todo_table.heading("State", text="State")
todo_table.pack()

#start the main event loop
window.mainloop()
