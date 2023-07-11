""" This script creates the wordle loop within tkinter"""

import pandas as pd
import random
import tkinter as tk
from tkinter import Label, Entry, Tk, ttk, mainloop, CENTER, StringVar


word_list = ['mango','spoon','ramen','plate']

large_dictionary = ['mango','spoon','ramen','plate', 'table', 'plato']

solution = random.choice(word_list) 
solution

win = Tk()

win.title('WORDLE GAME')

win.geometry("900x600")

count=0

def compare_word():
    """ This function compares an entered word against the list of 
    allowed words (large dictionary) as well as against the solution. 
    It outputs the colour coded guess and other prompts if the guess 
    entered is invalid.

    Used packages: Tkinter

    Author: Silja Guggisberg, 11/07/2023"""

    var = entry.get()
    sol='plate'
    global count

    if len(var) != 5:
        lab = Label(win, text="Please enter a five letter word")
        lab.grid(row=1, column=2)
        
    elif var not in large_dictionary:
        Label(win, text="Invalid word, Guess again", font='Helvetica 16').grid(row=10, column=0)

    else:
        count = count + 1
        col=3
        for letter, x in zip(var,sol):
            if letter == x:
                col+=1
                Label(win, text=letter, font='Helvetica 18', foreground='green').grid(row=count+1, column=col, sticky='E')
            
            elif letter in sol:
                col+=1
                Label(win, text=letter, font='Helvetica 18', foreground='yellow').grid(row=count+1, column=col, sticky='E')
            
            else:
                col+=1
                Label(win, text=letter, font='Helvetica 18').grid(row=count+1, column=col, sticky='E')
               
    if var == sol:
        Label(win, text='Well done!', font='Helvetica 22', foreground='green').grid(row=5, column=2, sticky='E')
    
    if count == 6:
        Label(win, text="Out of attempts", font='Helvetica 18').grid(row=10, column=0, sticky='W')


label1 = Label(win, text='Guess a five-letter word', font=('Helvetica 16'))
label1.grid(row=0, column=0)
entry = Entry(win, width= 42)
entry.grid(row=10, column=9)

ttk.Button(win, text= "Click to Submit", command= compare_word).grid(column=10,row=10)

def destr():
    """This function closes the running tkinter window and loop."""
    global win
    win.destroy()

while True:
    ttk.Button(win, text="Quit Game", command=destr).grid(row=7, column=0)
    win.mainloop() 

win.mainloop()


