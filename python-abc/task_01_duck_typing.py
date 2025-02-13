#!/usr/bin/env python3
"""

"""
from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    """
    This defines a Shape class.
    """
    @abstractmethod
    def area(self):
        """
        This abstract method calculate the area of the object
        and return its value.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        This abstract method calculate the perimeter of the object
        and return its value.
        """
        pass


class Circle(Shape):
    """
    This class defines a Circle subclass.
    """
    def __init__(self, radius):
        """
        Initialize a Circle Shape.
        Args:
            radius: The radius of the Circle.
        """
        self.radius = radius

    def area(self):
        return pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * pi * self.radius


class Rectangle(Shape):
    """
    This class defines a Rectangle subclass.
    """
    def __init__(self, height=0, width=0):
        """
        Initialize a Rectangle shape.
        Args:
            height: The height of the Rectangle.
            width: The width of the Rectangle.
        """
        self.height = height
        self.width = width

    def area(self):
        return self.height * self.height

    def perimeter(self):
        return 2 * (self.height + self.width)


def shape_info(shape):
    """
    This function prints the area and perimeter of
    the shape passed to the function
    Args:
        Shape: a Shape object
    """
    print("Area: {}\nPerimeter: {}".format(shape.area(), shape.perimeter()))
