#!/usr/bin/python3
"""
Module that returns information about TO DO list
progress for a given employee ID
"""


import csv
import json
from sys import argv

import requests


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
    employee_name = user[0]['username']
    all_tasks = tasks
    completed = 0
    title_completed_tasks = ''
    for task in all_tasks:
        if task['completed'] is True:
            completed += 1
            title_completed_tasks += '\t ' + task['title'] + '\n'
    print('Employee {} is done with tasks({}/{}):'
          .format(employee_name, completed, len(all_tasks)))
    print(title_completed_tasks, end='')


def export_csv(user, tasks):
    """Python script to export data in the CSV format.

    Args:
        user  : User Object
        tasks : Collection of User's Tasks
    """
    employee_name = user[0]['name']
    employee_id = user[0]['id']
    csvfile = '{}.csv'.format(employee_id)
    with open(csvfile, mode='w') as file:
        towrite = csv.writer(file, delimiter=',', quoting=csv.QUOTE_ALL)
        for task in tasks:
            towrite.writerow([employee_id, employee_name,
                              task['completed'], task['title']])


def export_json(user, tasks):
    """Python script to export data in the JSON format.

    Args:
        user  : User Object
        tasks : Collection of User's Tasks
    """
    employee_name = user[0]['username']
    employee_id = user[0]['id']
    all_tasks = []
    json_file = '{}.json'.format(employee_id)
    for task in tasks:
        all_tasks.append({
            'task': task['title'],
            'completed': task['completed'],
            'username': employee_name
            })
    dict_user = {}
    dict_user[argv[1]] = all_tasks
    with open(json_file, mode='w') as file:
        file_row = json.dumps(dict_user)
        file.write(file_row)


if __name__ == '__main__':
    user = get_user(argv[1])
    tasks = get_tasks(argv[1])
    export_json(user, tasks)
