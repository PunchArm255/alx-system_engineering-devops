#!/usr/bin/python3
"""
This script displays user's tasks using {JSON} Placeholder REST API
"""


def export_json(user, tasks):
    """
    Export TODO list into JSON file
    """
    import json

    infos = []
    for task in tasks:
        task_info = {
            'task': task.get('title'),
            'completed': task.get('completed'),
            'username': user.get('username'),
        }
        infos.append(task_info)
    content = {str(user.get('id')): infos}

    file_name = "{}.json".format(user.get('id'))
    with open(file_name, 'w', encoding='UTF8') as f:
        json.dump(content, f)


def main():
    """
    Gather all tasks of an employee based on ID in JSON format
    using a REST API
    """
    import requests
    import sys

    user_id = int(sys.argv[1])
    user = requests.get('https://jsonplaceholder.typicode.com/users/' +
                        '{}'.format(user_id))
    todos = requests.get('https://jsonplaceholder.typicode.com/todos' +
                  
