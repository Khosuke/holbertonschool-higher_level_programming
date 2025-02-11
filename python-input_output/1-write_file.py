#!/usr/bin/python3
"""
This module defines one function: write_file().
"""


def write_file(filename="", text=""):
    """
    This function writes a string to a text file.
    Args:
        filename: The name of the file.
        text: the string to write to the file.
    Returns:
        The number of characters written.
    """
    with open(filename, 'w', encoding="utf-8") as f:    
        return f.write(text)
