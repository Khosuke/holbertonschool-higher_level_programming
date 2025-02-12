#!/usr/bin/python3
"""
This script adds all arguments to a Python list,
and then save them to a file.
"""
import json
from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


try:
    args_list = load_from_json_file("add_item.json")
except FileNotFoundError:
    args_list = []

args_list.extend(argv[1:])
save_to_json_file(args_list, "add_item.json")
