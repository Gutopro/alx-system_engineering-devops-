#!/usr/bin/python3
"""Exports to-do list information of all employees to JSON format."""
import json
import requests
import sys

if len(sys.argv) != 2:
        print("Usage: {} EMPLOYEE_ID".format(sys.argv[0]))
            sys.exit(1)

            employee_id = sys.argv[1]

            # Retrieve employee information
            employee_response = requests.get("https://jsonplaceholder.typicode.com/users/{}".format(employee_id))
            employee_response.raise_for_status()
            employee = employee_response.json()

            # Retrieve TODO list information
            todo_response = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}".format(employee_id))
            todo_response.raise_for_status()
            todo_list = todo_response.json()

            # Extract completed tasks
            completed_tasks = [task for task in todo_list if task['completed']]

            # Print employee TODO list progress
            print("Employee {} is done with tasks({}/{}):".format(employee['name'], len(completed_tasks), len(todo_list)))
            for task in completed_tasks:
                    print("\t {}".format(task['title']))
                    
