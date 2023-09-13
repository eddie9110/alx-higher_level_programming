#!/usr/bin/python3
"""
Module for the save_to_json_file() function
"""
import json


def save_to_json_file(my_obj, filename):
    """
    A function that writes an object to a text file using a JSON representation
    Args:
        my_obj (obj): content to be JSON-ed and written
        filename (str): name of file
    """
    with open(filename, "w", encoding="utf-8") as file:
        file.write(json.dumps(my_obj))
