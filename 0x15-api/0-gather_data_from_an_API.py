#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""


import requests
import sys


def employee_progress(employee_id):
    '''function to get and display the todo list progress
    for an employee with it's given id'''
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = (
            f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
            )
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    user_response = requests.get(user_url)
    user_data = user_response.json()
    employee_name = user_data.get('name')

    total_tasks = len(todos_data)
    completed_tasks = [task for task in todos_data if task.get('completed')]
    number_of_done_tasks = len(completed_tasks)
    print(f"Employee {employee_name} is done with tasks"
          f"({number_of_done_tasks}/{total_tasks}):")

    for task in completed_tasks:
        print(f"\t {task.get('title')}")


if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    employee_progress(employee_id)
