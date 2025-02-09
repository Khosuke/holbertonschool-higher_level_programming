#!/usr/bin/python3
"""
This module defines one function : inherits_from()
"""


def inherits_from(obj, a_class):
    """
    This Function checks if an object is an 
    inherited instance of a class.
    Arguments:
        obj: The object to check.
        a_class: The class to compare against.
    Returns:
        True if the object is an instance that inherited
        from the specified class or else False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
