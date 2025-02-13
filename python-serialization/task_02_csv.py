#!/usr/bin/env python3
"""
Script to convert CSV file to JSON format.
"""
import csv
import json


def convert_csv_to_json(filename):
    """
    Convert a CSV file to JSON format where each row becomes a dictionary.
    Args:
        filename: Path to the CSV file.
    Returns:
        bool: True if successful, False otherwise.
    """
    data = []
    try:
        with open(filename, encoding="UTF8") as csv_File:
            csv_reader = csv.DictReader(csv_File)
            for row in csv_reader:
                data.append(row)
        with open("data.json", "w", encoding="UTF8") as json_file:
            return json_file.write(json.dumps(data))
    except FileNotFoundError:
        return False
