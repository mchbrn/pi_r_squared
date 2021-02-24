from datetime import datetime
from tkinter import *
from tkinter import ttk
import PIL.ImageTk
import PIL.Image
import database
import news
import weather

def getTodo():
    today = "SELECT activity FROM todo Where date='" + datetime.today().strftime("%Y-%m-%d") + "';"
    todo = database.get(today)
    todolist.set(todayslist)

root = Tk()
root.title("Pi R-Squared")

mainframe = ttk.Frame(root, padding="303 310")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

ttk.Button(mainframe, text="Hello World", command=getTodo).grid(column=1, row=1, sticky=(N, S))
todolist = StringVar()
ttk.Label(mainframe, textvariable=todolist)

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

root.mainloop()
