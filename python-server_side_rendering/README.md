# Project : 

### Task 0. Creating a Simple Templating Program

Create a Python function that generates personalized invitation files from a template with placeholders and a list of objects. Each output file should be named sequentially, starting from 1. Implement specific error handling for various edge cases.

File: task_00_intro.py

### Task 1. Creating a Basic HTML Template in Flask

Build a basic Flask application that serves a web page using a Jinja template. 
Create a simple HTML template that includes various elements like headings, paragraphs, and lists, and learn how to render it as a web page using Flask.
Additionally, create reusable templates for headers and footers to promote code reusability and consistency across multiple pages.

File: task_01_jinja.py

### Task 2. Creating a Dynamic Template with Loops and Conditions in Flask

Enhance your Flask application by integrating dynamic content into your HTML templates using Jinja’s loop and conditional constructs. It will read a list of items from a JSON file and display them dynamically on a web page.

File: task_02_logic.py

### Task 3. Displaying Data from JSON or CSV Files in Flask

Build a feature in your Flask application to read and display product data from two different data formats: JSON and CSV. You will create a single HTML template that can display data from either file type, depending on a query parameter provided in the URL. You will add functionality to your Flask application to filter product data based on an optional ``id`` query parameter. Additionally, you will handle edge cases such as invalid ``source`` parameter values or when the specified ``id`` is not found in the data.

File: task_03_files.py


### Task 4. Extending Dynamic Data Display to Include SQLite in Flask

Building on the previous exercise, you will now add the functionality to fetch and display data from a SQLite database in your Flask application. The application should allow users to choose between JSON, CSV, and SQL (SQLite database) as data sources using the ``source`` query parameter.

File: task_04_db.py
