#!/usr/bin/python3
"""
Module for append_after()
"""


def append_after(filename="", search_string="", new_string=""):
    """
    A function that inserts a line of text to a file,
    after each line containing a specific string
    Args:
        filename (str)
        search_string (str)
        new_string (str)
    """
    with open(filename, "r") as fle:
        string = fle.readlines()
    with open(filename, "w") as fle:
        for line in string:
            fle.write(line)
            if search_string in line:
                fle.write(new_string)
