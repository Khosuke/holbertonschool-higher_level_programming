#!/usr/bin/env python3
"""
This modules defines two functions:
Serializing and Deserializing with XML
"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    This function serialize the dictionary into XML
    and save it to the given filename.
    Args:
        dictionary: The python dictionary to serialize
        filename: The name of the output file.
    """
    root = ET.Element("data")

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)
    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):
    """
    This function deserialize a file from XML
    into a Python dictionary.
    Args:
        filename: The name of the XML file to deserialize.
    Returns:
        A Python dictionary.
    """
    tree = ET.parse(filename)
    root = tree.getroot()

    python_dict = {}
    for child in root:
        python_dict[child.tag] = child.text

    return python_dict
