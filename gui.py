import database
from datetime import datetime
from PIL import ImageTK, Image
from tkinter import *

def todolist():
    today = "SELECT * FROM todo WHERE date='" +datetime.today().strftime("%Y-%m-%d") + "';"
    todayslist = database.get(today)
    list = Label(root, text=todayslist)
    list.pack()

root = Tk()
root.title("Pi R-Squared")

#title = Label(root, text="Pi R-Squared")
#title.pack()
todo = Button(root, text="todo", padx=72, pady=72, command=todolist)
news = Button(root, text="news", padx=72, pady=72)
goodreads = Button(root, text="book", padx=72, pady=72)
weather = Button(root, text="weather", padx=72, pady=72)

todo.pack()
news.pack()
goodreads.pack()
weather.pack()

root.mainloop()


