# Project : Python - Object-relational mapping

### Task 0. Get all states
Write a script that lists all ``states`` from the database ``hbtn_0e_0_usa``:
- This script should take 3 arguments: ``mysql username``, ``mysql password`` and ``database name``.
- It uses the ``MySQLdb`` module.
- Results are sorted in ascending order by ``states.id``
File: 0-select_states.py

### Task 1. Filter states
Write a script that lists all ``states`` with a ``name`` starting with ``N`` (upper N) from the database ``hbtn_0e_0_usa``:
- This script should take 3 arguments: ``mysql username``, ``mysql password`` and ``database name``.
- Results are sorted in ascending order by ``states.id``
File: 1-filter_states.py

### Task 2. Filter states by user input
Write a script that takes in an argument and displays all values in the ``states`` table of ``hbtn_0e_0_usa`` where ``name`` matches the argument.
- This script should take 4 arguments: ``mysql username``, ``mysql password``, ``database name`` and ``state name searched``.
- You must use ``format`` to create the SQL query with the user input.
- Results are sorted in ascending order by ``states.id``
File: 2-my_filter_states.py

### Task 3. SQL Injection...
Once again, write a script that takes in arguments and displays all values in the ``states`` table of ``hbtn_0e_0_usa`` where ``name`` matches the argument. But this time, write one that is safe from MySQL injections!
- This script should take 4 arguments: ``mysql username``, ``mysql password``, ``database name`` and ``state name searched``.
- Results are sorted in ascending order by ``states.id``
File: 3-my_safe_filter_states.py

### Task 4. Cities by states
Write a script that lists all ``cities`` from the database ``hbtn_0e_4_usa``.
- This script should take 3 arguments: ``mysql username``, ``mysql password`` and ``database name``.
- Results are sorted in ascending order by ``cities.id``.
- You can use only ``execute()`` once.
File: 4-cities_by_state.py

### Task 5. All cities by state
Write a script that takes in the name of a state as an argument and lists all cities of that state, using the database hbtn_0e_4_usa.
- This script should take 4 arguments: ``mysql username``, ``mysql password``, ``database name`` and ``state name`` (SQL injection free!)
- Results must be sorted in ascending order by ``cities.id``.
File: 5-filter_cities.py

### Task 6. First state model
Write a python file that contains the class definition of a ``State`` and an instance ``Base = declarative_base()``:
- ``State`` class:
    - inherits from ``Base``.
    - links to the MySQL table ``states``.
    - class attribute ``id`` that represents a column of an auto-generated, unique integer, can’t be null and is a primary key.
    - class attribute ``name`` that represents a column of a string with maximum 128 characters and can’t be null.
- It must use the module ``SQLAlchemy``.
File: model_state.py

### Task 7. All states via SQLAlchemy
Write a script that lists all ``State`` objects from the database ``hbtn_0e_6_usa``.
- This script should take 3 arguments: ``mysql username``, ``mysql password`` and ``database name``.
- You must import ``State`` and ``Base`` from ``model_state`` - ``from model_state import Base, State``.
- Results must be sorted in ascending order by ``states.id``.
File: 7-model_state_fetch_all.py

### Task 8. First state
Write a script that prints the first ``State`` object from the database ``hbtn_0e_6_usa``.
- This script should take 3 arguments: ``mysql username``, ``mysql password`` and ``database name``.
- You must import ``State`` and ``Base`` from ``model_state`` - ``from model_state import Base, State``.
- The state you display must be the first in ``states.id``.
- If the table ``states`` is empty, print ``Nothing`` followed by a new line.
File: 8-model_state_fetch_first.py

### Task 9. Contains \`a\`
Write a script that lists all ``State`` objects that contain the letter ``a`` from the database ``hbtn_0e_6_usa``.
- This script should take 3 arguments: ``mysql username``, ``mysql password`` and ``database name``.
- Results must be sorted in ascending order by ``states.id``.
File: 9-model_state_filter_a.py

### Task 10. Get a state
Write a script that prints the ``State`` object with the ``name`` passed as argument from the database ``hbtn_0e_6_usa``.
- This script should take 4 arguments: ``mysql username``, ``mysql password``, ``database name`` and ``state name to search`` (SQL injection free)
- Results must display the ``states.id``.
- If no state has the name you searched for, display ``Not found``.
File: 10-model_state_my_get.py

### Task 11. Add a new state
Write a script that adds the ``State`` object “Louisiana” to the database ``hbtn_0e_6_usa``.
- This script should take 3 arguments: ``mysql username``, ``mysql password`` and ``database name``.
- Print the new ``states.id`` after creation.
File: 11-model_state_insert.py

### Task 12. Update a state
Write a script that changes the name of a ``State`` object from the database ``hbtn_0e_6_usa``.
- This script should take 3 arguments: ``mysql username``, ``mysql password`` and ``database name``.
- Change the name of the ``State`` where ``id = 2`` to ``New Mexico``.
File: 12-model_state_update_id_2.py

### Task 13. Delete states
Write a script that deletes all ``State`` objects with a name containing the letter ``a`` from the database ``hbtn_0e_6_usa``.
- This script should take 3 arguments: ``mysql username``, ``mysql password`` and ``database name``.
File: 13-model_state_delete_a.py

### Task 14. Cities in state
Write a Python file similar to ``model_state.py`` named ``model_city.py`` that contains the class definition of a ``City``.
- ``City`` class:
    - inherits from ``Base`` (imported from model_state)
    - links to the MySQL table ``cities``.
    - class attribute ``id`` that represents a column of an auto-generated, unique integer, can’t be null and is a primary key.
    - class attribute ``name`` that represents a column of a string of 128 characters and can’t be null.
    - class attribute ``state_id`` that represents a column of an integer, can’t be null and is a foreign key to ``states.id``.
Next, write a script ``14-model_city_fetch_by_state.py`` that prints all ``City`` objects from the database ``hbtn_0e_14_usa``:
- This script should take 3 arguments: ``mysql username``, ``mysql password`` and ``database name``.
- Results must be sorted in ascending order by ``cities.id``.
- Results must be display as they are in the example below (``<state name>``: (``<city id>``) ``<city name>``)
File: model_city.py, 14-model_city_fetch_by_state.py
