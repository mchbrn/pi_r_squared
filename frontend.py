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
    """Destroy all widgets bar buttons"""
    for child in mainframe.winfo_children():
        if (type(child) != ttk.Button):
            child.destroy()

def padButtons(padding_value):
    for child in mainframe.winfo_children():
        if (type(child) == ttk.Button):
            child.grid_configure(padx=30, pady=(padding_value,30))


def getTodo():
    destroyChildren()

    ttk.Label(mainframe, font="helvetica 40", justify="center", text="To Do List").grid(column=1, columnspan=2, row=0)

    today_activities = "SELECT activity FROM todo WHERE date='" + datetime.today().strftime("%Y-%m-%d") + "';"
    today_IDs = "SELECT id FROM todo WHERE date='" + datetime.today().strftime("%Y-%m-%d") + "';"
    today_completed = "SELECT completed FROM todo WHERE date='" + datetime.today().strftime("%Y-%m-%d") + "';"

    activities = database.get(today_activities)
    IDs = database.get(today_IDs)
    completed = database.get(today_completed)

    number_of_todos = len(activities)

    my_activities = []
    padding_values = [380, 320, 260, 200, 140, 80, 20]

    for activity in activities:
        my_activity = str(activity)
        my_activity = my_activity[2:]
        my_activity = my_activity[:-3]
        my_activities.append(my_activity)

    for i in range(number_of_todos):
        ttk.Label(mainframe, font="helvetiva 18", padding=(25,0,0,0), text=my_activities[i]).grid(column=0, columnspan=2, row=i+1, sticky=(W,))

        if (completed[i] == (0,)):
            # Add padding below final todo item
            if (i+1 == number_of_todos):
                control = 0
                Checkbutton(mainframe, command=partial(updateCompleted, IDs[i]), image=img_unchecked, selectimage=img_checked, indicatoron=False, onvalue=1, offvalue=0).grid(column=3, row=i+1, sticky=(E,))
                padButtons(200)
            else:
                control = 0
                Checkbutton(mainframe, command=partial(updateCompleted, IDs[i]), image=img_unchecked, selectimage=img_checked, indicatoron=False, onvalue=1, offvalue=0).grid(column=3, row=i+1, sticky=(E,))
        else:
            if (i+1 == number_of_todos):
                control = 1
                Checkbutton(mainframe, command=partial(updateCompleted, IDs[i]), image=img_checked, selectimage=img_unchecked, indicatoron=False, onvalue=1, offvalue=0).grid(column=3, row=i+1, sticky=(E,))
                padButtons(padding_values[i+1])
            else:
                control = 1
                Checkbutton(mainframe, command=partial(updateCompleted, IDs[i]), image=img_checked, selectimage=img_unchecked, indicatoron=False, onvalue=1, offvalue=0).grid(column=3, row=i+1, sticky=(E,))
 
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

    ttk.Label(mainframe, font="helvetiva 40", justify="center", padding=(0,20,0,20), text="News").grid(column=1, columnspan=2, row=0)

    todays_news = news.get()

    for index_item, item in enumerate(todays_news):
        item_formatted = ""
        words = item.split()
        character_counter = 0

        for index_word, word in enumerate(words):
            word_formatted = ""
            character_counter += len(word)

            if (character_counter >= 30):
                if (index_word + 1 != len(words)):
                    word_formatted = word + "\n" + " "
                    character_counter = 0
                else:
                    word_formatted = word + " "
            else:
                word_formatted = word + " "

            item_formatted += word_formatted

        ttk.Label(mainframe, font="helvetiva 18", justify="left", padding=(25,0,0,10), text="• " + item_formatted).grid(column=0, columnspan=4, row=index_item+1, sticky=(W,))

        padButtons(35)

def getWeather():
    destroyChildren()
    
    ttk.Label(mainframe, font="helvetica 40", justify="center", padding=(0,0,0,140), text="Liverpool").grid(column=1, columnspan=2, row=0)

    ttk.Label(mainframe, image=img_todays_weather, padding=(0,0,0,140)).grid(column=3, row=0)

    todays_weather = weather.get()

    for index, data in enumerate(todays_weather):
        ttk.Label(mainframe, font="helvetica 18", justify="center", text=data).grid(column=1, row=index+1, columnspan=2)

    padButtons(140)

def getGoodreads():
    destroyChildren()

    ttk.Label(mainframe, font="helvetica 40", justify="center", text="Goodreads").grid(column=0, columnspan=4, row=0)

    data = goodreads.get()

    ttk.Label(mainframe, font="helvetica 18", justify="center", padding=(0,0,0,20), text=data[0][0:-1]).grid(column=0, columnspan=4, row=1)
    ttk.Label(mainframe, font="helvetiva 26" , justify="center", text="Recently read").grid(column=0, columnspan=4, row=2)
    
    for i in range(1, 6):
        ttk.Label(mainframe, font="helvetica 18", justify="left", padding=(25,0,0,0), text="• " + data[i]).grid(column=0, columnspan=4, row=i+2, sticky=(W,))

    padButtons(164)

root = Tk()
# Make interface fullscreen
root.attributes('-zoomed',True)
root.title("Pi R-Squared")

mainframe = ttk.Frame(root, height="720", width="720")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

#content = ttk.Frame(mainframe, height=520, padding=(50,25,50,25), width=720)
#content.grid(column=0, row=0, sticky=(N, W, E))

#buttons = ttk.Frame(mainframe, padding=(0,0,0,5), height=500, width=720)
#buttons.grid(column=0, row=1, sticky=(W, E, S))

img_todo = PhotoImage(file="icons/todo_90.png")
img_news = PhotoImage(file="icons/news_90.png")
img_weather = PhotoImage(file="icons/weather_90.png")
img_goodreads = PhotoImage(file="icons/goodreads_90.png")
img_checked = PhotoImage(file="icons/checked.png")
img_unchecked = PhotoImage(file="icons/unchecked.png")
img_todays_weather = PhotoImage(file="icons/todays_weather.png")
logo = PhotoImage(file="icons/goodreads_logo.png")

button_todo = ttk.Button(mainframe, command=getTodo, image=img_todo).grid(column=0, row=9, sticky=(N, W, S))
button_news = ttk.Button(mainframe, command=getNews, image=img_news).grid(column=1, row=9, sticky=(N, S))
button_weather = ttk.Button(mainframe, command=getWeather, image=img_weather).grid(column=2, row=9, sticky=(N, S))
button_goodreads = ttk.Button(mainframe, command=getGoodreads, image=img_goodreads).grid(column=3, row=9, sticky=(N, S))

for child in mainframe.winfo_children():
    child.grid_configure(padx=30, pady=30)

getTodo()

root.mainloop()
