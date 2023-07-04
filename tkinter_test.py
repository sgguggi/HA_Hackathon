"""This script tests the tkinter package to create  user prompts and interactive windows"""

import tkinter as tk
from tkinter import Label, Entry, Tk, mainloop, CENTER

# Testing using code from the internet
master = Tk()
Label(master, text='First Name').grid(row=0)
Label(master, text='Last Name').grid(row=1)
e1 = Entry(master)
e2 = Entry(master)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
mainloop()

# Creating an example of a conditional print
win = Tk()
win.title('WORDLE GAME')

win.geometry("900x600")

def get_data():
    var = entry.get()
    if 'i' in var:
        Label(win,text=var).pack()
    else:
        Label(win, text='Guess again').pack()
        
label1 = Label(win, text='Guess a five-letter word')
label1.pack()
entry = Entry(win, width= 42)
entry.place(relx= .5, rely= .5, anchor= CENTER)

label= Label(win, text="", font=('Helvetica 14'))
label.pack()

ttk.Button(win, text= "Click to Submit", command= get_data).place(relx= .7, rely= .5, anchor= CENTER)

win.mainloop()
