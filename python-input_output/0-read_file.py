#!/usr/bin/python3
"""
This modules defines one function: read_file().
"""


def read_file(filename=""):
    """
    This function reads a text file and prints it to stdout.
    Args:
        filename: the name of the file to read.
    """
    with open(filename, encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end="")
