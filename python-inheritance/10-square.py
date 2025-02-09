#!/usr/bin/python3
"""
This module defines a Square class that inherits
from the Rectangle class.
"""
RectangleClass = __import__("9-rectangle").Rectangle


class Square(RectangleClass):
    """
    A Square class that inherits from Rectangle class.
    """

    def __init__(self, size):
        """
        Initialize a new Square object.
        Args:
            size: the size of the Square
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        Returns the area of the square.
        """
        return (self.__size * self.__size)
