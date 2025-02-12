#!/bin/python3

import sys # system functions and parameters

from datetime import datetime as dt # alias
print(dt.now()) # 2023-02-09 16:47:45.017222

print("\n")

# Advanced Strings
print("Advanced strings:")
my_name = "Jack my name"
print(my_name[0]) # first initial # J
print(my_name[-1]) # last letter  # e

sentence = "This is a sentence"
print(sentence[:4]) # first word               # This
print(sentence[-8:]) # last word               # sentence
print(sentence[-9:]) # last word but one space #  sentence

print(sentence.split()) # ['This', 'is', 'a', 'sentence']
print('\n')
sentence_split = sentence.split() 
sentece_join = ' '.join(sentence_split)
print(sentece_join) # This is a sentence
print('\n')

quoteception = "I said, 'give me all the money' " 
print(quoteception) # I said, 'give me all the money' 
quoteception = "I said, \"give me all the money\"" 
print(quoteception) # I said, "give me all the money" 


print("A" in "Apple") # True
print("a" in "Apple") # False

letter = "a"
word = "Apple"
word_two = "Bingo"
                                # True and not False => True
print((letter.lower() in word.lower()) and not (letter.lower() in word_two.lower())) # True

too_much_space = "         hello         "
print(too_much_space.strip()) # hello

full_name = "eath adams"
new_name = full_name.replace("eath", "heath") # heeath adams
print(new_name.title()) # Heath Adams
print(full_name.find("adams")) # 5 


def favorite_book(title, author):
    fav = f"My favorite book is {title}, which is written by {author}.".title()    
    format = "My favorite book is {}, which is written by {}.".format(title, author).split()
    return fav, format
print(favorite_book("atomic Habits", "james")) 
# ('My Favorite Book Is Atomic Habits, Which Is Written By James.', 
# ['My', 'favorite', 'book', 'is', 'atomic', 'Habits,', 'which', 'is', 'written', 'by', 'james.'])

