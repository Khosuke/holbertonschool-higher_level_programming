# Project : Python - More Classes and Objects


## Task 0. Simple rectangle
Write an empty class ``Rectangle`` that defines a rectangle:
File: 0-rectangle.py

## Task 1. Real definition of a rectangle
Write a class ``Rectangle`` that defines a rectangle by: (based on 0-rectangle.py)

- Private instance attribute: ``width:`` 
    - property ``def width(self):`` to retrieve it 
    - property setter ``def width(self, value):`` to set it
- Private instance attribute: ``height:``
    - property ``def height(self):`` to retrieve it
    - property setter ``def height(self, value):`` to set it
- Instantiation with optional ``width`` and ``height``: ``def __init__(self, width=0, height=0):``

File: 1-rectangle.py


## Task 2. Area and Perimeter
Write a class ``Rectangle`` that defines a rectangle by: (based on 1-rectangle.py)
- Public instance method: ``def area(self):`` that returns the rectangle area
- Public instance method: ``def perimeter(self):`` that returns the rectangle perimeter:
if width or height is equal to 0, perimeter is equal to 0

File: 2-rectangle.py


## Task 3. String representation
Write a class ``Rectangle`` that defines a rectangle by: (based on 2-rectangle.py)
- ``print()`` and ``str()`` should print the rectangle with the character ``#``:
if ``width`` or ``height`` is equal to 0, return an empty string

File: 3-rectangle.py


## Task 4. Eval is magic
Write a class ``Rectangle`` that defines a rectangle by: (based on 3-rectangle.py)
- ``repr()`` should return a string representation of the rectangle to be able to recreate a new instance by using ``eval()``

File: 4-rectangle.py


## Task 5. Detect instance deletion
Write a class ``Rectangle`` that defines a rectangle by: (based on 4-rectangle.py)
- Print the message ``Bye rectangle...`` (``...`` being 3 dots not ellipsis) when an instance of ``Rectangle`` is deleted

File: 5-rectangle.py


## Task 6. How many instances
Write a class ``Rectangle`` that defines a rectangle by: (based on 5-rectangle.py)
- Public class attribute ``number_of_instances``:
    - Initialized to ``0``
    - Incremented during each new instance instantiation
    - Decremented during each instance deletion

File: 6-rectangle.py


## Task 7. Change representation
Write a class ``Rectangle`` that defines a rectangle by: (based on 6-rectangle.py)
- Public class attribute ``print_symbol``:
    - Initialized to ``#``
    - Used as symbol for string representation
    - Can be any type

File: 7-rectangle.py


## Task 8. Compare rectangles
Write a class ``Rectangle`` that defines a rectangle by: (based on 7-rectangle.py)
- Static method ``def bigger_or_equal(rect_1, rect_2)``: that returns the biggest rectangle based on the area
    - ``rect_1`` must be an instance of ``Rectangle``, otherwise raise a ``TypeError`` exception with the message ``rect_1 must be an instance of Rectangle``
    - ``rect_2`` must be an instance of ``Rectangle``, otherwise raise a ``TypeError`` exception with the message ``rect_2 must be an instance of Rectangle``
    - Returns ``rect_1`` if both have the same area value

File: 8-rectangle.py


## Task 9. A square is a rectangle
Write a class ``Rectangle`` that defines a rectangle by: (based on 8-rectangle.py)
- Class method ``def square(cls, size=0)``: that returns a new Rectangle instance with ``width == height == size``

File: 9-rectangle.py

