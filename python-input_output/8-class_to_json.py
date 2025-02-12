#!/usr/bin/python3
"""
This module defines one function: class_to_json()
"""


def class_to_json(obj):
    """
    This function returns the dictionary description with simple
    data structure (list, dictionary, string, integer and boolean)
    for JSON serialization of an object.
    Args:
        obj: is an instance of a Class.
    Returns:
        The dict representation of obj.
    """
    return obj.__dict__
