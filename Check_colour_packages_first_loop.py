
# coding: utf-8

""" This script tests different packages for printing console outputs in colour.
Colorama package works as expected.

Author: Silja Guggisberg
Date: 02/06/23
"""

from colorama import Fore
from colorama import Style
import pandas as pd
import random
from termcolor import colored

print(colored("Hello", "red"), colored("world", "green"))
# termcolor does not work as expected

# Test colorama package
print(f"This is {Fore.GREEN}color{Style.RESET_ALL}!")

# Create simple loop comparing letters to word to test colorama
# package
word_list = ["mango", "spoon", "ramen", "plate"]

alphabet = [chr(i) for i in range(ord("a"),ord("z")+1)]

solution = random.choice(word_list) 
solution

guess = random.choice(alphabet)
guess

guess_word = random.choice(word_list)
guess_word

for guess_letter,solution_letter in zip(guess_word,solution):
    
    if guess_letter == solution_letter:
        print(f"{Fore.GREEN}{guess_letter}")
        
    elif guess_letter in solution:
        print(f"{Fore.YELLOW}{guess_letter}")
    else:
        print(f"{Fore.BLACK}{guess_letter}")
        

# Colorama package works to print coloured output in the console
