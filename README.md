# HA_Hackathon
June to July 2023

This project was created by the ONS Housing Analysis Team while taking part in the Coffee and Coding Hackathon 2023.
It contains the code to create a WORDLE game.

To play the WORDLE game run Wordle_script.py.
The game requires two dictionaries - wordle_dictionary.csv and checking_dictionary.csv.
The wordle_dictionary.csv is used to pick a word which needs to be solved, the checking_dictionary.csv is used to check input guesses against a valid five-letter word list.

How to play:
Run script Wordle_script.py

Game rules:
Guess a five-letter word. A jumble of letters is not allowed!
The game will show you if your letters are in the right place (green) or if they are within the solution, but not at the right place (yellow).
You have six guesses in total! Once you're out of guesses the correct solution will be shown.

Files within this repository:
Check_colour_packages_first_loop.py : Script used to test colouring console outputs
Create_dictionary_v2.py : Script used to create the five-letter word dictionary used to pick a random word to be guessed, wordle_dictionary.csv
Create_large_dictionary_py : Script used to create the five-letter word dictionary used to validate input guesses, checking_dictionary.csv
tkinter_test.py : Script used to test if the tkinter package can be used for the game
wordle_loop.py : Script used to create a basic wordle game using tkinter package
Wordle_script.py : Final script to play the game!

Authors:
Hacking Housing Analysis:
Nick Richardson
Nikki Bowers
Sarah Bruce
Craig Smith
Silja Guggisberg