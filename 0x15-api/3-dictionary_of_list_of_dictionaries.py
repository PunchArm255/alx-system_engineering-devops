#!/usr/bin/python3
"""
This script exports all users tasks using {JSON} Placeholder REST API
into a JSON file
"""


def user_tasks(user, tasks):
    """
    Returns list of all tasks' info about a user
    """
    infos = []
    for task in tasks:
        task_info = {
            'username': user.get('username'),
            'task': task.get('title'),
            'completed': task.get('completed'),
        }
        infos.append(task_info)
    return infos


def main():
    """
    Gather all tasks of of all employees in JSON format
    using a REST API
    """
    import json
    import requests
    import sys

    users = requests.get('https://jsonplaceholder.typicode.com/users/')
    content = {}

    for user in users.json():
        todos = requests.get('https://jsonplaceholder.typicode.com/todos' +
                             '?userId={}'.format(user.get('id')))
        content[str(user.get('id'))] = user_tasks(user, todos.json())

    with open("todo_all_employees.json", "w", encoding="UTF8") as f:
        json.dump(content, f)


if __name__ == '__main__':
    main()
