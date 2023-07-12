""" This script creates the wordle loop within tkinter using the cleaned dictionaries"""

import pandas as pd
import random
import tkinter as tk
from tkinter import Label, Entry, Tk, ttk, mainloop, CENTER, StringVar, END


solution_dictionary = pd.read_csv("wordle_dictionary.csv")
checking_dictionary = pd.read_csv("checking_dictionary.csv")


solution = random.choice(solution_dictionary['word']) 
solution



def destr():
    """This function closes the running tkinter window and loop."""
    global win
    win.destroy()

def to_uppercase(*args):
    var.set(var.get().upper())

def compare_word():
    """ This function compares an entered word against the list of 
    allowed words (large dictionary) as well as against the solution. 
    It outputs the colour coded guess and other prompts if the guess 
    entered is invalid.

    Used packages: Tkinter

    Author: Silja Guggisberg, 11/07/2023"""

    var = entry.get()

    global count

    if len(var) != 5:
        lab = Label(win, text="Please enter a five letter word")
        lab.grid(row=12, column=6)
        
    elif var not in checking_dictionary.word.values:
        invalid_lab = Label(win, text="Invalid word, Guess again", font='Helvetica 16')
        invalid_lab.grid(row=12, column=6)
        
    else:
        count += 1
        col=2
        for letter, x in zip(var,solution):
            if letter == x:
                col+=1
                Label(win, text=letter, font='Helvetica 18', foreground='green').grid(row=count+1, column=col)
            
            elif letter in solution:
                col+=1
                Label(win, text=letter, font='Helvetica 18', foreground='yellow').grid(row=count+1, column=col)
            
            else:
                col+=1
                Label(win, text=letter, font='Helvetica 18').grid(row=count+1, column=col)
               
    if var == solution:
        Label(win, text='Well done!', font='Helvetica 22', foreground='green').grid(row=6, column=2)
    
    if count == 6:
        Label(win, text=f"Out of attempts, the word was {solution}", font='Helvetica 18', foreground='red').grid(row=10, column=0, sticky='W')
        button1.destroy()

    entry.delete(0,END)



win = Tk()

win.title('WORDLE GAME')

win.geometry("900x600")

var = StringVar(win)
entry = Entry(win, width= 42, textvariable=var)

try:
    # python 3.6
    var.trace_add('write', to_uppercase)
except AttributeError:
    # python < 3.6
    var.trace('w', to_uppercase)


label1 = Label(win, text='Guess a five-letter word', font=('Helvetica 16'))
label1.grid(row=0, column=0)

entry.grid(row=10, column=4)

count=0
button1 = ttk.Button(win, text= "Click to Submit", command= compare_word)
button1.grid(column=7,row=10)

while True:
    ttk.Button(win, text="Quit Game", command=destr).grid(row=7, column=0)
    win.mainloop()