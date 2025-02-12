#!/usr/bin/python3
"""
This module defines one function: save_to_json_file()
"""
import json


def save_to_json_file(my_obj, filename):
    """
    This function writes an Object to a text file,
    using a JSON representation
    Args:
        my_obj: the object to write to a text file
        filename: the text file to write to
    """
    with open(filename, "w", encoding="UTF8") as f:
        f.write(json.dumps(my_obj))
