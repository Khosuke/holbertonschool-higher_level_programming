#!/usr/bin/python3
"""
This module defines two functions: 
    serialize_and_save_to_file()
    load_and_deserialize()
"""
import json


def serialize_and_save_to_file(data, filename):
    """
    This function 
    Args:
        data: A Dictionary with data.
        filename: Name of the JSON output file.
    """
    with open(filename, "w", encoding="UTF8") as f:
        f.write(json.dumps(data))

def load_and_deserialize(filename):
    """
    This function load and deserialize data from the specified file.
    Arg:
        filename: The filename of the JSON file.
    Returns:
        A Python dictionary with the deserialized JSON data from the file.
    """
    with open(filename, "r", encoding="UTF8") as f:
        my_str = f.readline()
    return json.loads(my_str)
