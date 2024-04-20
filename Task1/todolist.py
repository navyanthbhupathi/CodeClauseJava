import tkinter
from tkinter import messagebox
import random

# Initialize the tkinter window
root = tkinter.Tk()
root.configure(bg='#f0f0f0')
root.title('To-Do List')
root.attributes('-fullscreen', True)  # Make the window full screen
tasks = []
completed_tasks = []

# Function to update the listbox with tasks
def update_listbox():
    clear_listbox()
    for task in tasks:
        lb_tasks.insert("end", task)

# Function to clear the listbox
def clear_listbox():
    lb_tasks.delete(0, "end")

# Function to add a task to the list
def add_task():
    task = txt_input.get().strip()
    if task != '':
        tasks.append(task)
        update_listbox()
    else:
        messagebox.showwarning("Warning", "Please enter a task!")
    txt_input.delete(0, 'end')

# Function to delete a task from the list
def delete_task():
    try:
        task_index = lb_tasks.curselection()[0]
        del tasks[task_index]
        update_listbox()
        messagebox.showinfo("Info", "Task deleted!")
    except IndexError:
        messagebox.showwarning("Warning", "No task selected!")

# Function to update a task in the list
def update_task():
    try:
        task_index = lb_tasks.curselection()[0]
        task = txt_input.get().strip()
        if task != '':
            tasks[task_index] = task
            update_listbox()
            messagebox.showinfo("Info", "Task updated!")
        else:
            messagebox.showwarning("Warning", "Please enter a task!")
    except IndexError:
        messagebox.showwarning("Warning", "No task selected!")

# Function to choose a random task from the list
def choose_random():
    if tasks:
        task = random.choice(tasks)
        messagebox.showinfo("Random Task", task)
    else:
        messagebox.showwarning("Warning", "No tasks available!")

# Function to display the number of tasks
def number_of_tasks():
    number_of_tasks = len(tasks)
    messagebox.showinfo("Number of Tasks", f"Number of tasks: {number_of_tasks}")

# Function to mark a task as completed
def mark_completed():
    try:
        task_index = lb_tasks.curselection()[0]
        task = tasks[task_index]
        del tasks[task_index]
        completed_tasks.append(task)
        update_listbox()
        messagebox.showinfo("Info", "Task marked as completed!")
    except IndexError:
        messagebox.showwarning("Warning", "No task selected!")

# Function to display completed tasks
def view_completed():
    if completed_tasks:
        messagebox.showinfo("Completed Tasks", "\n".join(completed_tasks))
    else:
        messagebox.showinfo("Info", "No tasks completed yet!")

# Function to display pending tasks
def view_pending():
    if tasks:
        messagebox.showinfo("Pending Tasks", "\n".join(tasks))
    else:
        messagebox.showinfo("Info", "No pending tasks!")

# Function to exit the application
def exit_app():
    if messagebox.askokcancel("Exit", "Are you sure you want to exit?"):
        root.destroy()

# Title label
title = tkinter.Label(root, text="To-Do List", bg='#f0f0f0', fg='#333', font=("Arial", 30, "bold"))
title.pack(pady=(20, 10))

# Input entry field for adding tasks
txt_input = tkinter.Entry(root, width=50, font=("Arial", 12))
txt_input.pack(pady=10)

# Add Task button
btn_add_task = tkinter.Button(root, text="Add Task", fg='white', bg='#007bff', font=("Arial", 12, "bold"), command=add_task)
btn_add_task.pack(side='left', padx=10)

# Delete Task button
btn_delete = tkinter.Button(root, text="Delete Task", fg='white', bg='#dc3545', font=("Arial", 12, "bold"), command=delete_task)
btn_delete.pack(side='left', padx=10)

# Update Task button
btn_update = tkinter.Button(root, text="Update Task", fg='white', bg='#28a745', font=("Arial", 12, "bold"), command=update_task)
btn_update.pack(side='left', padx=10)

# Choose Random button
btn_choose_random = tkinter.Button(root, text="Choose Random", fg='white', bg='#17a2b8', font=("Arial", 12, "bold"), command=choose_random)
btn_choose_random.pack(side='left', padx=10)

# Number of Tasks button
btn_number_of_tasks = tkinter.Button(root, text="Number of Tasks", fg='white', bg='#ffc107', font=("Arial", 12, "bold"), command=number_of_tasks)
btn_number_of_tasks.pack(side='left', padx=10)

# Mark as Completed button
btn_mark_completed = tkinter.Button(root, text="Mark Completed", fg='white', bg='#28a745', font=("Arial", 12, "bold"), command=mark_completed)
btn_mark_completed.pack(side='left', padx=10)

# View Completed Tasks button
btn_view_completed = tkinter.Button(root, text="View Completed", fg='white', bg='#17a2b8', font=("Arial", 12, "bold"), command=view_completed)
btn_view_completed.pack(side='left', padx=10)

# View Pending Tasks button
btn_view_pending = tkinter.Button(root, text="View Pending", fg='white', bg='#ffc107', font=("Arial", 12, "bold"), command=view_pending)
btn_view_pending.pack(side='left', padx=10)

# Display label
display_label = tkinter.Label(root, text="", bg='#f0f0f0', fg='#333', font=("Arial", 14))
display_label.pack(pady=10)

# Listbox to display tasks
lb_tasks = tkinter.Listbox(root, width=100, height=15, font=("Arial", 12))
lb_tasks.pack(pady=10)

# Exit button
btn_exit = tkinter.Button(root, text="Exit", fg='white', bg='#6c757d', font=("Arial", 12, "bold"), command=exit_app)
btn_exit.pack(side='bottom', pady=20)

update_listbox()

root.mainloop()
