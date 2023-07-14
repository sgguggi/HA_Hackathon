""" This script runs a wordle game using the tkinter package.
Step 1: Import necessary packages
Step 2: Read in dictionaries
Step 3: Define functions required for game
Step 4: Run game"""

# Step 1
import pandas as pd
import random
import tkinter as tk
from tkinter import Label, Entry, Tk, ttk, CENTER, StringVar, END

# Step 2
solution_dictionary = pd.read_csv("wordle_dictionary.csv")
checking_dictionary = pd.read_csv("checking_dictionary.csv")

# Step 3
def to_uppercase(*args):
    var.set(var.get().upper())

def compare_word():
    """This function compares an entered word against the list of 
    allowed words (large dictionary) as well as against the solution. 
    It outputs the colour coded guess and other prompts if the guess 
    entered is invalid.

    Used packages: Tkinter

    Author: Silja Guggisberg, 11/07/2023"""

    var = entry.get()

    global count

    if len(var) != 5:
        lab = Label(win, text="Please enter a five letter word", font="Helvetica 14")
        lab.grid(row=10, column=0)
        
    elif var not in checking_dictionary.word.values:
        invalid_lab = Label(win, text="   Invalid word, Guess again   ", font='Helvetica 14')
        invalid_lab.grid(row=10, column=0)
        
    else:
        count += 1
        col=3
        empty_lab = Label(win, text="                                  ", font="Helvetica 20")
        empty_lab.grid(row=10, column=0)

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
        Label(win, text='        Well done!        ', font='Helvetica 22', foreground='green').grid(row=10, column=0)
    
    if (var != solution) and (count == 6):
        Label(win, text=f"Out of attempts, the word was {solution}", font='Helvetica 14', foreground='red').grid(row=10, column=0, sticky='W')
        button1.destroy()

    entry.delete(0,END)

# Step 4
# Rerun from here to replay game after initial run
solution = random.choice(solution_dictionary['word']) 

win = Tk()

win.title('WORDLE GAME')

win.geometry("900x600")

var = StringVar(win)
entry = Entry(win, width= 42, textvariable=var)
entry.grid(row=10, column=1)

var.trace_add('write', to_uppercase)

label1 = Label(win, text='Guess a five-letter word', font='Helvetica 16')
label1.grid(row=0, column=0)

count=0
button1 = ttk.Button(win, text= "Click to Submit", command= compare_word)
button1.grid(column=2,row=10)

win.mainloop()