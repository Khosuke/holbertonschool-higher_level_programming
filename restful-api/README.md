# Project: Restful API

### Task 2. Consuming and processing data from an API using Python
- Create a function `fetch_and_print_posts()` that fetches all post from JSONPlaceholder
    - Print the status code of the response i.e. `Status Code: 200`
    - If the request was sucessfull, parse the fetched data into a JSON object using the `.json()` method of the response object.
    - Iterate through the parsed JSON data and print out the titles of all the posts.
- Create a function `fetch_and_save_posts()` that fetches all post from JSONPlaceholder.
    - If the request was sucessfull, instead of printing titles, structure the data into a list of dictionaries, where each dictionary represents a post with keys and values for `id`, `title`, and `body`.
    - Using Python’s `csv` module, write this data into a CSV file called `posts.csv` with columns corresponding to the dictionary keys.

### Task 3. Develop a simple API using Python with the `http.server` module

**Objective:**
1. Set up a basic web server using the ``http.server`` module.
2. Handle different types of HTTP requests (GET, POST, etc.).
3. Serve JSON data in response to specific endpoints.

**Expected output:**
1. On visiting ``http://localhost:8000``, you should see the text: “Hello, this is a simple API!”.
2. On accessing the endpoint ``/data``, a JSON response with the sample dataset should be returned: ``{"name": "John", "age": 30, "city": "New York"}``.
3. When visiting ``/info``, you might see something like: ``{"version": "1.0", "description": "A simple API built with http.server"}``.
4. Accessing any other undefined endpoint should return a ``404 Not Found`` status with a message like “Endpoint not found”.
