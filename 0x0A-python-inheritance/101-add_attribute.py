#!/usr/bin/python3
"""
Module for add_attribute method
"""


def add_attribute(obj, attr, value):
    """
    A function that adds a new attribute to an object if it’s possible
    Args:
        obj, attr, value
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
