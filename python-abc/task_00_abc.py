#!/usr/bin/env python3
"""
This modules defines an Animal Class
with a Cat and Dog subclass.
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """
    This class defines an Animal.
    """
    @abstractmethod
    def sound(self):
        """
        This is an abstract method to make a sound.
        """
        pass

class Cat(Animal):
    """
    This class defines a Cat subclass.
    """
    def sound(self):
        return "Meow"
    
class Dog(Animal):
    """
    This class defines a Dog subclass.
    """
    def sound(self):
        return "Bark"
