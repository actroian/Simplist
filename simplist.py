from tkinter import *
import tkinter as tk
from datetime import time
from tkinter.ttk import *
from Task import Task
from tkinter.constants import CENTER, X
from tkinter.font import ITALIC
from tkinter.ttk import *
import math
from time import strftime
import sys
import functools

global routine
routine = []
global screen
screen = 0
print(screen)
#Variables needed for each task
seconds_remaining = 90
task_name = "Eat food"


def show_screen(screen):

    if screen==2:
        frame.grid_forget()
        frame2 = tk.Frame(window, bg="white")
        frame2.grid()

        def numPrint(btn): #replace print with index
            print(btn)

        files = []
        btn = []

        for i in routine:
            files.append(i)

        for i in range(len(files)):
            separator = Label(frame2, text="Task " + str(i+1), font=('Calibri', 16, 'bold'))
            separator.grid(row=(i+3*i), column=0)
            btn.append(Label(frame2, text=files[i]))
            btn[i].grid(row=(i+3*i+1), column=0) #this packs the buttons

        def click_add_task():
            frame2.grid_forget()
            show_screen(3)

        def start_routine():
            window.destroy()
            show_screen(4)

        start_btn = Button(frame2, text = "Start Routine", command =start_routine)
        start_btn.grid()
        add_task_btn = Button(frame2, text = "Add Task", command =click_add_task)
        add_task_btn.grid()

    elif screen==3:
        frame3 = tk.Frame(window, bg="white")
        frame3.grid()

        task_label = tk.Label(frame3, text="Enter your task:", font=("Calibri, 30"), )
        task_label.grid(row=0, column=1, padx=25, pady=20)
        name_label = tk.Label(frame3, text="Name:", font=("Calibri, 20"), justify=CENTER)
        name_label.grid(row=1, column=1, padx=25, pady=10)
        name_entry = tk.Entry(frame3, font=("Calibri, 14"), borderwidth=1, justify=CENTER)
        name_entry.grid(row=2, column=1, padx=25, ipady=5, pady=10)
        duration_label = tk.Label(frame3, text="Time duration (minutes):", font=("Calibri, 20"), justify=CENTER)
        duration_label.grid(row=3, column=1, padx=25, pady=10,)
        duration_entry = tk.Entry(frame3, font=("Calibri, 14"), borderwidth=1, justify=CENTER)
        duration_entry.grid(row=4, column=1, padx=25, ipady=5, pady=10)


        def click_submit():  # right now, this prints some stuff to the console to make sure the code works - you can delete the print statements
            print("Submitted")
            task1 = Task(name_entry.get(), int(duration_entry.get()))
            routine.append(task1)
            for task in routine:
                print(task)
            name_entry.delete(0, tk.END)
            duration_entry.delete(0, tk.END)
            frame3.grid_forget()
            show_screen(2)
            # code to make it return to the task list page

        submit_button = tk.Button(frame3, text="Submit", command=click_submit, justify=CENTER)
        submit_button.grid(row=5, column=1, ipadx=10, ipady=10, pady=10)

    elif screen==4:
        import Time


#Home Screen/Screen 1
if __name__=='__main__':
    window = tk.Tk()
    window.title('Routine App')
    window.geometry('295x520')

    frame = tk.Frame(window, bg="white")
    frame.grid()

    st = Style()
    st.theme_use('classic')
    st.configure('TButton', borderwidth=0, background='#79AC37', foreground='white', justify=CENTER, width=27, height=20)
    st.configure('TLabel', background='white', justify=CENTER)

    icon = Label(frame, text="️", style='TLabel', font=("Calibri", 60))
    icon.grid(row=0, column=1, pady=(25, 0))

    time = Label(frame, text="7:00am", style='TLabel', font=("Calibri", 44))
    time.grid(row=1, column=1, pady=(5, 0))

    welcome = Label(frame, text="Good morning Bob! \nLet's start your morning routine.", style='TLabel')
    welcome.grid(row=2, column=1, padx=10, pady=10)

    btn1 = Button(frame, text='Morning Routine\n7:00am - 8:00am', style='W.TButton', command= lambda: show_screen(2))
    btn1.grid(row=3, column=1, padx=10, pady=10)

    btn2 = Button(frame, text='Afternoon Routine\n3:00pm - 4:00pm', style='W.TButton', command=None)
    btn2.grid(row=4, column=1, padx=10, pady=10)

    btn3 = Button(frame, text='Evening Routine\n9:00pm - 10:00pm', style='W.TButton', command=None)
    btn3.grid(row=5, column=1, padx=10, pady=10)

    home = Label(frame, text = "home", background='white', font= ('Calibri 15 underline'))
    home.grid(row=6, column=1, pady=30)

window.mainloop()
