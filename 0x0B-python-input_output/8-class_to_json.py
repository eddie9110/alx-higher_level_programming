#!/usr/bin/python3
"""
A module for the function class_to_json()
"""


def class_to_json(obj):
    """
    A function that returns the turns the 
    dictionary representation of a simple data structure
    for JSON serialization of an object.

    Args:
        obj: An object

    Return:
        dict: Dictionary representation of obj.
    """
    return obj.__dict__
