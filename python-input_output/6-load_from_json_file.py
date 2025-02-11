#!/usr/bin/python3
"""
This module defines one function: load_from_json_file()
"""
import json


def load_from_json_file(filename):
    """
    This function creates an Object from a JSON file.
    Args:
        filename: the JSON file.
    """
    with open(filename, "r", encoding="UTF8") as f:
        my_str = f.readline()
    return json.loads(my_str)
