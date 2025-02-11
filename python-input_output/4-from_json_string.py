#!/usr/bin/python3
"""
This module defines one function: from_json_string()
"""
import json


def from_json_string(my_str):
    """
    This function returns an object represented by a JSON string
    Args:
        my_str: the JSON string
    Returns:
        An object represented by my_str
    """
    return json.loads(my_str)

