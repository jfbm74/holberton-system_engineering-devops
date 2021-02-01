#!/usr/bin/python3
"""Python script to export data in the JSON format"""


import json
import requests


def get_user():
    """Function that returns all users

    Returns:
        [users]: [User Data]
    """
    url = 'https://jsonplaceholder.typicode.com/'
    users = requests.get(url + 'users').json()
    return(users)


def get_tasks():
    """Returns all users's todo list

    Returns:
        [tasks]: [List of all tasks]
    """
    url = 'https://jsonplaceholder.typicode.com/'
    tasks = requests.get(url + 'todos').json()
    return tasks


def store_json(users, tasks):
    """data to JSON
    Args:
        users (list): Users
        tasks (list): Tasks
    """

    info = {}
    list_items = []
    idx = tasks[0]['userId']
    for task in tasks:
        username = users[task['userId'] - 1]['username']
        if task['userId'] != idx:
            list_items = []
            idx = task['userId']
        list_items.append({
                                'username': username,
                                'task': task['title'],
                                'completed': task['completed']})
        info[task['userId']] = list_items
    with open('todo_all_employees' + '.json', 'w') as f:
        json.dump(info, f)


if __name__ == '__main__':
    user = get_user()
    tasks = get_tasks()
    store_json(user, tasks)
