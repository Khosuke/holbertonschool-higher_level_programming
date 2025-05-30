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

    def to_json(self):
        """
        Returns a dictionary representation of a Student instance.
        """
        return self.__dict__
