import tkinter as tk
import os


class Task:
    def __init__(self):
        self.title = tk.StringVar()
        self.open = tk.StringVar()
        self.aim = tk.StringVar()
        self.log_msg = tk.StringVar()
        self.to_do = tk.StringVar()
        self.time = tk.StringVar()

def select(button, task):
    if button['bg'] == main_colour:
        selected_tasks.append(task)
        button.configure(bg=mark_colour)
    else:
        selected_tasks.remove(task)
        button.configure(bg=main_colour)

def remove_task():
    #remove the task from list and update the GUI
    #when removing tasks twice:error ValueError: list.remove(x): x not in list
    for widget in main_body.winfo_children():
        widget.destroy()
    for task in selected_tasks:
        tasks.remove(task)
    for task in tasks:
        write_task(task)


def write_task(task):
    mark_btn = tk.Button(master=main_body, text="", padx=10, pady=5,
                            command=lambda: select(mark_btn, task), bg=main_colour, bd=-2, highlightthickness=0, activebackground=mark_colour, cursor="hand2")
    mark_btn.grid(row=len(tasks)-1, column=0, columnspan = 2, sticky = "nsew")

    task_label = tk.Label(master=main_body, text = task.title.get(), font=("calibre",10,"normal"), bg=main_colour, fg=white)
    task_label.grid(row=tasks.index(task), column=0)

    task_label = tk.Label(master=main_body, text = str(task.time.get()) + " minutes", font=("calibre",10,"normal"), bg=main_colour, fg=white)
    task_label.grid(row=tasks.index(task), column=1)


def add_task():
    task = Task()
    task_window = tk.Toplevel(window)
    task_window.grab_set()

    header = tk.Frame(master=task_window, width=500, height=40, bg=darker_accent_colour)
    header.pack(fill=tk.X)

    task_main_body = tk.Frame(master=task_window, width=500,height=500, bg=accent_colour)
    task_main_body.pack(fill=tk.BOTH, expand=True)
    task_main_body.columnconfigure([0, 1],weight=1, minsize=50)
    task_main_body.rowconfigure([0, 1, 3],weight=1, minsize=50)

    labels = ["Title", "Task", "Time", "Aim"]

    header_label = tk.Label(master=header, text = "Please fill in task details", font=("calibre",12,"normal"), bg=darker_accent_colour, fg=white)
    header_label.pack()

    for i, label in enumerate(labels):
        lbl = tk.Label(master=task_main_body, text = label, font=("calibre",10,"normal"), bg=accent_colour, fg=white)
        lbl.grid(row=i, column=0)


    title_ent = tk.Entry(master=task_main_body, textvariable = task.title, font=("calibre",10,"normal"), bg=main_colour, fg=white, bd=0, highlightthickness=0)
    title_ent.grid(row=0, column=1, sticky = "ew", padx=10, pady=10)

    task_ent = tk.Entry(master=task_main_body, textvariable = task.open, font=("calibre",10,"normal"), bg=main_colour, fg=white, bd=0, highlightthickness=0)
    task_ent.grid(row=1, column=1, sticky = "ew", padx=10, pady=10)

    time_ent = tk.Entry(master=task_main_body, textvariable = task.time, font=("calibre",10,"normal"), bg=main_colour, fg=white, bd=0, highlightthickness=0)
    time_ent.grid(row=2, column=1, sticky = "ew", padx=10, pady=10)

    aim_ent = tk.Entry(master=task_main_body, textvariable = task.aim, font=("calibre",10,"normal"), bg=main_colour, fg=white, bd=0, highlightthickness=0)
    aim_ent.grid(row=3, column=1, sticky = "ew", padx=10, pady=10)

    footer = tk.Frame(master=task_window, width=500, height=40, bg=accent_colour)
    footer.pack(fill=tk.X)


    def close():
        task_window.destroy()
        tasks.append(task)
        write_task(task)




    add_task_btn = tk.Button(master=footer, text="Add", font=("calibre",10,"bold"), padx=10, pady=5, fg=white,
                            command= close, bg=green, bd=-2, highlightthickness=0, cursor="hand2", activebackground=light_green, activeforeground=white)
    add_task_btn.pack()



accent_colour = "#2C2F33"
main_colour = "#36393E"
darker_accent_colour = "#222529"
green = "#4a9f04"
light_green = "#54A90E"
yellow = "#faba01"
white = "#fffdff"
red = "#d11a2a"
light_red = "#DB2434"
mark_colour = "#404348"
select_colour = "#5F6267"


tasks = []
selected_tasks = []

window = tk.Tk()


sidebar = tk.Frame(master=window, width = 150, height=700, bg=accent_colour)
sidebar.pack(fill=tk.Y, side=tk.LEFT)
sidebar.columnconfigure([0, 1, 3, 4, 5, 6],weight=1, minsize=50)
sidebar.rowconfigure([0, 1, 3, 4, 5, 6],weight=1, minsize=50)


header = tk.Frame(master=window, width=650, height=70, bg=accent_colour)
header.pack(fill=tk.X)
header.columnconfigure([0, 1, 3, 4, 5, 6], minsize=50)
header.rowconfigure(0, minsize=50)


main_body = tk.Frame(master=window, width=500, bg=main_colour)
main_body.pack(fill=tk.BOTH, expand=True, side=tk.LEFT)
main_body.columnconfigure([0,1],weight=1, minsize=50)
main_body.rowconfigure([0, 1, 3, 4, 5, 6, 7, 8, 9, 10],weight=1, minsize=50)


add_task_btn = tk.Button(master=header, text="Add task", font=("calibre",10,"bold"), padx=10, pady=5, fg=white,
                        command=add_task, bg=green, bd=-2, highlightthickness=0, cursor="hand2", activebackground=light_green, activeforeground=white)
add_task_btn.grid(row=0, column=0)

remove_task_btn = tk.Button(master=header, text="Remove task", font=("calibre",10,"bold"), padx=10, pady=5, fg=white,
                        command=remove_task, bg=red, bd=-2, highlightthickness=0, cursor="hand2", activebackground=light_red, activeforeground=white)
remove_task_btn.grid(row=0, column=1)

#make add standard task button in the sidebar that makes it so you can add that task with one click

window.mainloop()
