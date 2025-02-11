# Project : Python - Input/Output

## Task 0. Read file
Write a function that reads a text file (UTF8) and prints it to stdout:
File: 0-read_file.py

## Task 1. Write to a file
Write a function that writes a string to a text file (UTF8) and returns the number of characters written:
File: 1-write_file.py

## Task 2. Append to a file
Write a function that appends a string at the end of a text file (UTF8) and returns the number of characters added:
File: 2-append_write.py

## Task 3. To JSON string
Write a function that returns the JSON representation of an object (string):
File: 3-to_json_string.py

## Task 4. From JSON string to Object
Write a function that returns an object (Python data structure) represented by a JSON string:
File: 4-from_json_string.py

## Task 5. Save Object to a file
Write a function that writes an Object to a text file, using a JSON representation:
File: 5-save_to_json_file.py

## Task 6. Create object from a JSON file
Write a function that creates an Object from a “JSON file”:
File: 6-load_from_json_file.py

## Task 7. Load, add, save
Write a script that adds all arguments to a Python list, and then save them to a file:
File: 7-add_item.py

## Task 8. Class to JSON
Write a function that returns the dictionary description with simple data structure (list, dictionary, string, integer and boolean) for JSON serialization of an object:
File: 8-class_to_json.py

## Task 9. Student to JSON
Write a class Student that defines a student by:
Public instance attributes:
- first_name
- last_name
- age

## Task 10. Student to JSON with filter
Write a class Student that defines a student by: (based on 9-student.py)
Public method def to_json(self, attrs=None): that retrieves a dictionary representation of a Student instance (same as 8-class_to_json.py):
- If attrs is a list of strings, only attribute names contained in this list must be retrieved.
- Otherwise, all attributes must be retrieved
File: 10-student.py

## Task 11. Student to disk and reload
Write a class Student that defines a student by: (based on 10-student.py)
Public method def reload_from_json(self, json): that replaces all attributes of the Student instance:
- You can assume json will always be a dictionary
- A dictionary key will be the public attribute name
- A dictionary value will be the value of the public attribute
File: 11-student.py


## Task 12. Pascal's Triangle
Create a function def pascal_triangle(n): that returns a list of lists of integers representing the Pascal’s triangle of n:
- Returns an empty list if n <= 0
- You can assume n will be always an integer
File: 12-pascal_triangle.py
