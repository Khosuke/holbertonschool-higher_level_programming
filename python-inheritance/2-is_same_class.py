#!/usr/bin/python3
"""
This module defines one function: is_same_class()
"""


def is_same_class(obj, a_class):
    """This function checks if an object
    is an instance of the specified class.
    Arguments:
        obj: the object to check if is an instance of.
        a_class: the specified class to check.
    Returns:
        True if obj is an instance of the specified class.
        False if obj is not an instance of the specified class.
    """
    if type(obj) is a_class:
        return True
    return False
