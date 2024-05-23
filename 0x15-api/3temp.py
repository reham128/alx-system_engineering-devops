#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
extend your Python script to export data in the JSON format.
"""


import json
import requests
import sys


def employee_progress():
    '''function to get and display the todo list progress
    for an employee with it's given id'''
    user_url = f"https://jsonplaceholder.typicode.com/users"

    user_response = requests.get(user_url)
    user_data = user_response.json()

    all_employees_tasks = {}
    for user in user_data:
        name = user.get('username')
        userid = user.get('id')

        todos_url = (
                f"https://jsonplaceholder.typicode.com/users/{userid}/todos"
                )
        todos_response = requests.get(todos_url)
        todos_data = todos_response.json()

        tasks_list = []
        for task in todos_data:
            dict_task = {
                    "username": name,
                    "task": task.get('title'),
                    "completed": task.get('completed')
                    }
            tasks_list.append(dict_task)

    filename = 'todo_all_employees.json'
    with open(filename, mode='w') as json_file:
        json.dump(all_employees_tasks, json_file)


if __name__ == "__main__":

    employee_progress()
