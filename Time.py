import tkinter as tk
from tkinter import *
from tkinter.constants import CENTER, X
from tkinter.font import ITALIC
from tkinter.ttk import *
import math
from time import strftime
import sys
import functools

#Variables needed for each task
#45, 1, 5
seconds_remaining = [2700,60, 300]
task_name = ["Walk Dog", "Drink Water", "Groom Myself"]
complete = [False, False, False]

reset = False

#window
root = tk.Tk()
root.title("Timer")
canvas = tk.Canvas(root, height =400, width = 400, bg = "white")

#clock circle
canvas.create_oval(50,65, 350,365)
index = 0

#init section
radians = math.pi / 2 * 3
speed = math.pi * 2 / seconds_remaining[index]
canvas.pack()

#clock at the bottom
lbl = Label(root, font = ('Times', 20, 'bold', ITALIC),
            background = 'white',
            foreground = 'black'
            )

#determines timer display
def findTime():
    global seconds_remaining
    minutes_remaining = int(seconds_remaining[index]/60)
    seconds = seconds_remaining[index] - minutes_remaining * 60
    return "{:02d}".format(minutes_remaining) + ": " + "{:02d}".format(seconds)

#determines position of dot, time remaining and creates timer display
def time(radians):
    global seconds_remaining
    global task_name
    global index
    global reset
    global speed
    radians = radians + speed
    x = math.cos(radians) * 150 + 200
    y = math.sin(radians) * 150 + 215
    string = strftime('%H:%M:%S %p')
    lbl.config(text = string)
    lbl.after(1000, time, radians)
    seconds_remaining[index] = seconds_remaining[index] - 1
    if(seconds_remaining[index] <= 0 or complete[index]):
        complete[index] = True
        canvas.delete("all")
        canvas.create_text(200,215,fill= "black",font="Times 20 italic bold",
                        text="Done!")
        canvas.create_text(200,20,fill= "black",font="Times 20 italic bold",
                        text=task_name[index])
        return
    canvas.delete("all")
    canvas.create_text(200,215,fill= "black",font="Times 20 italic bold",
                        text=findTime())
    canvas.create_text(200,20,fill= "black",font="Times 20 italic bold",
                        text=task_name[index])
    canvas.create_oval(50,65, 350,365)

    if(reset):
        x = 200
        y= 65
        radians = 0
        speed = math.pi * 2 / seconds_remaining[index]
        reset = False
    canvas.create_oval(x,y,x,y, width= 5)

lbl.pack()
time(radians)

#stops dot and sets time to zero
#manuel reset of seconds_remaining will be needed for another task
def done():
    global speed
    global seconds_remaining
    seconds_remaining[index] = 0
    speed = 0

def next():
    global index
    global radians
    global speed
    global reset
    if(len(task_name) - 1 > index):
        index = index + 1
        canvas.delete("all")
        radians = math.pi / 2 * 3
        speed = math.pi * 2 / seconds_remaining[index]
        reset = True

def previous():
    global index
    global radians
    global speed
    global reset
    if(1 <= index):
        index = index - 1
        canvas.delete("all")
        radians = math.pi / 2 * 3
        speed = math.pi * 2 / seconds_remaining[index]
        reset = True


#removable button if you want to
previous = tk.Button(root, text = "Previous", padx=10, pady=5, fg ="black", bg="white", command = previous)
previous.pack()


done = tk.Button(root, text = "Done!", padx=10, pady=5, fg ="black", bg="white", command= done)
done.pack()

#removable button if you want to
next = tk.Button(root, text = "Next", padx=10, pady=5, fg ="black", bg="white", command= next)
next.pack()


root.mainloop()
