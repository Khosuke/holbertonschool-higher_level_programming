#!/usr/bin/python3
"""
This is the text_indentation module
This module supplies one function: text_indentation(). For example,

>>> text_indentation("Hello World, this is a test text: Does it work ? Yes !")
Hello World, this is a test text:

Doest it Work ?

Yes !
"""


def text_indentation(text):
    """
    This function prints text with two new
    lines after each '.', '?', and ':' characters.
        The 'text' argument is the text to print and must be a string.
        A TypeError is raised if 'text' is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    text = text.lstrip()

    for i in range(len(text)):
        print(text[i], end="")
        if text[i] in ".?:":
            print("\n")
            while i + 1 < len(text) and text[i + 1] == ' ':
                i += 1
