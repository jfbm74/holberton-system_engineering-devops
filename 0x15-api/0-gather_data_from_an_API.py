#!/usr/bin/python3
"""
Module that returns information about TO DO list
progress for a given employee ID
"""


import requests
from sys import argv


def get_user(id):
    """Function that returns a given user

    Args:
        id (int): ID Employee

    Returns:
        [user]: [User Data]
    """
    url = 'https://jsonplaceholder.typicode.com/'
    user = requests.get(url + 'users', params={'id': id}).json()
    return user


def get_tasks(id):
    """Returns a given user's todo list

    Args:
        id ([int]): ID Employee

    Returns:
        [tasks]: [List of tasks]
    """
    url = 'https://jsonplaceholder.typicode.com/'
    tasks = requests.get(url + 'todos', params={'userId': id}).json()
    return tasks


def show_tasks_status(user, tasks):
    """Shows information about his/her TO DO list progress.

    Args:
        user ([user]): [User Object]
        tasks ([tasks]): [Tasks Object]
    """
    employee_name = user[0]['name']
    completed = 0
    title_completed_tasks = ''
    for task in tasks:
        if task['completed'] is True:
            completed += 1
            title_completed_tasks += '\t ' + task['title'] + '\n'
    print('Employee {} is done with tasks({}/{}):'
          .format(employee_name, completed, len(tasks)))
    print(title_completed_tasks, end='')


if __name__ == '__main__':
    user = get_user(argv[1])
    tasks = get_tasks(argv[1])
    show_tasks_status(user, tasks)
