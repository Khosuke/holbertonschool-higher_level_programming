#!/usr/bin/python3
"""
This module defines one function : is_kind_of_class()
"""


def is_kind_of_class(obj, a_class):
    """
    This function returns True if the object is an instance of a class
    that inherited from the specified class or otherwise False.
    Arguments:
        obj: The object to check with the a_class.
        a_class: The specified class to compare.
    Returns:
        True if obj is an instance of the specified class.
        False if obj is not an instance of the specified class.
    """
    if (isinstance(obj, a_class)):
        return True
    return False
