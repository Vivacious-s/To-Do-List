import tkinter as tk 
from tkinter import messagebox
import json

TASKS_FILE="tasks.json"

def load_tasks():
    try:
        with open(TASKS_FILE,"r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    
def save_tasks(tasks):
    with open(TASKS_FILE,"w") as file:
        json.dump(tasks,file,indent=4)

def add_task():
    task = entry.get()
    if task:
        tasks.append(task)
        save_tasks(tasks)
        listbox.insert(tk.END,task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning","Task cannot be empty!")

def remove_task():
    try:
        selected_index=listbox.curselection()[0]
        task=tasks.pop(selected_index)
        save_tasks(tasks)
        listbox.delete(selected_index)
    except IndexError:
        messagebox.showwarning("Warning","Please select a task to remove!")

root=tk.Tk()
root.title("TO-DO-LIST")
root.geometry("400x400")
 
tasks=load_tasks()

entry=tk.Entry(root,width=40)
entry.pack(pady=5)

add_button=tk.Button(root, text="ADD TASK",command=add_task)
add_button.pack()

listbox=tk.Listbox(root,width=50,height=15)
listbox.pack(pady=5)

remove_button=tk.Button(root, text="REMOVE TASK",command=remove_task)
remove_button.pack()

for task in tasks:
    listbox.insert(tk.END,task)

root.mainloop()
