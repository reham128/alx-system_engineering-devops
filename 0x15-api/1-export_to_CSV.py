#!/usr/bin/python3
"""
Based on previouse task extend your Python
script to export data in the CSV format.
"""


import requests
import sys
import csv


def employee_progress(employee_id):
    '''Function to get and display the TODO list progress
    for an employee with its given id and export to CSV'''

    # API endpoints
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = (
        f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    )

    # Fetch TODO list data
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Fetch user data
    user_response = requests.get(user_url)
    user_data = user_response.json()
    employee_name = user_data.get('username')
    employee_id = user_data.get('id')

    # Prepare CSV file name
    file_name = f"{employee_id}.csv"

    # Write data to CSV file
    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in todos_data:
            writer.writerow([
                employee_id,
                employee_name,
                task.get('completed'),
                task.get('title')
            ])

    # Displaying progress (optional)
    total_tasks = len(todos_data)
    completed_tasks = [task for task in todos_data if task.get('completed')]
    number_of_done_tasks = len(completed_tasks)

    print(f"Employee {employee_name} is done with tasks "
          f"({number_of_done_tasks}/{total_tasks}):")

    for task in completed_tasks:
        print(f"\t {task.get('title')}")


if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    employee_progress(employee_id)
