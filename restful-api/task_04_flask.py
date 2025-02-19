#!/usr/bin/python3
"""
This modules defines a simple API using Flask,
with multiples methods to access different routes
and handle a POST request.
"""
from flask import Flask, jsonify, request, json


app = Flask(__name__)
json.provider.DefaultJSONProvider.sort_keys = False
users = {}


@app.route("/")
def home():
    """
    This method defines a route for the root URL.

    Returns:
        A welcome message.
    """
    return "Welcome to the Flask API!"


@app.route("/data")
def jsonify_data():
    """
    This methods allows to access the 'data' route containing users data.

    Returns:
        The JSON users data.
    """
    response = jsonify(users)
    return response


@app.route("/status")
def status():
    """
    This method returns the status OK
    """
    return "OK"


@app.route("/users/<string:username>")
def dynamic_route(username):
    """
    This methods allows dynamic routing when trying
    to access a specific user data.

    Arg:
        username: the name of the user for the route access.
    Returns:
        The JSON user data if User exist.
        Else return 'error': 'User not found'.
    """
    if username in users:
        response = jsonify(users[username])
    else:
        response = jsonify({"error": "User not found"})
    return response, 200


@app.route("/add_user", methods=["POST"])
def add_user():
    """
    This method allows to make a POST request to add a new User,
    using JSON data.

    Returns:
        If a username is provided, returns confirmation message
        with the User data and status code 201.
        Else return 'error': 'Username is required'.
    """
    user_data = request.get_json()
    if 'username' not in user_data:
        return jsonify({"error": "Username is required"}), 400

    username = user_data["username"]
    users[username] = user_data.copy()
    return jsonify({"message": "User added", "user": users[username]}), 201


if __name__ == "__main__":
    app.run()
