
# coding: utf-8

""" This script creates a five letter word dictionary (pandas dataframe) 
using the words dictionary found here https://github.com/gokhanyavas/Oxford-3000-Word-List"""

import json
import pandas as pd

f = pd.read_fwf(r"Z:\C&C Hackathon\Oxford_3000_Dictionary.txt")

f

len(f)

f['a']=f['a'].astype('str')

len(f['a'])

five_letter_df = f[f['a'].str.len()==5]

five_letter_df.head()

len(five_letter_df)

five_letter_df.rename(columns = {'a':'word'}, inplace=True)

five_letter_df.reset_index(drop=True, inplace=True)

five_letter_df.count()

five_letter_df.head()

five_letter_df.tail()

# convert the words to UPPERCASE
five_letter_df["word"] = five_letter_df["word"].str.upper()

five_letter_df.head()

