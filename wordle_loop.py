""" This script creates the wordle loop within tkinter"""

import random
import tkinter as tk
from tkinter import Label, Entry, Tk, ttk, mainloop, CENTER, StringVar


word_list = ['mango','spoon','ramen','plate']

large_dictionary = ['mango','spoon','ramen','plate', 'table', 'plato']
large_dictionary = [x.upper() for x in large_dictionary]
large_dictionary


solution = random.choice(word_list) 
solution

win = Tk()

win.title('WORDLE GAME')

win.geometry("900x600")


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
    sol='PLATE'
    global count

    if len(var) != 5:
        lab = Label(win, text="Please enter a five letter word")
        lab.grid(row=1, column=2)
        #lab.after(1500,lab.destroy())
        
    elif var not in large_dictionary:
        invalid_lab = Label(win, text="Invalid word, Guess again", font='Helvetica 16')
        invalid_lab.grid(row=10, column=0)
        #invalid_lab.after(1500,invalid_lab.destroy())

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
        Label(win, text=f"Out of attempts, the word was {sol}", font='Helvetica 18', foreground='red').grid(row=10, column=0, sticky='W')
        button1.destroy()


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

entry.grid(row=10, column=9)

count=0
button1 = ttk.Button(win, text= "Click to Submit", command= compare_word)
button1.grid(column=10,row=10)

while True:
    ttk.Button(win, text="Quit Game", command=destr).grid(row=7, column=0)
    win.mainloop() 


# stop loop when max attempts reached - done removed button

# move out of attempts warning and other messages
# make more efficient
# make invalid word, guess again message disappear if button is clicked
