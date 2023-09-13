#!/usr/bin/python3
"""
A Module for read_file()
"""


def read_file(filename=""):
    """
    A function that reads a text file (UTF8) and prints it to stdout
    Args: filename (str): default ""
    """
    with open(filename, "r", encoding="utf-8") as fle:
        print(fle.read(), end='')
