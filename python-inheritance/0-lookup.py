#!/usr/bin/python3
"""
This module adds the function "lookup()".
"""


def lookup(obj):
    """
    This function returns the list of available
    attributes and methods of an object.
    Argument:
        obj: an object
    Return:
        A list of available attributes and methods.
    """
    return dir(obj)
