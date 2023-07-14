
# coding: utf-8

""" This script creates and saves a five-letter word dictionary 
using the words dictionary found here https://github.com/gokhanyavas/Oxford-3000-Word-List.
This dictionary is used to pick a random word to be guessed in the wordle game.

Author: Hacking Housing Analysis
Date: June 2023"""

import pandas as pd

f = pd.read_fwf("Oxford_3000_Dictionary.txt")
f

len(f)

f["a"]=f["a"].astype("str")

len(f["a"])

five_letter_df = f[f["a"].str.len()==5]

five_letter_df.head()

len(five_letter_df)

five_letter_df.rename(columns = {"a": "word"}, inplace=True)

five_letter_df.reset_index(drop=True, inplace=True)

five_letter_df.count()

five_letter_df.head()

five_letter_df.tail()

# convert the words to UPPERCASE
five_letter_df["word"] = five_letter_df["word"].str.upper()

five_letter_df.head()

five_letter_df.to_csv("wordle_dictionary.csv")