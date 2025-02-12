#!/usr/bin/python3
"""
This module defines a Student class.
"""


class Student:
    """
    This is a class 'Student' that defines a student by:
    Public instance attributes: 'first_name', 'last_name', 'age'
    """
    def __init__(self, first_name, last_name, age):
        """
        Initialize a student
        Args:
            first_name: The first name of the student
            last_name: The last name of the student
            age: The age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns a dictionary representation of a Student instance.
        If attrs is a list of strings, only attribute names contained
        in this list will be returned.
        Args:
            attrs: The attributes to represent. (optional)
        """
        if (type(attrs) is list and
                all(type(element) is str for element in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
