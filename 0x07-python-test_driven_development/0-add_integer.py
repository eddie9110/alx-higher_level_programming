#!/usr/bin/python3
"""
This module adds two integers

"""


def add_integer(a, b=98):
    """
    A function that adds 2 integers.
    Args: a & b=98(optional argument)

    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    a = int(a)
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    b = int(b)

    return a + b
