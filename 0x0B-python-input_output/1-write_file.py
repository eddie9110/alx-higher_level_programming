#!/usr/bin/python3
"""
Module for the function write_file()
"""


def write_file(filename="", text=""):
    """
    A function that writes a string to a text file (UTF8)
    and returns the number of characters written

    Args:
        filename (str): name of file
        text (str): content to be written
    """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
