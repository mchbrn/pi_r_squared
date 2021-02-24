from datetime import datetime
import PIL.ImageTk
import PIL.Image
from tkinter import *
import database
import news
import weather

def getTodo():
    today = "SELECT activity FROM todo WHERE date='" + datetime.today().strftime("%Y-%m-%d") + "';"
    todayslist = database.get(today)
    return todayslist

def getNews():
    headlines = news.getNews()

def getGoodreads():
    print("Show Goodreads")  

def getWeather():
    print("Show weather")

def destroyWidgets(frame):
    for widget in frame.winfo_children():
        widget.destroy()

def showTodo():
    destroyWidgets(frame_display)

    frame_display_todo = LabelFrame(frame_display, bd=0, height=512, width=696)
    frame_display_todo.pack()
    
    todayslist = getTodo()

    checked = PhotoImage(file="icons/checked.png")
    unchecked = PhotoImage(file="icons/unchecked.png")
#    checked_img = PIL.ImageTk.PhotoImage(PIL.Image.open("icons/checked.png"))
#    unchecked_img = PIL.ImageTk.PhotoImage(PIL.Image.open("icons/unchecked.png"))
    
    for activity in range(0, len(todayslist)):
        item = todayslist[activity]
        item = str(item)
        item = item[2:-3]
        # add command to checkbutton
        check = Checkbutton(frame_display_todo, image=unchecked, selectimage=checked,  text=item)
        check.pack()

    print(todayslist)

def showNews():
    destroyWidgets(frame_display)
    print("News")

def showGoodreads():
    destroyWidgets(frame_display)
    print("Books")

def showWeather():
    destroyWidgets(frame_display)
    print("Weather")

root = Tk()
root.title("Pi R-Squared")

frame_display = LabelFrame(root, bd=0, height=512, width=696)
frame_display.pack()

showTodo()

#var = StringVar()
#todolist = Message(frame_display, textvariable=var)
#var.set(todayslist)
#todolist.pack()

#todolist = Text(frame_display)
#todolist.insert(INSERT, todayslist)
#todolist.pack()

frame_buttons = LabelFrame(root, bd=0, padx=0, pady=0)
frame_buttons.pack()

frame_todo = LabelFrame(frame_buttons, bd =0, padx=12, pady=5)
frame_news = LabelFrame(frame_buttons, bd =0, padx=12, pady=5)
frame_goodreads = LabelFrame(frame_buttons, bd =0, padx=12, pady=5)
frame_weather = LabelFrame(frame_buttons, bd =0, padx=12, pady=5)

frame_todo.grid(row=1, column=0)
frame_news.grid(row=1, column=1)
frame_goodreads.grid(row=1, column=2)
frame_weather.grid(row=1, column=3)

todo_img = PIL.ImageTk.PhotoImage(PIL.Image.open("icons/todo.png"))
todo = Button(frame_todo, height=144, width=144, command=showTodo, image=todo_img)
news_img = PIL.ImageTk.PhotoImage(PIL.Image.open("icons/news.png"))
news = Button(frame_news, height=144, width=144, command=showNews, image=news_img)
goodreads_img = PIL.ImageTk.PhotoImage(PIL.Image.open("icons/goodreads.png"))
goodreads = Button(frame_goodreads, height=144, width=144, image=goodreads_img)
weather_img = PIL.ImageTk.PhotoImage(PIL.Image.open("icons/weather.png"))
weather = Button(frame_weather, height=144, width=144, command=showWeather, image=weather_img)

todo.pack()
news.pack()
goodreads.pack()
weather.pack()

root.mainloop()
