#!/usr/bin/python3
"""
This modules defines two functions:
fetch_and_print_posts()
fetch_and_save_posts()
"""
import requests
import csv


def fetch_and_print_posts():
    """
    This function fetches all post from JSONPlaceholder,
    prints the status code and iterate through the parsed
    JSON data and print out the titles of all the posts.
    """
    get_posts = requests.get("https://jsonplaceholder.typicode.com/posts")
    print("Status code: {}".format(get_posts.status_code))
    if get_posts.status_code == 200:
        posts_data = get_posts.json()
        for i in range(len(posts_data)):
            title_content = posts_data[i]["title"]
            print("{}".format(title_content))


def fetch_and_save_posts():
    """
    This function fetches all post from JSONPlaceholder, 
    structures the data into a list of dictionaries, 
    with keys and values for 'id', 'title', and 'body'.
    And writes this data into a CSV file.
    """
    posts_dict = []
    get_posts = requests.get("https://jsonplaceholder.typicode.com/posts")
    if get_posts.status_code == 200:
        data = get_posts.json()
        for i in range(len(data)):
            data[i].pop('userId')
            posts_dict.append(data[i])
            

        with open("posts.csv", "w", newline="") as csv_file:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(posts_dict)

