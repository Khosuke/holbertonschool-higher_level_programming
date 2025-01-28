#!/usr/bin/python3
"""Define a Rectangle class."""


class Rectangle():
    """Create a Rectangle class."""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """width: the 'width' of the Rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the Rectangle.
        Arg:
            value: an int for the size of the Rectangle.
        Raises:
            TypeError if 'value' is not an int.
            ValueError if 'value' is negative.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """height: the 'height' of the Rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the Rectangle.
        Arg:
            value: an int for the size of the Rectangle.
        Raises:
            TypeError if 'value' is not an int.
            ValueError if 'value' is negative.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return:
            The Area of the rectangle
        """
        return self.height * self.width

    def perimeter(self):
        """Return:
            The Perimeter of the rectangle
        """
        if self.width == 0 or self.height == 0:
            return 0
        return ((self.width * 2) + (self.height * 2))

    def __str__(self):
        """Return:
            A string to print the rectangle
        """
        rectangle_str = ""
        if self.width == 0 or self.height == 0:
            return rectangle_str
        for i in range(self.height):
            for j in range(self.width):
                rectangle_str += '#'
            rectangle_str += '\n'
        return rectangle_str.strip()

    def __repr__(self):
        """Return:
            A string representation of the rectangle to recreate it
        """
        return f"Rectangle({self.width}, {self.height})"
