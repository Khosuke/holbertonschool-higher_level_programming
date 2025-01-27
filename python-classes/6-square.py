#!/usr/bin/python3
""" Create a square class."""


class Square:
    """Define a square class.

    Attributes:
        size (int): The size of the square.
        position (:tuple: int, int): The position of the square.

    """
    def __init__(self, size=0, position=(0, 0)):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        if (not isinstance(position, tuple) or len(position) != 2 or not
                all(isinstance(elem, int) and elem >= 0 for elem in position)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.size = size
        self.position = position

    @property
    def size(self):
        """size: the 'size' of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.
        Arg:
            value: an int for the size of the square.
        Raises:
            TypeError if 'value' is not an int.
            ValueError if 'value' is negative.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Area() return the area of the square which is 'size * size'.

        Returns:
            int: size * size
        """
        return self.__size * self.__size

    def my_print(self):
        """my_print() prints the square using
            its 'size' and 'position' attributes.
        """
        if self.__size == 0:
            print()
        for x in range(self.__position[1]):
            print()
        for i in range(self.__size):
            for y in range(self.__position[0]):
                print(" ", end="")
            for j in range(self.__size):
                print("#", end="")
            print()

    @property
    def position(self):
        """position() return the position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square.
        Arg:
            value: a tuple for the coordinates of the square
        Raises:
            TypeError if 'value' is not a tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple) or len(value) != 2 or not
                all(isinstance(elem, int) and elem >= 0 for elem in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
