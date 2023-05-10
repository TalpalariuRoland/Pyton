import turtle
import time
import random
from tkinter import *
import sched
from CokieClass import *


class Index:
    screen=turtle.Screen()
    screen.setup(width=1.0, height=1.0)
    Cookie = CokieClass()
    Cookie.start()

    canvas = screen.getcanvas()
    button = Button(canvas.master, text="Bonus on click", command=Cookie.ClickPowerUpp)
    button.pack()
    pasive = Button(canvas.master, text="Bonus pasive", command=Cookie.addPasive)
    pasive.pack()
    button.place(x= screen.window_width()-100, y=screen.window_height()/10) 
    pasive.place(x= screen.window_width()-100, y=screen.window_height()/7) 

    save = Button(canvas.master, text="Save", command=Cookie.saveData,bg="green", fg="white")
    save.pack()
    save.place(x= screen.window_width()/2, y=screen.window_height()-100) 

    load = Button(canvas.master, text="Load last Save", command=Cookie.loadData,bg="green", fg="white")
    load.pack()
    load.place(x= screen.window_width()/2 +100, y=screen.window_height()-100) 


    Cookie.Cookie.onclick(Cookie.clicked)
    Cookie.update_score()
    turtle.mainloop()
    


