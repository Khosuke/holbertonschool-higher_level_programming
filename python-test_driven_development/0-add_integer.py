#!/usr/bin/python3
"""
This is the "add_integer" module

This module supplies one function: add_integer(). For example,

>>> add_integer(5, 6)
11
"""


def add_integer(a, b=98):
    """
    Return the sum of two numbers, a and b that must be integers or floats
    if only one argument is passed, b equals 98
    A TypeError exception is raised if a or b are not integers or float
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
