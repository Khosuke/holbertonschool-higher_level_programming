#!/usr/bin/python3
"""
This module define one function: append_write().
"""


def append_write(filename="", text=""):
    """
    This function appends a string at the end of a text file.
    Args:
        filename: the name of the file.
        text: the string to append to the file.
    Returns:
        The number of characters added to the text file.
    """
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
