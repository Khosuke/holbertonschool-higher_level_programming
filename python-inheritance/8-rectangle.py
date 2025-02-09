#!/usr/bin/python3
"""
This module defines a Rectangle class that inherits form BaseGeometry
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A Rectanlge class that inherits from BaseGeometry class.
    """

    def __init__(self, width, height):
        """
        Initialize a new Rectangle object.
        Arguments:
            width: the width of the rectangle.
            height: the height of the rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
