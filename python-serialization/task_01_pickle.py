#!/usr/bin/python3
"""
This modules defines a custom object class.
"""
import pickle


class CustomObject:
    """
    This class defines a custom object.
    """
    def __init__(self, name="", age=0, is_student=True):
        """
        Initialize a CustomObject
        Args:
            name: The name of the person
            age: The age of the person
            is_student: Whether the person is a student
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        This method display a string representation of the object.
        """
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """
        This method serialize the current instance of the object
        and save it to the provided filename.
        Args:
            filename: name of the file
        """
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except pickle.PicklingError as e:
            return

    @classmethod
    def deserialize(cls, filename):
        """
        This method will load and return an instance of the CustomObject
        from the provided filename.
        Args:
            filename: Name of the file.
        Returns:
            An instance of the CustomObject.
        """
        try:
            with open(filename, "rb") as f:
                return pickle.load(f)
        except (FileNotFoundError, pickle.UnpicklingError) as e:
            return
