from datetime import datetime
from functools import partial
from tkinter import *
from tkinter import ttk
from sqlite3 import Error
import sqlite3
import PIL.ImageTk
import PIL.Image
import database
import news
import weather
import goodreads

def destroyChildren():
    for child in content.winfo_children():
        child.destroy()

def getTodo():
    destroyChildren()

    ttk.Label(content, text="To Do List").grid(column=0, row=0)

    today_activities = "SELECT activity FROM todo WHERE date='" + datetime.today().strftime("%Y-%m-%d") + "';"
    today_IDs = "SELECT id FROM todo WHERE date='" + datetime.today().strftime("%Y-%m-%d") + "';"
    today_completed = "SELECT completed FROM todo WHERE date='" + datetime.today().strftime("%Y-%m-%d") + "';"

    activities = database.get(today_activities)
    IDs = database.get(today_IDs)
    completed = database.get(today_completed)

    number_of_todos = len(activities)

    my_activities = []

    for activity in activities:
        my_activity = str(activity)
        my_activity = my_activity[2:]
        my_activity = my_activity[:-3]
        my_activities.append(my_activity)

    for i in range(number_of_todos):
        ttk.Label(content, text=my_activities[i]).grid(column=0, row=i+1)

        if (completed[i] == (0,)):
            control = 0
            Checkbutton(content, command=partial(updateCompleted, IDs[i]), image=img_unchecked, selectimage=img_checked, indicatoron=False, onvalue=1, offvalue=0).grid(column=1, row=i+1)
        else:
            control = 1
            Checkbutton(content, command=partial(updateCompleted, IDs[i]), image=img_checked, selectimage=img_unchecked, indicatoron=False, onvalue=1, offvalue=0).grid(column=1, row=i+1)
 
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

def getNews():
    destroyChildren()

    ttk.Label(content, text="News").grid(column=0, row=0)

    todays_news = news.get()

    for index, item in enumerate(todays_news):
        ttk.Label(content, text=item).grid(column=0, row=index+1, sticky=(W,))

def getWeather():
    destroyChildren()
    
    ttk.Label(content, text="Liverpool").grid(column=0, row=0, rowspan=1)

    todays_weather = weather.get()

    for index, data in enumerate(todays_weather):
        ttk.Label(content, text=data).grid(column=0, row=index+1, sticky=(W,))

    ttk.Label(content, image=img_todays_weather).grid(column=1, row=1, columnspan=3)

def getGoodreads():
    destroyChildren()

    data = goodreads.get()

    ttk.Label(content, text=data[0]).grid(column=0, row=1)
    ttk.Label(content, text="Recently read").grid(column=0, row=2)
    
    for i in range(1, 6):
        ttk.Label(content, text=data[i]).grid(column=0, row=i+2, sticky=(W,))

root = Tk()
root.title("Pi R-Squared")

mainframe = ttk.Frame(root, height="720", width="720")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

content = ttk.Frame(mainframe, height=520, padding=(50,25,50,25), width=720)
content.grid(column=0, row=0, sticky=(N, W, E))

buttons = ttk.Frame(mainframe, height=200, width=720)
buttons.grid(column=0, row=1, sticky=(W, E, S))

img_todo = PhotoImage(file="icons/todo_90.png")
img_news = PhotoImage(file="icons/news_90.png")
img_weather = PhotoImage(file="icons/weather_90.png")
img_goodreads = PhotoImage(file="icons/goodreads_90.png")
img_checked = PhotoImage(file="icons/checked.png")
img_unchecked = PhotoImage(file="icons/unchecked.png")
img_todays_weather = PhotoImage(file="icons/todays_weather.png")
logo = PhotoImage(file="icons/goodreads_logo.png")

button_todo = ttk.Button(buttons, command=getTodo, image=img_todo ).grid(column=0, row=0, sticky=(N, W, S))
ttk.Button(buttons, width=25, command=getNews, image=img_news).grid(column=1, row=0, sticky=(N, S))
ttk.Button(buttons, command=getWeather, image=img_weather).grid(column=2, row=0, sticky=(N, S))
ttk.Button(buttons, command=getGoodreads, image=img_goodreads).grid(column=3, row=0, sticky=(N, E, S))

for child in buttons.winfo_children():
    child.grid_configure(padx=39, pady=39)

getTodo()

root.mainloop()
