
# coding: utf-8

"""This script creates and saves a five-letter dictionary which is more 
extensive than the Oxford learners 3000. 
The dictionary file was downloaded from here: https://github.com/dwyl/english-words
This dictionary will be used when validating input guesses."""

import json
import pandas as pd

f = open("words_dictionary.json")

original_dict = json.load(f)
len(original_dict)

original_dict.keys()

d = dict((k, v) for k, v in original_dict.items() if len(k) == 5)
len(d)

five_letter_df = pd.DataFrame(d.items())

five_letter_df.rename(columns = {0: "word"}, inplace=True)

five_letter_df = five_letter_df[["word"]]

five_letter_df.count()

five_letter_df.head()

five_letter_df["word"] = five_letter_df["word"].str.upper()

five_letter_df.head()

five_letter_df.to_csv("checking_dictionary.csv")