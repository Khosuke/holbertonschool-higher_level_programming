#!/usr/bin/python3
"""
This modules defines a custom object class.
"""
import pickle


class CustomObject:
    """
    This class defines a custom object.
    """
    def __init__(self, name, age, is_student):
        """
        Initialize a CustomObject
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        This method display a string representation of the object.
        """
        print("Name: {}\n"
              "Age: {}\n"
              "Is Student: {}".format(self.name, self.age, self.is_student))

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
        except FileNotFoundError:
            return None

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
                data_loaded = pickle.load(f)
            return data_loaded
        except FileNotFoundError:
            return None
