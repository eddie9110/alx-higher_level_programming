#!/usr/bin/python3
"""
Module to seperate text based on delimiter characters
"""


def text_indentation(text):
    """
    A ftn that prints a text with 2 new lines
    after: ., ? and :

    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    inpt = ""
    delim_ = [".", "?", ":"]
    n_txt = []
    

    for xter in text:
        inpt += xter
        if xter in delim_:
            n_txt.append(inpt.replace(" \n", "\n").replace("\n ", "\n"))
            inpt = ""
    else:
        if inpt != "":
            n_txt.append(inpt.replace(" \n", "\n").replace("\n ", "\n"))

    for inpt in n_txt:
        print(inpt.strip(" \t"), end="")
        for ui in delim_:
            if ui in inpt:
                print(end="\n\n")
                break
