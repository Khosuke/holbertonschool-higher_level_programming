#!/usr/bin/env python3
"""
This modules defines a VerboseList with multiples methods.
"""


class VerboseList(list):
    """
    This defines the VerboseList subclass of list.
    """
    def append(self, item):
        """
        This method appends an item to the list.
        """
        super().append(item)
        print("Added [{}] to the list".format(item))

    def extend(self, x):
        """
        This method extends the list with one or multiple elements.
        """
        super().extend(x)
        print("Extended the list with [{}] items".format(len(x)))

    def remove(self, item):
        """
        This method removes an item from the list.
        """
        if item not in self:
            raise ValueError(f"Item '{item}' does not exist in the list")
        print("Removed [{}] from the list".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """
        This method removes an item at the chosen index.
        """
        if not self:
            raise IndexError("Cannot pop from an empty list")
        try:
            item = super().pop(index)
            print("Popped [{}] from the list.".format(item))
            return item
        except IndexError:
            raise IndexError("List index {} is out of range".format(index))
