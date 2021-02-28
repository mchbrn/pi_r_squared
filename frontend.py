from datetime import datetime
from functools import partial
from tkinter import *
from tkinter import ttk
from sqlite3 import Error
import sqlite3
import pandas as pd
import PIL.ImageTk
import PIL.Image
import database
import news
import weather

def getTodo():
    """Get activities for today's date, if none are set then return message to user"""
    today_activities = "SELECT activity FROM todo WHERE date='" + datetime.today().strftime("%Y-%m-%d") + "';"
    today_IDs = "SELECT id FROM todo WHERE date='" + datetime.today().strftime("%Y-%m-%d") + "';"
    today_completed = "SELECT completed FROM todo WHERE date='" + datetime.today().strftime("%Y-%m-%d") + "';"

    activities = database.get(today_activities)
    IDs = database.get(today_IDs)
    completed = database.get(today_completed)

    number_of_todos = len(activities)

    for i in range(number_of_todos):
        ttk.Label(content, text=activities[i]).grid(column=0, row=i)

        if (completed[i] == (0,)):
            print("Draw uncompleted")
            control = 0
            Checkbutton(content, command=partial(updateCompleted, IDs[i]), image=unchecked, selectimage=checked, indicatoron=False, onvalue=1, offvalue=0).grid(column=1, row=i)
        else:
            print("Draw completed")
            control = 1
            Checkbutton(content, command=partial(updateCompleted, IDs[i]), image=checked, selectimage=unchecked, indicatoron=False, onvalue=1, offvalue=0).grid(column=1, row=i)
 
def updateCompleted(ID):
    conn = None
    db = r"db/sqlite.db"

    try:
        conn = sqlite3.connect(db)
    except Error as e:
        print(e)

    ID = str(ID)
    ID = ID[1:2]

    sql = "SELECT completed FROM todo WHERE id = '" + ID + "';"
    control = database.get(sql)

    control = str(control)
    control = control[2:3]

    if (control == "1"):
        sql = "UPDATE todo SET completed = 0 WHERE id = '" + ID + "';"
    elif (control == "0"):
        sql = "UPDATE todo SET completed = 1 WHERE id = '" + ID + "';"

    database.query(conn, sql)

root = Tk()
root.title("Pi R-Squared")

mainframe = ttk.Frame(root, height="720", width="720")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

content = ttk.Frame(mainframe, height="520", width="720")
content.grid(column=0, row=0, sticky=(N, W, E))

buttons = ttk.Frame(mainframe, height="200", width="720")
buttons.grid(column=0, row=1, sticky=(W, E, S))

ttk.Button(buttons, text="A", command=getTodo).grid(column=0, row=0, sticky=(N, W, S))
ttk.Button(buttons, text="B").grid(column=1, row=0, sticky=(N, S))
ttk.Button(buttons, text="C").grid(column=2, row=0, sticky=(N, S))
ttk.Button(buttons, text="D").grid(column=3, row=0, sticky=(N, E, S))
todolist = StringVar()
ttk.Label(mainframe, textvariable=todolist)

checked = PhotoImage(file="icons/checked.png")
unchecked = PhotoImage(file="icons/unchecked.png")

for child in buttons.winfo_children():
    child.grid_configure(padx=50, pady=20)

root.mainloop()
