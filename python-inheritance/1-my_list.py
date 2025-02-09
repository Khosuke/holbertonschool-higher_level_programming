#!/usr/bin/python3
"""
This is a module that defines the MyList class
"""


class MyList(list):
    """
    The MyList class inherits from 'list'
    """
    def print_sorted(self):
        """
        Prints the list, but sorted
        """
        print(sorted(self))
