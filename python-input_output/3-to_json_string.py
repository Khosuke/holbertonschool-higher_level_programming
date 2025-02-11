#!/usr/bin/python3
"""
This module defines one function: to_json_string().
"""
import json


def to_json_string(my_obj):
    """
    This function returns the JSON representation of an object (string)
    Args:
        my_obj:
    Returns:
        JSON representation (string) of my_obj.
    """
    return json.dumps(my_obj)
