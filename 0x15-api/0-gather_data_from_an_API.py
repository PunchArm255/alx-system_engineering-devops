#!/usr/bin/python3
"""
Displays user todo list using json placeholder rest api
"""


def main():
    """
    Returns information about todo list progress of given employee ID
    using a rest api
    """
    import requests
    import sys

    user_id = int(sys.argv[1])
    user = requests.get('https://jsonplaceholder.typicode.com/users/' +
                        '{}'.format(user_id))
    todos = requests.get('https://jsonplaceholder.typicode.com/todos' +
                         '?userId={}'.format(user_id))

    done = [task for task in todos.json() if task.get('completed', False)]
    print("Employee {} is done with tasks".format(user.json().get('name')) +
          "({}/{}):".format(len(done), len(todos.json())))
    for task in done:
        print("\t {}".format(task.get('title')))


if __name__ == '__main__':
    main()
