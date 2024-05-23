#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""


import json
import requests


def fetch_data():
    users_url = 'https://jsonplaceholder.typicode.com/users'
    todos_url = 'https://jsonplaceholder.typicode.com/todos'

    users_response = requests.get(users_url)
    todos_response = requests.get(todos_url)

    users = users_response.json()
    todos = todos_response.json()

    return users, todos


def create_data_structure(users, todos):
    data = {}
    users_dict = {user['id']: user['username'] for user in users}

    for todo in todos:
        user_id = todo['userId']
        task_info = {
            "username": users_dict[user_id],
            "task": todo['title'],
            "completed": todo['completed']
        }
        if user_id not in data:
            data[user_id] = []
        data[user_id].append(task_info)

    return data


def export_to_json(data, filename='todo_all_employees.json'):
    with open(filename, 'w') as json_file:
        json.dump(data, json_file)


def main():
    users, todos = fetch_data()
    data = create_data_structure(users, todos)
    export_to_json(data)


if __name__ == "__main__":
    main()
