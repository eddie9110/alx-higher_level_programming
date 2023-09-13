#!/usr/bin/python3
"""
Module of to_json_string() function
"""
import json


def to_json_string(my_obj):
    """
    A  function that takes an object as a parameter & 
    returns the JSON representation of an object (string):
    """
    return json.dumps(my_obj)
