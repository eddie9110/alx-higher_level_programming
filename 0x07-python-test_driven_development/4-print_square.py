#!/usr/bin/python3
"""
This module prints a square using the hash symbol(#)

"""


def print_square(size):
    """
    A function that prints a square with the character - (#)

    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for r in range(size):
        for c in range(size):
            print("#", end="")
        print()
