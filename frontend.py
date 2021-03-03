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

    ttk.Label(content, font="helvetica 40", text="To Do List").grid(column=0, row=0)

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
        ttk.Label(content, font="helvetiva 18", text=my_activities[i]).grid(column=0, row=i+1, sticky=(W,))

        if (completed[i] == (0,)):
            control = 0
            Checkbutton(content, command=partial(updateCompleted, IDs[i]), image=img_unchecked, selectimage=img_checked, indicatoron=False, onvalue=1, offvalue=0).grid(column=1, row=i+1, sticky=(E,))
        else:
            control = 1
            Checkbutton(content, command=partial(updateCompleted, IDs[i]), image=img_checked, selectimage=img_unchecked, indicatoron=False, onvalue=1, offvalue=0).grid(column=1, row=i+1, sticky=(E,))
 
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

    ttk.Label(content, font="helvetiva 40", padding=(0,0,0,20), text="News").grid(column=0, row=0, sticky=(W,))

    todays_news = news.get()

    for index_item, item in enumerate(todays_news):
        item_formatted = ""
        words = item.split()
        character_counter = 0

        for index_word, word in enumerate(words):
            word_formatted = ""
            character_counter += len(word)
            print("Index is " + str(index_word))
            print("Number of words " + str(len(words)))

            if (character_counter >= 30):
                if (index_word + 1 != len(words)):
                    word_formatted = word + "\n" + " "
                    character_counter = 0
                else:
                    word_formatted = word + " "
            else:
                word_formatted = word + " "

            item_formatted += word_formatted

        ttk.Label(content, font="helvetiva 18", padding=(0,0,0,10), text="• " + item_formatted).grid(column=0, row=index_item+1, sticky=(W,))

def getWeather():
    destroyChildren()
    
    ttk.Label(content, font="helvetica 40", text="Liverpool").grid(column=0, row=0)

    todays_weather = weather.get()

    for index, data in enumerate(todays_weather):
        ttk.Label(content, font="helvetica 18", text=data).grid(column=0, row=index+1, sticky=(W,))

    ttk.Label(content, image=img_todays_weather).grid(column=1, row=1, columnspan=3)

def getGoodreads():
    destroyChildren()

    ttk.Label(content, font="helvetica 40", text="Goodreads").grid(column=0, row=0)

    data = goodreads.get()

    ttk.Label(content, font="helvetica 18", padding=(0,0,0,20), text=data[0]).grid(column=0, row=1)
    ttk.Label(content, font="helvetiva 26" ,text="Recently read").grid(column=0, row=2)
    
    for i in range(1, 6):
        if (i < 6):
            ttk.Label(content, font="helvetica 18", text="• " + data[i]).grid(column=0, row=i+2, sticky=(W,))
        else:
            ttk.Label(content, font="helvetica 18", padding=(0,0,0,300), text="• " + data[i]).grid(column=0, row=i+2, sticky=(W,))



root = Tk()
root.title("Pi R-Squared")

mainframe = ttk.Frame(root, height="720", width="720")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

content = ttk.Frame(mainframe, height=520, padding=(50,25,50,25), width=720)
content.grid(column=0, row=0, sticky=(N, W, E))

buttons = ttk.Frame(mainframe, padding=(0,0,0,5), height=200, width=720)
buttons.grid(column=0, row=1, sticky=(W, E, S))

img_todo = PhotoImage(file="icons/todo_90.png")
img_news = PhotoImage(file="icons/news_90.png")
img_weather = PhotoImage(file="icons/weather_90.png")
img_goodreads = PhotoImage(file="icons/goodreads_90.png")
img_checked = PhotoImage(file="icons/checked.png")
img_unchecked = PhotoImage(file="icons/unchecked.png")
img_todays_weather = PhotoImage(file="icons/todays_weather.png")
logo = PhotoImage(file="icons/goodreads_logo.png")

ttk.Button(buttons, command=getTodo, image=img_todo ).grid(column=0, row=0, sticky=(N, W, S))
ttk.Button(buttons, command=getNews, image=img_news).grid(column=1, row=0, sticky=(N, S))
ttk.Button(buttons, command=getWeather, image=img_weather).grid(column=2, row=0, sticky=(N, S))
ttk.Button(buttons, command=getGoodreads, image=img_goodreads).grid(column=3, row=0, sticky=(N, E, S))

for child in buttons.winfo_children():
    child.grid_configure(padx=39, pady=19)

getTodo()

root.mainloop()
